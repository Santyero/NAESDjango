from django.urls import path

from estudante.views import EstudanteView

urlpatterns = [
    # importa as urls do app 'admin'
    path("estudante/", EstudanteView.as_view(), name="estudante"),
]
