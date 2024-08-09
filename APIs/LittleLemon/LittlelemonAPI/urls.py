from . import views
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

#rotas
urlpatterns = [
    path('menu-item/',views.menu_itens),
    path('menu-item/<int:id>',views.single_item),
    path('api-token-auth/',obtain_auth_token),
    path('throttle-check/',views.throttle_check),
    path('throttle-check-auth/',views.throttle_check_auth),
    path('groups/managers/users',views.managers),
    path('category/',views.category_ctl),
    path('category/<int:id>',views.category_ctl),
    path('groups/delivery-crew/users',views.delivery_crew),
    path('groups/delivery-crew/users/<int:id>',views.delivery_crew),
    path('register',views.user_register),
]
