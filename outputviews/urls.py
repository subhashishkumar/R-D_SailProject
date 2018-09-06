from outputviews import views
from django.urls import path

urlpatterns = [
    path('showtables/home', views.showtables, name='ShowTables'),
    path('showtables/manhours/', views.ManhoursFilteredView.as_view(), name='ManhoursTableView'),
    path('showtables/accd_table_detailed/', views.year_wise_detailed, name='AccdTableDetailView'),
    path('showtables/filter_accd_table/', views.AllFilteredView.as_view(), name='FilterAccdTableView'),
    path('showtables/accdtype/<slug:accdType>/', views.get_data_view, name='FatalDataView'),
    path('showtables/accdtype/<slug:accdType>/', views.get_data_view, name='FirstAidDataView'),
    path('showtables/accdtype/<slug:accdType>/', views.get_data_view, name='ReportableDataView'),
    path('showtables/accdtype/<slug:accdType>/', views.get_data_view, name='NonReportableDataView'),
]
