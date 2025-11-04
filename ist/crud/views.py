from django.shortcuts import redirect, render,get_object_or_404
from .models import Student
from .forms import StudentForm

def CreateView(request):
    if request.method == 'POST':
        form =StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form=StudentForm()
    return render(request, 'crud/form.html', {"form":form})

def ShowView(request):
    student = Student.objects.all()
    return render(request, 'crud/show.html', {"student":student})

def updateView(request, f_Sid):
    student = get_object_or_404(Student, Sid=f_Sid)
    form = StudentForm(instance=student)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
                form.save()
                return redirect('list') 
    return render(request, 'crud/form.html', {"form":form})

def deleteView(request, f_Sid):
    student = get_object_or_404(Student, Sid=f_Sid)
    if request.method == 'POST':
        student.delete()
        return redirect('list')
    return render(request, 'crud/confirm.html', {'student': student})


