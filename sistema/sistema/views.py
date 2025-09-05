# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render

class Login(View):
    """
    Class Based View para autenticação de usuário.
    """

    def get(self, request):
        contexto = {}
        return render( request, 'autenticacao.html', contexto)