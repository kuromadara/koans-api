from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.response import Response

from .models import Koan
from .serializers import KoanSerializer
from rest_framework.decorators import api_view
from .models import *



# Create your views here.

class KoanCreateView(CreateView):
    model = Koan
    fields = ['title', 'koan', 'status']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


def koans_count(request):
    count = Koan.objects.count()
    return JsonResponse({'count': count})

def get_all_koans(request):
    if request.method == 'GET':
        koans = Koan.objects.all()
        koans_serializer = KoanSerializer(koans, many=True)
        return JsonResponse(koans_serializer.data, safe=False)

def get_koan(request, id):
    try:
        koan = Koan.objects.get(id=id)
    except Koan.DoesNotExist:
        return JsonResponse({'message': 'The koan does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = KoanSerializer(koan)
        return JsonResponse(serializer.data)

# @csrf_exempt
def create_koan(request):
    if request.method == 'POST':
        koan_data = JSONParser().parse(request)
        koan_serializer = KoanSerializer(data=koan_data)
        if koan_serializer.is_valid():
            koan_serializer.save()
            return JsonResponse(koan_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(koan_serializer.errors, status=status.HTTP_400_BAD_REQUEST)