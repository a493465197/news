import os
from pathlib import Path
from django.urls import path,re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from . import api
BASE_DIR = Path(__file__).resolve().parent.parent

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
    path('api/userList', api.userList),
    path('api/delUser', api.delUser),
    path('api/delDoc', api.delDoc),
    path('api/addTag', api.addTag),
]


# urlpatterns += static('/static', document_root=os.path.join(BASE_DIR, 'static'))