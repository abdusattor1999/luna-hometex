from django.utils.translation import gettext_lazy as _
from django.shortcuts import render
from .models import News, Product
from .forms import MessageForm
from django.contrib import messages
from django.conf import settings
import requests
from django.utils.translation import get_language, activate, gettext

def send_message(text, chat_id):
    telegram_api = f"https://api.telegram.org/bot{settings.BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "HTML",
    }
    req = requests.post(telegram_api, data=payload)
    return req.status_code

def index(request):
    print("Language: ", get_language())
    products = Product.objects.all()
    news = News.objects.all()
    return render(request, "index.html", locals())

def about(request):
    return render(request, "about.html")

def news_list(request):
    news = News.objects.all()
    return render(request, "news_list.html", {"news": news})

def news_detail(request, pk):
    new = News.objects.get(id=pk)
    return render(request, "news_detail.html", {"new": new})

def product_details(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, "product_detail.html", {"product": product})

def contact(request):
    try:
        if request.method == "POST":
            form = MessageForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, _("Xabaringiz muvaffaqiyatli yuborildi"))
                form_data = form.cleaned_data
                message_text = (
                    "<b>Yangi habar !</b>",
                    f"Ism : {form_data['first_name']}",
                    f"Familiya: {form_data['last_name']} ",
                    f"Email: {form_data['email']}",
                    f"Xabar: {form_data['message']}",
                )
                send_message("\n".join(message_text), settings.ADMIN_ID)
                return render(request, "contact.html", {"form": MessageForm()})
        else:
            form = MessageForm()    
            return render(request, "contact.html", {"form": form})
        
    except Exception as e:
        print(e)