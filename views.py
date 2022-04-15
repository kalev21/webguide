from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import FolderForm


def index(request):
    return render(request, 'guide/index.html')


class CreateFolderView(CreateView):
    form_class = FolderForm
    template_name = 'guide/create.html'
    success_url = reverse_lazy('guide/index.html')
    context_object_name = 'folders'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)  # Важная строка кода (иначе все потеряется)
        return context


