from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.courses),
    path('courses/create', views.create),
    path('courses/destroy/<int:id>', views.destroy),
    path('courses/delete/<int:id>', views.delete),
    
]
