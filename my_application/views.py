from django.shortcuts import render

from django.http import HttpResponse

def homepage(request):
    context = {'title' : 'HOMEPAGE'}
    return render(request,template_name="my_application/homepage.html", context=context)
    # return render(request, template_name="my_application/homepage.html")  # , context=context)
    # return HttpResponse('<h1>Aceasta este prima pagina</h1>')

def despre(request):
    return  render(request,template_name='my_application/despre.html')
    return HttpResponse('<h1>Aceasta este pagina despre mine</h1>')