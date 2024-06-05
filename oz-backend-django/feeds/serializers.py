from rest_framework.serializers import ModelSerializer
from .models import Feed

# (1) 전체 데이터를 다 보여주는 Serialize
class FeedSerializer(ModelSerializer):
    class Meta:
        model = Feed
        fields = "__all__"
					# 현재의 모델과 연결된 모델들까지 serialize 시키겠다는 뜻        
					# Feed - User 모델 => 현재 코드는 Feed 모델 객체를 직렬화 하고 있지만,
					# depth = 1 이라는 코드를 통해 User 객체도 직렬화하겠다는 뜻.
        depth = 1 # objects도 serialize화 시킴
# class FeedListSerializer(ModelSerializer):
#     class Meta:
#         model = Feed
#         fields = ("id", "user", "title", "content")\



