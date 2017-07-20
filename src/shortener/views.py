# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.shortcuts import render,get_object_or_404
from django.views import View
from analytics.models import ClickEvent
from .forms import SubmitUrlForm
from .models import RakibbUrl
# Create your views here.

class HomeView(View):
    def get(self,request,*args,**kwargs):
        the_form=SubmitUrlForm()
        bg_image='http://webneel.com/wallpaper/sites/default/files/images/04-2013/dreamy-beach-wallpaper.preview.jpg'
        context={
            'title':'Rakibb.co',
            'form':the_form,
            'bg_image':bg_image
        }
        return render(request,"shortener/home.html",context)
    def post(self, request, *args, **kwargs):
        form = SubmitUrlForm(request.POST)
        context = {
            "title": "Rakibb.co",
            "form": form
        }
        template = "shortener/home.html"
        if form.is_valid():
            new_url = form.cleaned_data.get("url")
            obj, created = RakibbUrl.objects.get_or_create(url=new_url)
            context = {
                "object": obj,
                "created": created,
            }
            if created:
                template = "shortener/success.html"
            else:
                template = "shortener/already-exists.html"

        return render(request, template ,context)

class URLRedirectView(View):
    """docstring for RAkibbRedirectView."""
    def get(self,request,shortcode=None,*args,**kwargs):
        #obj=get_object_or_404(RakibbUrl,shortcode=shortcode)
        qs=RakibbUrl.objects.filter(shortcode__iexact=shortcode)
        if qs.count()!=1 and not qs.exists():
            raise Http404
        obj=qs.first()
        print(ClickEvent.objects.create_event(obj))
        return HttpResponseRedirect(obj.url)
