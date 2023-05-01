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

    try:
        count = Koan.objects.count()
        data = {'count': count}

        response = {'status': 'success', 'data': data}
    except Exception as e:
        response = {'status': 'error', 'error_messages': [str(e)]}
        return JsonResponse(response)

    return JsonResponse(response)

def get_all_koans(request):
    if request.method == 'GET':
        try:
            koans = Koan.objects.all()
            koans_serializer = KoanSerializer(koans, many=True)
            data = koans_serializer.data

            response = {'status': 'success', 'data': data}
            if 'error_messages' in data:
                data.pop('error_messages')
        except Exception as e:
            response = {'status': 'error', 'data': [], 'error_messages': [str(e)]}

        # remove error_messages field for successful requests
        if response['status'] == 'success':
            response.pop('error_messages', None)

        return JsonResponse(response, safe=False)

def get_koan(request, id):
    try:
        koan = Koan.objects.get(id=id)
        koan_serializer = KoanSerializer(koan)
        data = koan_serializer.data
        response = {'status': 'success', 'data': data}
    except Koan.DoesNotExist as e:
        response = {'status': 'error', 'error_messages': [str(e)]}

        # set status code based on response status
        status_code = status.HTTP_404_NOT_FOUND
        return JsonResponse(response, status=status_code, safe=False)

    response.pop('error_messages', None)

    # set status code based on response status
    status_code = status.HTTP_200_OK


    return JsonResponse(response, status=status_code, safe=False)


@csrf_exempt
def create_koan(request):
    if request.method == 'POST':
        # Check if the request body is empty
        if not request.body:
            return JsonResponse({'status': 'error', 'error_message': 'Empty request body'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            koan_data = JSONParser().parse(request)
        except:
            return JsonResponse({'status': 'error', 'error_message': 'Invalid request body format'}, status=status.HTTP_400_BAD_REQUEST)
        koan_serializer = KoanSerializer(data=koan_data)
        if koan_serializer.is_valid():
            koan_serializer.save()
            return JsonResponse({'status': 'success', 'data': koan_serializer.data}, status=status.HTTP_201_CREATED)
        return JsonResponse({'status': 'error', 'error_message': koan_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)