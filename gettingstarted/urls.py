from django.conf.urls import include, url
from django.urls import path

from django.contrib import admin
admin.autodiscover()

import hello.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^scheduled/', hello.views.scheduled, name='scheduled'),
    url(r'^statistics/', hello.views.statistics, name='statistics'),
    path('admin/', admin.site.urls),
    path('tip/<int:pk>/', hello.views.tip, name='tip'),

]




#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [path('accounts/', include('django.contrib.auth.urls')),]
