from django.shortcuts import render

def index(request):
    return render(request,'<h2>hello</h2>')
