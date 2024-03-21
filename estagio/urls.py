from django.urls import path

from estagio.views import EstagioView

urlpatterns = [
    # importa as urls do app 'admin'
    path("estagio/", EstagioView.as_view(), name="estagio"),
]
