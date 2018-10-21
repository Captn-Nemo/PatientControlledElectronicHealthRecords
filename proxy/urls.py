from django.conf.urls import url, include
from rest_framework import routers
from data_office import views

router = routers.DefaultRouter()
router.register(r'patients', views.PatientViewSet)
router.register(r'data_sets', views.DataSetViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]