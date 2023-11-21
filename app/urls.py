from django.urls import path
from .views import index

urlpatterns = [
    path("", index),

    # path("/<int:pk>/", portfolio_single_view)
]
