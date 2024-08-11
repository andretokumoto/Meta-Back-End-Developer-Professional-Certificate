from . import views
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

#rotas
urlpatterns = [
    path('menu-item/',views.menu_itens),
    path('menu-item/<int:id>',views.single_item),
    path('throttle-check/',views.throttle_check),
    path('throttle-check-auth/',views.throttle_check_auth),
    path('groups/managers/users',views.managers),
    path('category/',views.category_ctl),
    path('category/<int:id>',views.category_ctl),
    path('groups/delivery-crew/users',views.delivery_crew),
    path('groups/delivery-crew/users/<int:id>',views.delivery_crew),
    path('register',views.user_register),
    path('token/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('item-of-day',views.ItemOfDay),
]
