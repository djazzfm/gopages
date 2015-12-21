from django.conf.urls import url


urlpatterns = [
    url(r'^(?P<name>\w+)\.html$', 'gopages.views.page', name='page'),

], 'gopages', 'gopages'
