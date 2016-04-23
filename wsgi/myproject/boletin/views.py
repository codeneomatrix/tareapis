from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.generic import CreateView,TemplateView,ListView,FormView,UpdateView, DeleteView

def inicio(TemplateView):
    template_name = 'index.html'
