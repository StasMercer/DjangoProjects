from django.urls import path

from . import views

urlpatterns = [
    path('', views.render_main),
    path('admin_page/', views.render_admin),
    path('add_in_queue/', views.add_in_queue),
    path('logout_user/', views.logout_user),
    path('delete_from_queue/', views.delete_from_queue),
    path('mark_user/', views.mark_user)
]
