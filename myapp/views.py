from django.shortcuts import render,HttpResponse
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.conf import settings
from .models import Student

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

# Create your views here


def StudentApi(request):
    if 'student' in cache:
        products = cache.get('student')
        print("in if statment")
        return HttpResponse(products)
    else:
        print("in else statment")
        results = list(Student.objects.all().values())
        cache.set("student", results, timeout=CACHE_TTL)
        return HttpResponse(results)