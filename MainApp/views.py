from django.http import Http404
from django.shortcuts import render, redirect
from MainApp.models import Snippet
from MainApp.forms import SnippetForm
from MainApp.forms import UserForm




def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


def add_snippet_page(request):
    if request.method == "GET":
        form = SnippetForm()
        context = {
            'pagename': 'Добавление нового сниппета',
            'form': form
        }
        return render(request, 'pages/add_snippet.html', context)
    if request.method == "POST":
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("snippetslist")
        return render(request, 'pages/add_snippet.html', {'form': form})



def snippets_page(request):
    snippets = Snippet.objects.all()
    context = {'pagename': 'Просмотр сниппетов',
                'snippets': snippets,
                'lensnippets':len(snippets)}
    return render(request, 'pages/view_snippets.html', context)

def get_snippet(request, snippet_id):
    try:
        snippet = Snippet.objects.get(id=snippet_id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f'Snippet with id = {snippet_id} not found.')
    context = {
        "snippet":snippet
    }
    if request.method == "POST":
        return render(request, 'pages/edit_snippet.html', context)
    return render(request, 'pages/snippet.html', context)

def create_snippet(request):
   if request.method == "POST":
       form = SnippetForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect("snippetslist")
       return render(request,'pages/add_snippet.html',{'form': form})

def req_del(request, snippet_id):
    try:
        snippet = Snippet.objects.get(id=snippet_id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f'Snippet with id = {snippet_id} not found.')
    context = {
        "snippet":snippet
    }
    return render(request, 'pages/snippet_delete.html', context)

def delete_snippet(request, snippet_id):
    snippet = Snippet.objects.get(id=snippet_id)
    if request.method =="POST":
        snippet.delete()
    return redirect('snippetslist')
 
    return render(request, "pages/delete_snippet.html")

def edit_snippet(request, snippet_id):
    snippet = Snippet.objects.get(id=snippet_id)
    if request.method =="POST":
        if 'saved' in request.POST:
            snippet.name = request.POST.get("name")
            snippet.code = request.POST.get("code")
        snippet.save()
    return redirect('snippetslist')





