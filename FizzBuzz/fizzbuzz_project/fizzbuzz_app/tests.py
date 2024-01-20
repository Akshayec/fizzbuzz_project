from django.test import TestCase
from django.urls import reverse
from .views import statistics, update_statistics

class FizzBuzzTests(TestCase):
    def test_fizz_buzz_endpoint_default_params(self):
        response = self.client.get(reverse('fizz_buzz'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [
            '1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz',
            '11', 'fizz', '13', '14', 'fizzbuzz', '16', '17', 'fizz', '19', 'buzz'
        ])

    def test_fizz_buzz_endpoint_custom_params(self):
        params = {'int1': 2, 'int2': 3, 'limit': 10, 'str1': 'foo', 'str2': 'bar'}
        response = self.client.get(reverse('fizz_buzz'), params)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [
            '1', 'foo', 'bar', 'foo', '5', 'foobar', '7', 'foo', 'bar', 'foo'
        ])

    def test_statistics_endpoint(self):
        # Make requests to update statistics
        self.client.get(reverse('fizz_buzz'))
        self.client.get(reverse('fizz_buzz'), {'int1': 3, 'int2': 5, 'limit': 15, 'str1': 'fizz', 'str2': 'buzz'})
        self.client.get(reverse('get_statistics'))

        response = self.client.get(reverse('get_statistics'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            'most_used_request': reverse('fizz_buzz'),
            'hits': 2
        })

    def test_index_page(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<h1>Fizz-Buzz App</h1>', html=True)
        self.assertContains(response, '<strong>Welcome to the Fizz-Buzz app!</strong>', html=True)
        self.assertContains(response, '<a href="{}" class="button">Fizz-Buzz</a>'.format(reverse('fizz_buzz')), html=True)
        self.assertContains(response, '<a href="{}" class="button">Statistics</a>'.format(reverse('get_statistics')), html=True)
