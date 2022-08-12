from django.http import HttpResponse
from django.shortcuts import render

from PyDictionary import PyDictionary
# Create your views here.

# home page
def index(request):
    return render(request,'index.html')

def word(request):

    try:
        search = request.GET.get('search')

        dictionary = PyDictionary()
        meaning = dictionary.meaning(search)
        synonyms = dictionary.synonym(search)
        antonyms = dictionary.antonym(search)

        context={'meaning':meaning,'synonyms':synonyms,'antonyms':antonyms}
        return render(request,'index.html',context)

    except:
        return HttpResponse('<div style="text-align: center;margin-top: 50px;"><h1>Opps..! Something went wrong</h1><a href="/">Back</a></div>')