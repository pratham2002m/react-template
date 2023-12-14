from django.shortcuts import render
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import pandas as pd
import numpy as np
from rest_framework import status
from django.utils.decorators import method_decorator



# Create your views here.

class DM(APIView) :
    @method_decorator(csrf_exempt)
    def post(self, request) :
        try:
                
            # file = request.FILES.get('file')
            # df = pd.read_csv(file)
            
            # print(df)
            print("test")
            
            return JsonResponse({"accuracy": "accuracy"})
        except Exception as e :
            print(e)
            return JsonResponse({"error => ": str(e)}, status=status.HTTP_200_OK, safe=False)