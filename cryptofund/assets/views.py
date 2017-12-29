from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Client, DollarDeposit, share_price, total_shares, total_value
from django.core.exceptions import ObjectDoesNotExist
from .forms import LoginForm


def login(request):
    request.session.flush()
    error_message = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            try:
                client = Client.objects.get(access_code=form.cleaned_data["access_code"])
                request.session["client"] = str(client.uuid)
                return HttpResponseRedirect('/')
            except ObjectDoesNotExist:
                error_message = "Invalid access code."
        else:
            error_message = "Invalid authentication request."
                # TODO: make this dynamic
    form = LoginForm()
    return render(request, 'assets/login.html', {'form': form, 'error': error_message})


def logout(request):
    request.session.flush()
    return HttpResponseRedirect('/')


def dashboard(request):
    if not is_authenticated(request):
        return HttpResponseRedirect("/")

    client = Client.objects.get(uuid=request.session["client"])
    context = {
        "client": client,
        "value": str_num((client.shares / total_shares()) * total_value()),
        "total_shares": str_num(total_shares()),
        "total_assets": str_num(total_value()),
        "shares": str_num(client.shares),
        "share_price": str_num(share_price()),
        "deposits": str_num(client.deposits()),
        "deposits_log": DollarDeposit.objects.filter(client=client),
        "percent": client.str_percent_change(),
        "change": str_num(client.change()),
        "growth": client.change() >= 0
    }
    return render(request, 'assets/dashboard.html', context=context)


def index(request):
    if is_authenticated(request):
        return HttpResponseRedirect('dashboard/')
    else:
        request.session.flush()
        return HttpResponseRedirect('login/')

def is_authenticated(request):
    return 'client' in request.session and Client.objects.get(uuid=request.session["client"]) is not None

def str_num(num):
    return "{0:,.2f}".format(num)