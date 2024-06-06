
from django.contrib.auth.password_validation import validate_password
from rest_framework.exceptions import ParseError, NotFound
from rest_framework.views import APIView
from .serializers import MyInfoUserSerializer
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication #사용자 인증
from rest_framework.permissions import IsAuthenticated #인증된유저만 볼수 있는 페이지

class Users(APIView):
    # 유저 생성 
    def post(self, request):
        password = request.data.get("password")
        serializer = MyInfoUserSerializer(data=request.data)
        
        try:
            validate_password(password) # 비밀번호 validation
        except:
            raise ParseError("Invalid password") # 오류가 났을 때 유저에게 공유

        if serializer.is_valid():#시리얼라이즈가 유효하면
            user = serializer.save() # 새로운 유저 생성
            user.set_password(password) # 비밀번호 업데이트
            user.save() # 데이터 업데이트 후 저장

            serializer = MyInfoUserSerializer(user)
            return Response(serializer.data)
        else:
            raise ParseError(serializer.errors)
        
class MyInfo(APIView):
    # read
    authentication_classes = [TokenAuthentication] # 추가
    permission_classes = [IsAuthenticated] # 추가
    

    def get(self, request):
        user = request.user
        serializer = MyInfoUserSerializer(user)
        return Response(serializer.data)

    # update
    def put(self, request):
        user = request.user
        serializer = MyInfoUserSerializer(user, data=request.data, partial=True)

        if serializer.is_valid():
            user = serializer.save()
            serializer = MyInfoUserSerializer(user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)