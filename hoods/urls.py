from django.conf.urls import url
from .views import *

urlpatterns = [
    url('^$', home, name='home'),