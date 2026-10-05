from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response

from employee import serializers
from employee.models import Employee
from employee.serializers import EmployeeSerializer


class Employeelist(APIView):
    def get(self,request):
        s=Employee.objects.all()
        serializer_instance=EmployeeSerializer(s,many=True)
        #converts qs into python native datatypes
        #qs contains more than one record so we use many=True
        return Response(data=serializer_instance.data)

#API view for creating a new student record
from json import loads
# from django.utils.decorators import method_decorator
# from django.views.decorators.csrf import csrf_exempt
# @method_decorator(csrf_exempt,name="dispatch")
class Employeecreate(APIView):
    def post(self,request):
        #View recieves data as request.data (client side data python native type)
        #Calls serializer class for deserialization . here we pass request.data as argument
        #after validation serializer saves data as model object inside db table
        serializer_instance=EmployeeSerializer(data=request.data)
        # e=data['empid']
        # n=data['name']
        # a=data['age']
        # p=data['place']
        # g=data['gender']
        # sa=data['salary']
        # d=data['designation']
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)

#API View for reading a specific record


class Employeedetail(APIView):
    def get(self,request,i):
        #Reads employee objects from model
        # e=Employee.objects.get(id=i)
        e=get_object_or_404(Employee,id=i)
        #converts model object to python native using EmployeeSerializer
        serializer_instance=EmployeeSerializer(e)
        #sends the response as json
        return Response(serializer_instance.data)

#API View for deleting a specific record
class Employeedelete(APIView):
    def delete(self,request,i):
        # s=Employee.objects.get(id=i)
        e=get_object_or_404(Employee,id=i)
        e.delete()
        return Response({"message":"Deleted Successfully"})


# import json

# @method_decorator(csrf_exempt,name="dispatch")
# class Employeefullupdate(View):
#     def put(self,request,i):
#         data = json.loads(request.body)
#         print(data)
#
#         s=Employee.objects.get(id=i)
#         s.empid = data['empid']
#         s.name =data['name']
#         s.age = data['age']
#         s.place = data['place']
#         s.salary =data['salary']
#         s.joindate= data['joindate']
#         s.designation = data['designation']
#         s.save()
#         return JsonResponse({"message":"updated Successfully"})
#
#
# @method_decorator(csrf_exempt,name="dispatch")
# class Employeepartalupdate(View):
#     def patch(self,request,i):
#         data = json.loads(request.body)
#         print(data)
#
#         s=Employee.objects.get(id=i)
#         if 'empid' in data :
#             s.empid= data['empid']
#         if 'name' in data:
#             s.name =data['name']
#         if 'age' in data:
#             s.age = data['age']
#         if 'place' in data:
#             s.place = data['place']
#         if 'salary' in data:
#             s.salary =data['salary']
#         if 'joindate' in data:
#             s.joindate =data['joindate']
#         if 'designation' in data:
#             s.designation =data['designation']
#         s.save()
#         return JsonResponse({"message":"updated partally"})