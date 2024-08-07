from . import views
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

#menu_itens
urlpatterns = [
    #path('ratings/', views.RatingsView.as_view(), name='ratings'),
    path('menu-item/',views.menu_itens),
    path('menu-item/<int:id>',views.single_item),
    path('secret/',views.secret),
    path('api-token-auth/',obtain_auth_token),
    path('manage-view/',views.manage_view),
    path('throttle-check/',views.throttle_check),
    path('throttle-check-auth/',views.throttle_check_auth),
    
]
