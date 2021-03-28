from django.urls import path
from programmes import views

urlpatterns = [
    path('', views.programme, name='programmes'),
    path('build_muscle/', views.build_muscle, name='build_muscle'),
    path('get_lean/', views.get_lean, name='get_lean'),
    path('lose_weight/', views.lose_weight, name='lose_weight'),
    path('membership/', views.membership, name='membership'),
]
