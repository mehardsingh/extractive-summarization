from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
import json
from django.contrib.auth.models import User #####
from django.http import JsonResponse , HttpResponse ####

from wiki.summarize import summarize as sm

def index(request):
    return HttpResponse("Hello, world. You're at the wiki index.")


# https://pypi.org/project/wikipedia/#description
def get_wiki_summary(request):
    topic = request.GET.get('topic', None)

    print('topic:', topic)
    print(sm.summarize(topic))
    results = sm.summarize(topic)

    data = {
        'summary': results[0],
        'keywords': results[1],
        'raw': 'Successful',
    }

    print('json-data to be sent: ', data)

    return JsonResponse(data)