from django.shortcuts import render, redirect
from .models import Contact, Portfolio, Phonenumber, Web, Mobile, Uxui, Expertiza, \
    Individual, Innopodxod, Technical, Gibkost, Inno_razrabotki1, Inno_razrabotki2, Inno_razrabotki3, Expertiza473

import requests
from .forms import FormWithCaptcha


def home(request):
    if request.method == "POST":
        return render(request, 'index.html')


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
    form = FormWithCaptcha()

    web = Web.objects.all().first()
    mobile = Mobile.objects.all().first()
    uxui = Uxui.objects.all().first()
    expertiza = Expertiza.objects.all().first()
    individual = Individual.objects.all().first()
    innopodxod = Innopodxod.objects.all().first()
    technical = Technical.objects.all().first()
    gibkost = Gibkost.objects.all().first()
    inno_razrabotki1 = Inno_razrabotki1.objects.all().first()
    inno_razrabotki2 = Inno_razrabotki2.objects.all().first()
    inno_razrabotki3 = Inno_razrabotki3.objects.all().first()
    expertiza473 = Expertiza473.objects.all().first()

    d = {
        'portfolios': portfs,
        'phone_numbers': phone_numbers,
        'form': form,

        'web': web,
        'mobile': mobile,
        'uxui': uxui,
        'expertiza': expertiza,
        'individual': individual,
        'innopodxod': innopodxod,
        'technical': technical,
        'gibkost': gibkost,
        'inno_razrabotki1': inno_razrabotki1,
        'inno_razrabotki2': inno_razrabotki2,
        'inno_razrabotki3': inno_razrabotki3,
        'expertiza473': expertiza473

    }

    if request.method == "POST":

        data = request.POST
        print(data)

        if len(data.get("g-recaptcha-response")) > 30:
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
            url = f"https://api.telegram.org/bot6548466627:AAFhjI1BZNAbvsVAtUkOb1Ms_6tykRjHYxU/sendMessage?chat_id=594445343&text=you have a notification from incorp website: {data['message']}"
            result = requests.get(url)
        return redirect('/')

    return render(request, "index.html", context=d, )
