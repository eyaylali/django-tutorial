from django.shortcuts import render

def post_list(request):

    return render(request, 'first_project/post_list.html', {})