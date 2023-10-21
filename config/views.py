from django.shortcuts import render
from rest_framework.views import APIView


class Main(APIView):
    def get(self, request):
        print("get")
        return render(request, "instagram/main.html")

    def post(self, request):
        print("post")
        return render(request, "instagram/main.html")
