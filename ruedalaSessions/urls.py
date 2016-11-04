from django.conf.urls import url, patterns
from ruedalaSessions.views import *

urlpatterns = patterns(
    '',
    url(
        r'^password/reset/$',
        'ruedalaSessions.views.password_reset',
        {
            'post_reset_redirect': 'password_reset_done',
            'template_name': 'registrations/password_reset_form.html',
            'email_template_name': 'registrations/password_reset_email.html',
            'html_email_template_name': 'registrations/html_password_reset_email.html',
        },
        name="password_reset"
    ),
    url(
        r'^password/reset/done/$',
        'django.contrib.auth.views.password_reset_done',
        {
            'template_name': 'registrations/password_reset_done.html'
        },
        name="password_reset_done"
    ),
    url(
        r'^password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        'django.contrib.auth.views.password_reset_confirm',
        {
            'post_reset_redirect': 'password_done',
            'template_name': 'registrations/password_reset_confirm.html'
        },
        name="password_reset_confirm"
    ),
    url(
        r'^password/done/$',
        'django.contrib.auth.views.password_reset_complete',
        {
            'template_name': 'registrations/password_reset_complete.html'

        },
        name='password_done'
    ),
    url(r'index/$',
        Index.as_view(),
        name='index'),
    url(r'^$',
        'ruedalaSessions.views.login_request',
        name='login'),
    url(
        r'^accounts/confirm/(?P<activation_key>\w+)/(?P<pk>\d+)/$',
        ActivateAccount.as_view(),
        name='register_confirm'),
    url(
        r'^accounts/generateKey/(?P<pk>\d+)/$',
        'ruedalaSessions.views.generate_key',
        name='generate_key'),
    url(
        r'^register/$',
        'ruedalaSessions.views.user_registration',
        name='register'),
    url(
        r'^logout/$',
        'django.contrib.auth.views.logout',
        {
            'next_page': '/'
        },
        name='logout'),
    url(
        r'^editProfile/(?P<pk>\d+)$',
        EditPassword.as_view(),
        name='edit-profile'),
)
