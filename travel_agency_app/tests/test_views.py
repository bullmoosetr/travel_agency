from rest_framework.test import APIRequestFactory

factory = APIRequestFactory()
request = factory.post('/destinations/', {'destination_name': 'new idea'}, format='json')
