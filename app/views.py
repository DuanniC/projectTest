from .models import *
from rest_framework import viewsets
from django.shortcuts import render
from .serializers import ProdutoSerializers
from django.core import paginator
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = product.objects.all()
    serializer_class = ProdutoSerializers


def home(request, template_name="home.html"):
    query = request.GET.get("busca", '')
    ordenar = request.GET.get("ordenar", '')
    page = request.GET.get('page', '')
    if query:
        produto = product.objects.filter(name__icontains=query)
    else:
        try:
            if ordenar:
                produto = product.objects.all().order_by(ordenar)
            else:
                produto = product.objects.all()
            produto = Paginator(produto, 8)
            produto = produto.page(page)
        except PageNotAnInteger:
            produto = produto.page(1)
        except EmptyPage:
            produto = paginator.page(paginator.num_pages)
    produtos = {'lista': produto}
    return render(request, template_name, produtos)


def contact(request):
    return render(request, 'contact.html')


def login(request):
    return render(request, 'login.html')


def forgotLogin(request):
    return render(request, 'forgotLogin.html')
