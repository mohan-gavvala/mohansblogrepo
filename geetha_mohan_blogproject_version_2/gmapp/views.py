from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request,'about.html')
def blog_post(request):
    return render(request,'blog-post.html')
def index(request):
    return render(request,'index.html')
def contact(request):
    return render(request,'contact.html')
