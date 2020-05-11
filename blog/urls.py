from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns=[
    path('',views.blog_request_view,name='blog'),
    path('<int:id>/details',views.blog_request_details,name='details'),
    path('create/',views.create_blog_request,name="create"),
    path('<int:id>/delete',views.delete_post_handler,name="delete")
 
]+staticfiles_urlpatterns()