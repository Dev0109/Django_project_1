from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

# Create your views here.
def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers' : mymembers,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    mymembers = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymembers' : mymembers,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())