from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('analyze', views.analyze, name='analyze'),
    path('about_us/',views.about_us, name='about_us'),
    path('contect_us/',views.contect_us, name='contect_us'),
    # path('capitalizefirst', views.capfirst, name='capfirst'),
    # path('newlineremover', views.newlineremover, name='newlineremover'),
    # path('spaceremover', views.spaceremover, name='spaceremover'),
    # path('charcount', views.charcount, name='charcount'),
]
