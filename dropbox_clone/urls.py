from django.conf import settings
from django.conf.urls import patterns, include, url

from django.contrib import admin
from tastypie.api import Api
from dropbox.api.resources import MediaResource, UserResource

admin.autodiscover()

#can create multiple versions for versioning ability
v1_api = Api(api_name="v1")
v1_api.register(UserResource())
v1_api.register(MediaResource())


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'dropbox.views.home', name='home'),
    # url(r'^blog/', include ('blog.urls')),
    url(r'^check_login/$', 'dropbox.views.check_login', name='check_login'),
    url(r'^profile/$', 'dropbox.views.profile', name='profile'),
    url(r'^profile/(?P<user_id>\w+)/update/$', 'dropbox.views.profile_update', name='profile_update'),



    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),
    url(r'api/doc/',
        include('tastypie_swagger.urls', namespace='tastypie_swagger'),
        kwargs={"tastypie_api_module": "v1_api",
                "namespace": "tastypie_swagger"}
        ),


    url(r'^register/$', 'dropbox.views.register', name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),




    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    # Support old style base36 password reset links; remove in Django 1.7
    url(r'^reset/(?P<uidb36>[0-9A-Za-z]{1,13})-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm_uidb36'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm',
        name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),





)


if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
)