from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path("" , views.index , name = "index"),
    path("login" , views.login_view, name = "login"),
    path("login_patient" , views.login_patient , name = "login_patient"),
    path("logout" , views.logout_view , name = "logout"),
    path("patient_register" , views.patient_register , name = "patient_register"),
    path("login_doctor" , views.login_doctor , name = "login_doctor"),
    path("doctor_register" , views.doctor_register , name = "doctor_register"),
    path("liked" , views.liked , name = "liked"),
    path("like" , views.like , name = "like"),
    path("added" , views.added , name = "added"),
    path("add" , views.add , name = "add"),
    path("profile/<str:status>/<int:id>" , views.profile , name = "profile"),
    path("my_doctors" , views.my_doctors , name = "my_doctors"),
    path("add_photo/<str:status>" , views.add_photo , name = "add_photo"),
    path("add_advice" , views.add_advice , name = "add_advice"),
    path("pending" , views.pending , name = "pending" ),
    path("confirm" , views.confirm  , name = "confirm"),
    path("advices" , views.advices , name = "advices"),
    path("massage" , views.massaging , name = "massage"),
    path("remove" , views.remove , name = "remove")
]

urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)