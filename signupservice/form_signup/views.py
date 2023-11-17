from django.shortcuts import render, HttpResponse
from rest_framework.response import Response
from .models import Signup
from .seriealizer import signup_serializer
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.
# def start(request):
#     return HttpResponse("The form sign-up sevice started")

class SignUp(APIView):
    def get(self, request, pk=None, format=None):

        if pk is not None:
            try:
                s= Signup.objects.get(id=pk)
                serializer=signup_serializer(s)
                return Response(serializer.data)
            except:
                return Response(f"No data found in the given id {pk}.")
            
        try:
            s=Signup.objects.all()
            serializer=signup_serializer(s, many=True)
            # print(serializer.data)
            return Response(serializer.data)
        except:
            return Response(f"No data found, check your inur well")
    
    def post(self, request, format=None):
        serializer=signup_serializer(data=request.data)
        try:
            print("thr try is working")
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        except:
            print("exception happen")
            return Response("The data is not acceptable, check it again")
        return Response("The data is not acceptable, check it again")
    
    def put(self, request, pk, format=None):
        try:
            s= Signup.objects.get(id=pk)
        except:
            return Response(f"No data found with the id{pk}")
        
        serializer=signup_serializer(s, request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response("Your data has been saved successfully")
        except:
            return Response("Check your data again, it's not saved")
    
    def delete(self, request, pk, format=None):
        try:
            s= Signup.objects.get(id=pk)
            s.delete()
            return Response("Successfully deleted")
        except:
            return Response("not deleted. Check your id or data again")