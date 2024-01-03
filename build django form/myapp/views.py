# myapp/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Student
from .forms import StudentForm

def index(request):
    students = Student.objects.all()
    return render(request, 'myapp/index.html', {'students': students})

def delete_student(request, roll):
    student = get_object_or_404(Student, roll=roll)
    student.delete()
    return HttpResponseRedirect(reverse('index'))

def update_student(request, roll):
    student = get_object_or_404(Student, roll=roll)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = StudentForm(instance=student)

    return render(request, 'myapp/update_student.html', {'form': form, 'student': student})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = StudentForm()

    return render(request, 'myapp/add_student.html', {'form': form})