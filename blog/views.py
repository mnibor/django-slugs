from typing import Any
from django.db import models
from django.db.models.query import QuerySet
from django.views.generic import ListView, DetailView
from .models import Post
from django.shortcuts import render
from django.http import Http404

class HomeView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(author__isnull=False, category__isnull=False)

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset=queryset)
        except self.model.DoesNotExist:
            raise Http404("El post no existe.")

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Http404:
            return render(request, 'blog/error_404.html', status=404)
