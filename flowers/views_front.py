from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import flowers


class flowersListView(LoginRequiredMixin, ListView):
    template_name = "flowers/flowers_list.html"
    model = flowers
    context_object_name = "flower"


class flowersDetailView(LoginRequiredMixin, DetailView):
    template_name = "flowers/flowers_detail.html"
    model = flowers


class flowersUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "flowers/flowers_update.html"
    model = flowers
    fields = "__all__"


class flowersCreateView(LoginRequiredMixin, CreateView):
    template_name = "flowers/flowers_create.html"
    model = flowers
    fields = ["name", "rating", "reviewer"] # "__all__" for all of them


class flowersDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "flowers/flowers_delete.html"
    model = flowers
    success_url = reverse_lazy("flowers_list")
