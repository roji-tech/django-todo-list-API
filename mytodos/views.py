from django.shortcuts import redirect, render
from .models import Todo
from .forms import TodoForm


# Create your views here.


def list_todos(request):
    todos = Todo.objects.all().order_by("-created")
    total_todos = Todo.objects.count()
    no_todo = False if total_todos == 0 else True
    print(total_todos)
    print(no_todo)

    form = TodoForm()
    context = {
        "todos": todos,
        "total_todos": total_todos,
        "form": form,
        "no_todo": no_todo
    }
    return render(request, 'index.html', context)


def add_todos(request):
    form = TodoForm(request.POST or None)

    if form.is_valid():
        form.save()
        form = TodoForm()

    return redirect("/")


def del_todo(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()

    return redirect("/")


def completedTodo(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.completed = not todo.completed
    todo.save()
    return redirect('/')


def delete_completed(request):
    Todo.objects.filter(completed__exact=True).delete()

    return redirect('/')


def delete_all_todos(request):
    Todo.objects.all().delete()

    return redirect('/')
