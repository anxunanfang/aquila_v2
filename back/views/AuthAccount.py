from django.shortcuts import redirect
from model_model import models
from django.db.models import Q
from django.db import connection


def AuthAccount(func):
    def inner(request, *args, **kwargs):
        username = request.session.get('username', None)
        ret = models.UserInfo.objects.filter(Q(user_name=username) | Q(email=username)).count()
        if not username and not ret:
            return redirect('/back/login.html')
        return func(request, *args, **kwargs)
    return inner


def GetUserInfo(request):
    '''
    get user privileges, group privileges
    '''
    username = request.session.get('username', None)
    user_info = models.UserInfo.objects.filter(Q(user_name=username) |
                                               Q(email=username)).all().select_related('role', 'user_group')
    return user_info