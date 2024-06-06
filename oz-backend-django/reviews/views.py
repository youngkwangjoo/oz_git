from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, NotAuthenticated
from .models import Review
from .serializers import ReviewSerializer

# GET: 전체 리뷰 데이터 가져오기
class Reviews(APIView):
    def get(self, request):
        reviews = Review.objects.all() # 장고 객체
        # (Serializer) 장고 객체 -> JSON
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

# GET: 특정 리뷰 데이터 가져오기
class ReviewDetail(APIView):
    def get(self, request, review_id):
        try:
            review = Review.objects.get(id=review_id)
        except Review.DoesNotExist:
            raise NotFound

        serializer = ReviewSerializer(review)
        return Response(serializer.data)