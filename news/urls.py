from django.urls import path

from . import views
from . import api

urlpatterns = [
    path('', views.index, name='index'),
    path('api/getInfo', api.getInfo),
    path('api/reg', api.reg),
    path('api/login', api.login),
    path('api/docList', api.docList),
    path('api/updateDoc', api.updateDoc),
    path('api/setInfo', api.setInfo),
    path('api/hendleGet', api.hendleGet),
    path('api/runList', api.runList),
    path('api/logout', api.logout),
]