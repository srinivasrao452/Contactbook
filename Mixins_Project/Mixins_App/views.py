
from django.shortcuts import render
from Mixins_App.models import Employee
from Mixins_App.serializers import EmployeeSerializer
from rest_framework import mixins, generics

class EmployeeListView(mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       generics.GenericAPIView):

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self,request):
        return self.list(request)

    def post(self,request):
        return self.create(request)


class EmployeeDetailView(mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin,
                         generics.GenericAPIView):

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self,request,pk):
        return self.retrieve(request)

    def put(self,request,pk):
        return self.update(request)

    def delete(self,request,pk):
        return self.destroy(request)
