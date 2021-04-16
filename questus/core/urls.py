from rest_framework import routers
from . import viewsets
router = routers.DefaultRouter()
router.register('leaf', viewsets.QuestLeafViewSet)
router.register('param', viewsets.ParamViewSet)
router.register('param-set', viewsets.ParamsSetViewSet)

urlpatterns = [

]

urlpatterns += router.urls