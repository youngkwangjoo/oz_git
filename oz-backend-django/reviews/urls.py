from django.urls import path
from . import views

urlpatterns = [
    path("", views.Reviews.as_view(), name="reviews"),
    path("<int:review_id>", views.ReviewDetail.as_view(), name="review_detail"),
]