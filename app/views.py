from django.shortcuts import render, redirect
from .models import Contact, Portfolio, Phonenumber
import requests


def index(request):
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
        # url = f"https://api.telegram.org/bot6548466627:AAFhjI1BZNAbvsVAtUkOb1Ms_6tykRjHYxU/sendMessage?chat_id=594445343&text=you \
        # have a notification from incorp website: {data['message']}"
        # result = requests.get(url)
        return redirect('/')

    return render(request, "index.html", context=d, )
