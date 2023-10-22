from django.shortcuts import render
from .models import Contact, Portfolio
import requests


def index(request):
    portfs = Portfolio.objects.all()
    d = {
        'portfolios': portfs
    }

    if request.method == "POST":
        data = request.POST
        obj = Contact.objects.create(name=data['name'], surname=data['surname'], email=data['email'],
                                     message=data['message'], number=data['number'])

        obj.save()
        url = f"https://api.telegram.org/bot6548466627:AAFhjI1BZNAbvsVAtUkOb1Ms_6tykRjHYxU/sendMessage?chat_id=748076346&text=you have a notification from incorp website: {data['message']}"
        result = requests.get(url)

    return render(request, "index.html", context=d)
