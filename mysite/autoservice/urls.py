from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('cars/', views.cars, name="cars"),
    path('cars/<int:pk>/', views.car, name="car"),
    path('orders/', views.OrderListView.as_view(), name="orders"),
    path('orders/<int:pk>/', views.OrderDetailView.as_view(), name="order"),
    path("search/", views.search, name="search"),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path("profile/", views.profile, name="profile"),
    path('userorders/', views.UserOrderListView.as_view(), name="user_orders"),
    path('userorders/create/', views.UserOrderCreateView.as_view(), name="user_orders_create"),
    path('userorders/<int:pk>/update/', views.UserOrderUpdateView.as_view(), name="user_orders_update"),
    path('userorders/<int:pk>/delete/', views.UserOrderDeleteView.as_view(), name="user_orders_delete"),
    path('userorders/<int:pk>/linecreate/', views.UserOrderLineCreateView.as_view(), name="user_orderline_create"),
    path('orderlines/<int:pk>/update/', views.UserOrderLineUpdateView.as_view(), name="user_orderline_update"),
    path('orderlines/<int:pk>/delete/', views.UserOrderLineDeleteView.as_view(), name="user_orderline_delete"),
]
