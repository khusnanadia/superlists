#from django.conf.urls import include, url
#from django.contrib import admin

from django.conf.urls import url
from lists import views

urlpatterns = [
	# Examples:
	# url(r'^$', 'superlists.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),

	url(r'^$', views.home_page, name='home'),
	url(r'^lists/new$', views.new_list, name='new_list'),
	url(r'^lists/the-only-list-in-the-world/$', views.view_list, name='view_list')
	# url(r'^admin/', include(admin.site.urls)),
]
