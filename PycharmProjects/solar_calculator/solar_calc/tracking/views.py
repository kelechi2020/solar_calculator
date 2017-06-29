from django.shortcuts import render
from __future__ import unicode_literals
from django.shortcuts import redirect
from .forms import InspirationalQuoteForm

def add_quote(request):
    if request.method == "POST":
        form = InspirationalQuoteForm(data=request.POST,files=request.FILES,)
        if form.is_valid():
            quote = form.save()
            return  redirect ("aadd_quote_done")
        else:
            form = InspirationalQuoteForm()
        return render("tracking/change_quote.html",{"form": form})

# Create your views here.
