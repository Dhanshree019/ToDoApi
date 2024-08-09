from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from ToDoApi.models import *
from ToDoApi.serializers import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# Create your views here.


class ToDoView(APIView):
    def get(self,request):
        todo_id = request.GET.get('todo_id')
        todo_details = None
        if todo_id:
            todo_details = ToDoData.objects.filter(id=todo_id).first()
            if todo_details is not None:
                todo_details = ToDoSerializer(todo_details).data

        else:
            todo_details = ToDoData.objects.all()
            if len(todo_details) > 0:
                todo_details = ToDoSerializer(todo_details, many=True).data

        if todo_details is not None:
            return Response({"message": "Data reterived successfully","data": todo_details},status=200)
        else:
            return Response({"message": "Data not found"},status=404)


    def post(self, request):
        todo_data = request.data

        ToDoData.objects.create(title=todo_data["title"],description=todo_data["description"])

        return Response({"Message":"To Do created succesfully"},status=201)


@csrf_exempt
def home(request):

    if request.method == "POST":
        email = request.POST.get('email')
        return render(request, 'result.html', {"email": email})

    return render(request, 'home.html')

