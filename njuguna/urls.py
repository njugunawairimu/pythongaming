from django.urls import path
from . import views
app_name = 'njuguna'
urlpatterns =[
    path('',views.MemberListView.as_view(), name='index'),

    path('add_member', views.MemberCreateView.as_view(),
         name='add_member'),
    path('<int:pk>/update', views.MemberUpdateView.as_view(),
         name='update-member'),
    path('<int:pk>/delete',views.MemberDeleteView.as_view(),
         name='member_delete'),
]