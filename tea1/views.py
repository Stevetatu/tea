from django.shortcuts import render
from .models import Tea

# Create your views here.
def tea_list(request):
    # Logic to retrieve and display a list of teas
    tea = Tea.objects.all()
    username("owen", "smith")
    return render(request, 'core/tea.html', {'tea': tea, 'username': username})

def tea_blog(request):
    # Logic to retrieve and display a list of teas
    tea = Tea.objects.all()
    return render(request, 'core/tea_blog.html')

def username(first_name, last_name):
    return f"{first_name} {last_name}"