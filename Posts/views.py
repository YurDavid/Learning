from django.shortcuts import render

# Create your views here.
def home_page(request):
    template = "index.html"
    context = {}
    return render(request, template, context)
