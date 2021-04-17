from django.urls import reverse
from rest_framework.test import APITestCase
from django.utils import timezone

from .models import NewsModel
from .serializers import NewsModelSerializers
from rest_framework import status
import json


class NewsSerializersAPITestCase(APITestCase):
    def test_serializer(self):
        news_1 = NewsModel.objects.create(title="news1", content="any text", publish_date='2021-02-11 00:00:00')
        news_2 = NewsModel.objects.create(title="news2", content="some text", publish_date='2021-03-20 00:00:00')
        data = NewsModelSerializers([news_1, news_2], many=True).data
        expected_data = [
            {
                "id": news_1.id,
                "title" : "news1",
                "content": "any text",
                "publish_date": "2021-02-11 00:00:00"
            },
             {
                "id": news_2.id,
                "title" : "news2",
                "content": "some text",
                "publish_date": "2021-03-20 00:00:00"
            }
        ]
        self.assertEqual(expected_data, data)


class NewsAPITestCase(APITestCase):
    def setUp(self):
        self.news_1 = NewsModel.objects.create(title="news1", content="any text", publish_date=timezone.now())
        self.news_2 = NewsModel.objects.create(title="news2", content="some text", publish_date=timezone.now())
        self.url = reverse('newsmodel-list')

    def test_get(self):
        response = self.client.get(self.url)
        serializer_data = NewsModelSerializers([self.news_1, self.news_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_create(self):
        self.assertEqual(2, NewsModel.objects.all().count())
        data = {
            "title": "Test_create",
            "content": "Any create content",
            "publish_date": "2021-03-20 00:00:00"
        }
        json_data = json.dumps(data)
        response = self.client.post(self.url, data=json_data, content_type="application/json")
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(3, NewsModel.objects.all().count())

    def test_update(self):
        data = {
            "title": self.news_1.title,
            "content": "Any update content",
            "publish_date": "2021-04-07T19:56:33Z"
        }
        path = reverse('newsmodel-detail', args=(self.news_1.id,))
        json_data = json.dumps(data)
        response = self.client.put(path, data=json_data, content_type="application/json")
        self.news_1.refresh_from_db()
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual("Any update content", self.news_1.content)

    def test_patch(self):
        data = {
            "content": "Any update content",
        }
        path = reverse('newsmodel-detail', args=(self.news_1.id,))
        json_data = json.dumps(data)
        response = self.client.patch(path, data=json_data, content_type="application/json")
        self.news_1.refresh_from_db()
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual("Any update content", self.news_1.content)

    def test_delete(self):
        new3 = NewsModel.objects.create(title="news3", content="some text", publish_date=timezone.now())
        path = reverse('newsmodel-detail', kwargs={'pk':new3.id})
        response = self.client.delete(path)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_detail_item(self):
        path = reverse('newsmodel-detail', args=(self.news_1.id,))
        response = self.client.get(path, content_type="application/json")
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        serializer_data = NewsModelSerializers(self.news_1).data
        self.assertEqual(serializer_data, response.data)
       



