from django.conf.urls import url
from lists import views

urlpatterns = [
	url(r'^new$', views.new_list, name='new_list'),
	url(r'^(\d+)/$', views.view_list, name='view_list'),
#	url(r'^(\d+)/add_item$', views.add_item, name='add_item'),
#	url(r'^$', list_views.home_page, name='home'),
#	url(r'^lists/', include(list_urls)),
# 	url(r'^admin/', include(admin.site.urls)),
]

