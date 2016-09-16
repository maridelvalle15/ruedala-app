# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.defaults import page_not_found

LOGIN_URL = settings.LOGIN_URL


class LoginRequiredMixin(object):
    @method_decorator(login_required(login_url=LOGIN_URL))
    def dispatch(self, request, *args, **kwargs):
        return super(
            LoginRequiredMixin, self).dispatch(request, *args, **kwargs)


class AdminRequiredMixin(object):
    @method_decorator(login_required(login_url=LOGIN_URL))
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            user = request.user
            all_admins = [
                'super_admin'
            ]
            groups = user.groups.filter(name__in=all_admins)

            if not groups:
                return page_not_found(request)

        return super(
            AdminRequiredMixin, self).dispatch(request, *args, **kwargs)


class GroupRequiredMixin(object):
    @method_decorator(login_required(login_url=LOGIN_URL))
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            user = request.user
            all_admins = [
                'super_admin',
                'admin'
            ]
            groups = user.groups.filter(name__in=all_admins)

            if not groups:
                return page_not_found(request)

        return super(
            GroupRequiredMixin, self).dispatch(request, *args, **kwargs)


class CorredorRequiredMixin(object):
    @method_decorator(login_required(login_url=LOGIN_URL))
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            user = request.user
            all_admins = [
                'corredor'
            ]
            groups = user.groups.filter(name__in=all_admins)

            if not groups:
                return page_not_found(request)

        return super(
            CorredorRequiredMixin, self).dispatch(request, *args, **kwargs)


class DetailRequiredMixin(object):
    @method_decorator(login_required(login_url=LOGIN_URL))
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            user = request.user
            all_admins = [
                'corredor',
                'super_admin',
                'admin'
            ]
            groups = user.groups.filter(name__in=all_admins)

            if not groups:
                return page_not_found(request)

        return super(
            DetailRequiredMixin, self).dispatch(request, *args, **kwargs)
