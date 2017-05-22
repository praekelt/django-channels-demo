from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def article_list(request):
    return render(request, 'demo/article_list.html')


