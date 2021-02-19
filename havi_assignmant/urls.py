from django.contrib import admin
from django.urls import path
from usepanel import views as user
from adminpanel import views as admins
urlpatterns = [
    path('admin/', admin.site.urls),
     path('curd_api/', user.curd_api,name='curd_api'),
     path('curd_api/<int:pk>', user.curd_api,name='curd_api'),


    path('signup/', user.home,name='signup'),
    path('image/', user.image,name='image'),
    path('', user.loginuser,name='login'),
    path('show_data/', user.show_data, name='show_data'),
    path('logout/', user.logout, name='logout'),
    path('delete/<int:id>/',user.delete_data,name="deletedata"),
    path('update/<int:id>/',user.update,name="updatedata"),



    path('aminHome',admins.aminHome,name="aminHome"),



]
