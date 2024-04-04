from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .forms import EmployeeForm
from .models import Employee


class InfoView(View):
    template_name = "curd_app/info.html"
    form = EmployeeForm

    def get(self, request):
        form = self.form()
        context = {"form": form}
        return render(request,self.template_name, context)

    def post(self,  request, *args, **kwargs):
        form = self.form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
        return render(request, self.template_name, {"form": form})


class ShowView(View):
    template_name = "curd_app/show.html"
    form = EmployeeForm

    def get(self, request):
        form = self.form()
        obj = Employee.objects.all()
        context = {"obj": obj, "form": form}

        return render(request, self.template_name, context)

    def post(self , request, *args, **kwargs):
        form = self.form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('info_url')
        return render(request, self.template_name, {"form": form})


class UpdateView(View):
    template_name = "curd_app/info.html"
    form = EmployeeForm

    def get(self, request, pk):
        objs = Employee.objects.get(id=pk)
        form = self.form(instance=objs)
        context = {"objs": objs, "form": form}
        return render(request, self.template_name, context)

    def post(self, request, pk):
        objs = Employee.objects.get(id=pk)
        form = self.form(request.POST, instance=objs)
        if form.is_valid():
            form.save()
            return redirect('show_url')
        return render(request, self.template_name, {"form": form})


class DeleteView(View):
    template_name = "curd_app/confirm.html"
    form = EmployeeForm

    def get(self, request, pk):
        objs = Employee.objects.get(id=pk)
        form = self.form(instance=objs)
        context = {"objs": objs, "form": form}
        return render(request, self.template_name, context)

    def post(self, request, pk):
        obj = Employee.objects.get(id=pk)
        obj.delete()
        return redirect("show_url")

