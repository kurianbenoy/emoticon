# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView,FormView
from django.core.urlresolvers import reverse

from .forms import Search

# Create your views here.


def home(request):
	form = Search()
	ser=False;
	if request.method =='POST' :
		ser=True
		form=Search(request.POST)
		if form.is_valid():
			data = form.cleaned_data['search_text']
			# print data
			a =67
			b =23
			c =10
		# data=" "	
		context = {'form':form,'data':data,'positive':a,'negative':b,'neutral':c,'ser':ser}
		return render(request,'index.html',context)
	else:	
		form = Search()
		context ={'form':form,'ser':ser}
	return render(request,'index.html',context)






