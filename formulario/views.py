from django.shortcuts import render

def post_list(request):
    return render(request, 'formulario/post_list.html', {})
