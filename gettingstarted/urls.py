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
    url(r'^addnew/', hello.views.addnew, name='addnew'),
    path('admin/', admin.site.urls),
    path('shift/<int:pk>/', hello.views.shift, name='shift'),
    

]




#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [path('accounts/', include('django.contrib.auth.urls')),]
