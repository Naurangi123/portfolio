from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    #USER LOGIN, LOGOUT,REGIATER PATH
    path('',views.index,name='index'),
    path('home/',views.home,name='home'),
    # path('login/',views.login,name='login'),
    path('register/',views.register_user,name='register'),
    path('logout/',views.logout_user,name='logout'),


    #RECORDS PATH
    path('record/<int:pk>', views.customer_record, name='record'),
    path('add_record/',views.add_record,name='add_record'),
    path('update_record/<int:pk>', views.update_record, name='update_record'),
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),


    #PROJECT PATH
    path('project', views.project, name='project'),
    path('project_detail/<int:pk>', views.project_detail, name='project_detail'),
    path('upload/', views.upload_project, name='upload'),
    path('delete_project/<int:pk>',views.delete_project,name='delete_project'),


    #BMI,GALLERY,VIDEO GALLERY PATH
    path('bmi/', views.bmi_calculeter, name='bmi'),
    path('gallery/', views.gallery, name='gallery'),
    path('gallery_one/<int:pk>', views.gallery_one, name='gallery_one'),
    path('delete_gallery/<int:pk>',views.delete_gallery,name='delete_gallery'),
    path('video/', views.video_gallery, name='video'),
    path('video_one/<int:pk>', views.video_gallery_one, name='video_one'),

    # Weather Data
    path('weather/',views.weather,name='weather'),


    path('error/', views.error, name='error'),


]

urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)