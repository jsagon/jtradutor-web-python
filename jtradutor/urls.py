from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'jtradutor.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

	url(r'^$', "app.view.index"),
	url(r'^translate/', "app.view.translate"),
	#url(r'^admin/', include(admin.site.urls)),
]
