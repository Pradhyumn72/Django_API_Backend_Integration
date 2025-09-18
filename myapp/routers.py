from rest_framework import routers
from myapp.views import StudentViewSet
# router = routers.SimpleRouter()
#  default router is used to combine url of stu_list and stu_detail...single url 
router = routers.DefaultRouter()
router.register(r'Student', StudentViewSet)
urlpatterns = router.urls