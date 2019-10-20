# I have created this file - Kunal

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # return HttpResponse("Home")
    return render(request, 'index.html')

def analyze(request):
    # get the text:
    djtext = request.POST.get('text','default')

def about_us(request):
    return render(request,"about_us.html")

def contect_us(request):
    return render(request,"contect_us.html")

    # Check checkbox values
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    charcount = request.POST.get('charcount','off')

    # Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose':'Removed Punctuations','analyzed_text':analyzed}
        # Analyse the text:
        djtext = analyzed
        return render(request,'analyze.html',params)

    if(fullcaps == "on"):
        analyzed = " "
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose':'Change to Uppercase','analyzed_text':analyzed}
        # Analyse the text:
        djtext = analyzed
        return render(request,'analyze.html',params)

    if(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose':'Remove new Lines','analyzed_text':analyzed}
        # Analyse the text:
        djtext = analyzed
        return render(request,'analyze.html',params)

    if(extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose':'Remove Extra Space','analyzed_text':analyzed}
        # Analyse the textdjtext = analyzed
        djtext = analyzed
        return render(request,'analyze.html',params)

    if(charcount == "on"):
        count = 0
        for char in djtext:
            if char != " ":
                count+=1
        params = {'purpose':'Character Count','analyzed_text':count}

    if(removepunc != "on" and fullcaps != "on" and newlineremover != "on" and extraspaceremover != "on" and charcount != "on"):
        return HttpResponse('Error')

    return render(request,'analyze.html',params)
