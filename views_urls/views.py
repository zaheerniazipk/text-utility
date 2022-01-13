#  Self Created File
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


# Text Analyzer
def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    # Global Variable
    purpose = ''

    # Remove punctuations
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}

        # Analyze the text
        djtext = analyzed
        purpose += " Removed Punctuations "
        # return render(request, 'analyze.html', params)

    # Full Capitalize
    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}

        # Analyze the text
        djtext = analyzed
        purpose += " | Change To Uppercase "
        # return render(request, 'analyze.html', params)

    # New Line Remover
    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
            else:
                print("no")
        print("pre", analyzed)
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

        # Analyze the text
        djtext = analyzed
        purpose += " | Remove Newlines "
        # return render(request, 'analyze.html', params)

    #  Extra Space Remover
    if extraspaceremover == "on":
        analyzed = ""
        for indx, char in enumerate(djtext):
            if not (djtext[indx] == " " and djtext[indx + 1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

        # Analyze the text
        djtext = analyzed
        purpose += " | Remove Extra Spaces "
        # return render(request, 'analyze.html', params)

    # Purpose & Output
    params = {'purpose': purpose, 'analyzed_text': djtext}

    # Character Count
    if charcount == 'on':
        analyzed = 0

        for char in djtext:
            if not (char.isspace()):
                analyzed = analyzed + 1

        params = {'purpose': 'Character Count', 'analyzed_text': analyzed}

        # Analyze the text
        characters = "Total Characters: " + str(analyzed)
        purpose += " | Character Count"

        params = {'purpose': purpose, 'analyzed_text': djtext, 'Total_characters': characters}

    # what if none of if statement is selected
    if removepunc != "on" and newlineremover != "on" and extraspaceremover != "on" and fullcaps != "on" and charcount != 'on':
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)
