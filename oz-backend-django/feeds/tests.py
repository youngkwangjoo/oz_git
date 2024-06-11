from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Feed
from users.models import User
from rest_framework_simplejwt.tokens import RefreshToken


class FeedAPITestCase(APITestCase):
    # 각 테스트 메서드가 실행되기 전에 호출
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")
        refresh = RefreshToken.for_user(self.user)
        self.token = str(refresh.access_token)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")

        self.feed1 = Feed.objects.create(user=self.user, title="Title 1")
        self.feed1 = Feed.objects.create(user=self.user, title="Title 2")

    def test_get_all_feeds(self):
        url = reverse("all_feeds")
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 2)

    def test_get_feed_detail(self):
        url = reverse("feed_detail", kwargs={"feed_id": 1})
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data["content"], self.feed1.content)

    def test_create_feed(self):
        self.client.login(username="testuser", password="password")

        url = reverse("all_feeds")
        data = {"title": "New Title", "content": "New Feed"}
        res = self.client.post(url, data)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(
            Feed.objects.count(), 3
        )  # 전체 게시글의 갯수는 3개여야 합니다.
        self.assertEqual(Feed.objects.latest("id").content, "New Feed")