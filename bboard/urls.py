from django.urls import path

from .views import index, by_rubric, BbCreateView

urlpatterns = [
    path('create/', BbCreateView.as_view(), name='create'),
    path('<int:rubric_id>/', by_rubric, name='by-rubric'),
    path('', index, name='index'),
]