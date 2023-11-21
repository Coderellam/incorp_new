from django.shortcuts import render, redirect
from .models import Contact, Portfolio, Phonenumber
import requests
from .forms import MyForm
from django.contrib import messages
from django import forms
from captcha.fields import CaptchaField


def home(request):
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            messages.success(request, "Success!")
        else:
            messages.error(request, "Wrong Captcha!")

        form = MyForm()
        return render(request, 'index.html', {'form': form})


def index(request):
    data = request.GET
    lang = data.get("lang")

    # if lang is None:
    #     lang = "en"
    #
    # if lang == "en":
    #     return render(request, "en/index.html")
    #
    # elif lang == "ru":
    #     return render(request, "ru/index.html")

    phone_numbers = Phonenumber.objects.all()
    portfs = Portfolio.objects.filter(is_active=True)

    d = {
        'portfolios': portfs,
        'phone_numbers': phone_numbers
    }

    if request.method == "POST":
        data = request.POST
        print(data)

        service_web = True if data.get('service-web') == 'on' else False
        service_mob = True if data.get('service-mob') == 'on' else False
        service_ux = True if data.get('service-ux') == 'on' else False
        service_plt = True if data.get('service-plt') == 'on' else False
        obj = Contact.objects.create(name=data['name'], surname=data['surname'], email=data['email'],
                                     message=data['message'], number=data['number'],
                                     web_development=service_web
                                     , ux_ui=service_ux, internet_platform=service_plt,
                                     mobile_development=service_mob)

        obj.save()
        # # import requests
        #
        # chat_ids = ['594445343', '788076346']
        # for chat_id in chat_ids:
        #     url = f"https://api.telegram.org/bot6548466627:AAFhjI1BZNAbvsVAtUkOb1Ms_6tykRjHYxU/sendMessage?chat_id={chat_id}&text=you have a notification from incorp website: {data['message']}"
        #
        #     result = requests.get(url)
        #
        # return redirect('/')

        url = f"https://api.telegram.org/bot6548466627:AAFhjI1BZNAbvsVAtUkOb1Ms_6tykRjHYxU/sendMessage?chat_id=748076346&text=you have a notification from incorp website: {data['message']}"
        result = requests.get(url)
        return redirect('/')
    # 748076346 /  594445343
    return render(request, "index.html", context=d, )
