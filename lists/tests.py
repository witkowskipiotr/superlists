from django.template.loader import render_to_string
from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page


class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertIn('A new list item', response.content.decode())
        #expected_html = render_to_string(
        #    'home.html',
        #    {'new_item_text': 'New item list'}
        #)
        #self.assertEqual(response.content.decode(), expected_html)
        self.assertTemplateUsed(response, 'home.html')

    # def test_root_url_resolves_to_home_page_view(self):
    #     found = resolve('/')
    #     self.assertEqual(found.func, home_page)
    #
    # def test_home_page_returns_correct_html(self):
    #     # request = HttpRequest()
    #     # response = home_page(request)
    #
    #     response = self.client.get('/')
    #     html = response.content.decode('utf-8')
    #     # expected_html = render_to_string('home.html')
    #     # self.assertEqual(html, expected_html)
    #
    #
    #     self.assertTrue(html.startswith('<html>'))
    #     self.assertIn('<title>To-Do lists</title>', html)
    #     self.assertTrue(html.strip().endswith('</html>'))
    #
    #     self.assertTemplateUsed(response, 'home.html')
