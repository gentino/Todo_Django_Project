from django.shortcuts import render,redirect,get_object_or_404
from .models import Tasks
from .forms import RegisterForm, LoginForm, TaskForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    tasks = Tasks.objects.filter(owner=request.user)
    total_task = tasks.count()
    undone_tasks =tasks.filter(done=False).count()
    context = {
        'tasks': tasks,
        'total_task':total_task,
        'undone_tasks':undone_tasks,
    }
    return render(request,'index.html', context)

def signup(request):
    if request.method == 'POST':
        form =RegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            messages.success(request,f'Welcome {user.username} Your account was setup successfully')
            return redirect('/index')
            
    else:
        form = RegisterForm()
        
    return render(request,'registration/register.html',{'form':form})
    

def signin(request):
    if request.method == 'POST':
        form =LoginForm(request,data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return  redirect('index')
    else:
        form =LoginForm()
        
    return render(request,'registration/login.html',{'form': form})

@login_required
def create(request):
    
    if request.method =="POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f'You Task successfully added')
            return redirect('index')
    else:
        form = TaskForm()
    
    return render(request,'create.html', {'form': form})

@login_required
def task_edit(request,pk):
    task=get_object_or_404(Tasks,pk=pk)
    if request.method=='POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request,f'Task updated successfully')
            return redirect('index')
    else:
        form = TaskForm(instance=task)
    return render(request,'task_edit.html',{'form':form, 'task': task})

@login_required
def delete_task(request,pk):
    task = get_object_or_404(Tasks,pk=pk)
    if request.method=='POST':
        task.delete()
        messages.success(request,f'Task deleted successfully')
        return redirect('index')
    return render(request,'delete_task.html',{'task':task})