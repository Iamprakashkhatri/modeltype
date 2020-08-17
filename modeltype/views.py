from django.shortcuts import render
from .models import Language,Framework,Movie,Character

def index(request):
    q1=Framework.objects.filter(language__name='python')
    q2=Language.objects.filter(framework__name='django')
    q3=Movie.objects.filter(character__name='Captain America')
    q4=Character.objects.filter(movies__name='Avengers')
    print(q1)
    print(q2)
    print(q3)
    return render(request,'modeltype/home.html',{})
