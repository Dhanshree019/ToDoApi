from django.shortcuts import redirect, render
from rest_framework.response import Response
from rest_framework.views import APIView
from ToDoApi.models import *
from ToDoApi.serializers import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# Create your views here.


# class ToDoView(APIView):
    
#     def get(self,request):
#         todo_id = request.GET.get('todo_id')
#         todo_details = None
#         if todo_id:
#             todo_details = ToDoData.objects.filter(id=todo_id).first()
#             if todo_details is not None:
#                 todo_details = ToDoSerializer(todo_details).data

#         else:
#             todo_details = ToDoData.objects.all()
#             if len(todo_details) > 0:
#                 todo_details = ToDoSerializer(todo_details, many=True).data

#         if todo_details is not None:
#             return Response({"message": "Data reterived successfully","data": todo_details},status=200)
#         else:
#             return Response({"message": "Data not found"},status=404)

#     def post(self, request):
#         todo_data = request.data

#         ToDoData.objects.create(title=todo_data["title"],description=todo_data["description"])

#         return Response({"Message":"To Do created succesfully"},status=201)


@csrf_exempt
def home(request):

    if request.method == "POST":

        title = request.POST.get('title', "New Todo")
        description = request.POST.get('description', "descrition")
        ToDoData.objects.create(title=title, description=description)

        data = ToDoData.objects.filter().order_by('-id')
        return render(request, 'todo/index.html', {"todos": data})

    data = ToDoData.objects.filter().order_by('-id')
    return render(request, 'todo/index.html', {"todos": data})



def todo_delete(request):

    todo_id = request.GET.get('t_id', None)

    ToDoData.objects.filter(id=todo_id).delete()

    return redirect('/todo/home')



@csrf_exempt
def edit_todo(request):
    if request.method == "POST":
        todo_id = request.GET.get('t_id', None)
        print(f"todo id : {todo_id}")
        edited_title = request.POST.get('edited_title',None)
        edited_description = request.POST.get('edited_description',None)
        ToDoData.objects.filter(id=todo_id).update(
            title = edited_title,
            description =  edited_description
        )
        return redirect('/todo/home')

    todo_id = request.GET.get('t_id',None)
    print(f"todo id : {todo_id}")
    if todo_id:
        data = ToDoData.objects.filter(id=todo_id).first()
        return render(request,'todo/edit.html',{"todo_data":data})
    



        

    























# @csrf_exempt
# def home(request):

#     if request.method == "POST":
#         email = request.POST.get('email')
#         return render(request, 'result.html', {"email": email})

#     return render(request, 'home.html')

