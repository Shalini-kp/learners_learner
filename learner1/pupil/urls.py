from django.conf.urls import url
from . import views

#urls configuration

urlpatterns = [
	url(r'^$',views.index,name="index"),
]