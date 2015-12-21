from django.shortcuts import render
from django.template import TemplateDoesNotExist
from django.http import Http404


def page(request, name):
    try:
        return render(request, "gopages/%s.html" % name)
    except TemplateDoesNotExist:
        raise Http404("Page does not exists.")
