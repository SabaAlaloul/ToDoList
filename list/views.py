from django.shortcuts import render
from .models import *
from django.urls import reverse
# Create your views here.
from django.views.generic import (
ListView,
CreateView,
UpdateView,
)

class ListListView(ListView):
    model= To_DO_List
    queryset = To_DO_List.objects.all()
    template_name = "listing.html"

class ItemListView(ListView):
    model = List
    template_name = "list/todo_list.html"
    def get_queryset(self):
        return List.objects.filter( To_DoList=self.kwargs["list_id"])
    def get_context_data(self):
        context = super().get_context_data()
        context[" To_DoList"] =  To_DO_List.objects.get(id=self.kwargs["list_id"])
        return context

class ListCreate(CreateView):
    model = To_DO_List
    fields = ["name"]
    def get_context_data(self):
        context = super(ListCreate, self).get_context_data()
        context["title"] = "Add a new list"
        return context        


class ItemCreate(CreateView):
    model = List
    fields = [
    "To_DoList",
    "title",
    "description",
    "due_date",
    ]
    def get_initial(self):
        initial_data = super(ItemCreate, self).get_initial()
        todo_list =  To_DO_List.objects.get(id=self.kwargs["list_id"])
        initial_data["To_DoList"] = To_DoList
        return initial_data
    def get_context_data(self):
        context = super(ItemCreate, self).get_context_data()
        todo_list = To_DO_List.objects.get(id=self.kwargs["list_id"])
        context["To_DoList"] = To_DoList
        context["title"] = "Create a new item"
        return context

        def get_success_url(self):
            return reverse("list", args=[self.object.todo_list_id])         


class ItemUpdate(UpdateView):
    model = List
    fields = [
    "To_DoList",
    "title",
    "description",
    "due_date",
    ]

    def get_context_data(self):
        context = super(ItemUpdate, self).get_context_data()
        context["todo_list"] = self.object.todo_list
        context["title"] = "Edit item"
        return context
    def get_success_url(self):
        return reverse("list", args=[self.object.todo_list_id])