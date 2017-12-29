from django.db import models

from datetime import datetime, timedelta
import requests, string, random, uuid

from django.utils import timezone

class Client(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4())
    name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    access_code = models.CharField(max_length=8, default=''.join(random.choices(string.ascii_uppercase + string.digits, k=8)))
    email = models.CharField(max_length=200)
    shares = models.FloatField()

    def value(self):
        return (self.shares / total_shares()) * total_value()

    def deposits(self):
        deposits = DollarDeposit.objects.filter(client=self)
        sum = 0
        for deposit in deposits:
            sum += deposit.amount
        return sum

    def ratio(self):
        return self.value() / self.deposits()

    def change(self):
        return self.value() - self.deposits()

    def str_percent_change(self):
        amt = (self.ratio() * 100) - 100
        prefix = ""
        if amt > 0:
            prefix = "+"
        return prefix + "{0:,.2f}".format(amt)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.__repr__()

class DollarDeposit(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4())
    amount = models.FloatField()
    date = models.DateField(auto_now_add=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __repr__(self):
        return self.client.name + " ($" + str(self.amount) + ")"

    def __str__(self):
        return self.__repr__()

class Currency(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4())
    ticker = models.TextField(max_length=3)
    unit_value = models.FloatField(null=True, blank=True)
    value_last_updated = models.DateTimeField(null=True, blank=True)

    def get_unit_value_usd(self, force_refresh=False):
        if self.ticker == "usd":
            return float(1)

        if self.unit_value is None or self.value_last_updated is None or self.value_last_updated < (timezone.now() - timedelta(0,60)) or force_refresh:
            try:
                self.unit_value = requests.get("https://api.cryptonator.com/api/ticker/" + self.ticker + "-usd").json()["ticker"]["price"]
                self.value_last_updated = timezone.now()
                self.save()
            except Exception:
                print("Error occurred while trying to fetch value for " + self.ticker + ":")
                print(Exception)
        return float(self.unit_value)

    def __repr__(self):
        return self.ticker.upper()

    def __str__(self):
        return self.__repr__()


class Asset(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4())
    amount = models.FloatField()
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    location = models.TextField()

    def calculate_usd_value(self, force_refresh=False):
        """
        Calculate the value of the asset, given prices in a dictionary.
        :param usd_dict: usd_dict is a dictionary with currencies as keys and their USD value as values
        :return: the value of the asset, in dollars.
        """

        return float(self.amount) * float(self.currency.get_unit_value_usd(force_refresh=force_refresh))

    def __repr__(self):
        return str(self.amount) + " " + self.currency.ticker.upper() + " @ " + self.location

    def __str__(self):
        return self.__repr__()

def total_value():
    sum_total = float(0)
    for asset in Asset.objects.all():
        sum_total += asset.calculate_usd_value()
    return float(sum_total)
    # convert to float just in case


def total_shares():
    total = float(0)
    for shareholder in Client.objects.all():
        total += float(shareholder.shares)
    return float(total)

def share_price():
    return total_value() / total_shares()