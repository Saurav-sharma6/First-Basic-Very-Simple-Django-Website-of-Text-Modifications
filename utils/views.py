# Views.py
# I have created this file - Harry
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

    # return HttpResponse("Home")



def analyze(request):
    #Get the text
   djtext = request.GET.get('text', 'default')
   copy=djtext

   # Check checkbox values
   removepunc = request.GET.get('removepunc', 'off')
   fullcaps = request.GET.get('fullcaps', 'off')
   newlineremove = request.GET.get('newlineremove', 'off')
   extraspaceremover = request.GET.get('extraspaceremover', 'off')
   counter = request.GET.get('counter', 'off')

    #Check which checkbox is on
   if removepunc == "on":
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    analyzed = ""
    for char in djtext:
         if char not in punctuations:
                analyzed = analyzed + char
    params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
    #return render(request, 'analyze.html', params)
    djtext=analyzed
   if fullcaps=="on":
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
       # return render(request, 'analyze.html', params)
        djtext=analyzed

   if newlineremove=="on":
       analyzed =""
       for char  in djtext:
           if char!='\n' and char!='\r':
            analyzed = analyzed + char
       params = {'purpose': 'New Line Remover', 'analyzed_text': analyzed}
       #return render(request, 'analyze.html', params)
       djtext=analyzed

   if extraspaceremover=="on":
       analyzed = ""
       for char in djtext:
           if char!=' ':
               analyzed=analyzed+char
       params = {'purpose': 'Space Remover', 'analyzed_text': analyzed}
       #return render(request, 'analyze.html', params)
       djtext=analyzed

   if counter == "on":
       analyzed = len(djtext)
       params = {'purpose': 'Lenght', 'analyzed_text':analyzed}
       djtext=analyzed

   if(counter!='on' and fullcaps!='on' and extraspaceremover!="on" and newlineremove!="on" and removepunc!="on"):
       return HttpResponse("Plz Select Operation-- \n"+" "+copy)




   #else:
        #return HttpResponse("Error")
   return render(request, 'analyze.html', params)
#def capfirst(request):
 #   return HttpResponse("<a  href='google.com'>GOOGLE</a>")
#
# def newlineremove(request):
#     return HttpResponse("newline remove first")
#
#
# def spaceremove(request):
#     return HttpResponse("space remover back")
#
# def charcount(request):
#     return HttpResponse("charcount ")
