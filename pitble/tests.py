from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client


class PitbleTestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def test_get_200(self):
        # index view
        index_url = reverse('index')
        index_res = self.client.get(index_url)
        self.assertEqual(index_res.status_code, 200)

        # sign in view
        sign_in_url = reverse('sign_in')
        sign_in_res = self.client.get(sign_in_url)
        self.assertEqual(sign_in_res.status_code, 200)

        # sign up view
        sign_up_url = reverse('sign_up')
        sign_up_res = self.client.get(sign_up_url)
        self.assertEqual(sign_up_res.status_code, 200)

        # followers view
        followers_url = reverse('followers')
        followers_res = self.client.get(followers_url)
        self.assertEqual(followers_res.status_code, 302)
