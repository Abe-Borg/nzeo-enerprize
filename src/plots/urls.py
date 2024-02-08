from django.urls import path
from . import views

urlpatterns = [
    path('line-plot', views.get_line_plot, name='line-plot'),
    path('scatter-plot', views.get_scatter_plot, name='scatter-plot'),
    path('histogram', views.get_histogram, name='histogram'),
    path('bar-plot', views.get_bar_plot, name='bar-plot'),
    path('area-plot', views.get_area_plot, name='area-plot'),
    path('heatmap', views.get_heatmap, name='heatmap'),
]

