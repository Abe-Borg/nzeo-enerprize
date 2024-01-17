from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required
def overall_map(request, *args, **kwargs):
    return render(request, 'overall_map.html')