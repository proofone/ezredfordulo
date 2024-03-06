from django.shortcuts import render
from django.views.generic import ListView, DetailView
from palyazat.models import Kiiras


class KiirasListView(ListView):
    model = Kiiras
    template_name = "palyazat/list.html"


class KiirasDetailView(DetailView):
    model = Kiiras
    template_name = "palyazat/palyazat_detail.html"
