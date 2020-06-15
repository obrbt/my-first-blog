from django.shortcuts import render
import os

# Create your views here.
def post_list(request):
    #return render(request, os.getcwd() + '\\blog\\templetes\\blog\\post_list.html', {})
    return render(request, 'blog/post_list.html', {})
