from django.urls import path
from .views import ItemListCreate, ItemUpdateView, TaskDeleteAPIView

urlpatterns = [
    path('items/', ItemListCreate.as_view(), name='item-list-create'),
    path('items/<int:pk>/', ItemUpdateView.as_view(), name='status-update'),
    path('items/<int:id>/delete/', TaskDeleteAPIView.as_view(), name='task-delete'),
]
