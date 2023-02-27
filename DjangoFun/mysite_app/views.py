# from django.http import HttpResponse

# # Create your views here.
# def mysite_view(request):
#     return HttpResponse("<h1>Hello World! Welcome to my Django Site!</h1>")

from django.shortcuts import render, redirect
from .models import MysiteModel
from DjangoFun.forms import MySiteForm

# Create a function
def mysite_view(request):

    content = MysiteModel.objects.all()
    context = {
        'content': content
    }
    return render(request, "index.html", context=context)

# Function for forms
def mysite_form(request):
    if request.method == 'POST':
        form = MySiteForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("mysite_view")
        
        else:
            # Uncomment below line to see errors (if any)
            # print(form.errors)
            return redirect(mysite_form)

    else:
        context = {}
        context['form'] = MySiteForm
        return render(request, "form.html", context=context)