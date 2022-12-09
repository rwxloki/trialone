from urllib import response
from django.test import SimpleTestCase#this is said to be so small case
from django.test import TestCase #added this
from polls.models import Mymod, BlogMod #connect to models
from django.urls import reverse #connect to urls
from django.contrib.auth import get_user_model



class SimpleTests(TestCase):
    def test_myhome_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        #tests if home page exists

    def test_myabout_page(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
        #tests if about page exists


class PollsModelTest(TestCase):
    def setUp(self):
        Mymod.objects.create(text = 'trial test case')
        #creates a model instance

    def test_text_content(self):
        mypost = Mymod.objects.get(id=1)
        expected_obj_name = f'{mypost.text}'
        self.assertEqual(expected_obj_name, 'trial test case')
        #test if conent is inserted


class HomePageViewTest(TestCase):
    def setUp(self):
        Mymod.objects.create(text = 'this is another test')
    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code,200)
    def test_view_url_by_name(self):
        resp = self.client.get(reverse('myhome'))
        self.assertEqual(resp.status_code,200)
    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('myhome'))
        self.assertEqual(resp.status_code,200)
        self.assertTemplateUsed(resp, 'home.html')
        

class BlogTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='myuser',
            email='my@email.com',
            password='secret',
        )
        self.my_object = BlogMod.objects.create(
            title='me',
            body='mybodycontent',
            author=self.user,
        )

    def test_string_representation(self):
        mykpost = BlogMod(title='simple title')
        self.assertEqual(str(mykpost), mykpost.title)

    def test_get_absolute_url(self):
        self.assertEqual(self.my_object.get_absolute_url(), '/anyname/1/')
        #added this during edit blog stage

    def test_blog_content(self):
        self.assertEqual(f'{self.my_object.title}','me')
        self.assertEqual(f'{self.my_object.author}','myuser')
        self.assertEqual(f'{self.my_object.body}','mybodycontent')

    def test_blog_list_view(self):
        response = self.client.get(reverse('myblog'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,'mybodycontent')
        self.assertTemplateUsed((response,'blog.html'))

    def test_log_detail_view(self):
        response = self.client.get('/anyname/1/')
        no_response = self.client.get('/anyname/100000/')
        self.assertEqual(response.status_code,200)
        self.assertEqual(no_response.status_code,404)
        self.assertContains(response,'me')
        self.assertTemplateUsed(response,'detail.html')

    def test_blog_create_view(self):
        response = self.client.post(reverse('mynew'), {
            'title': 'New title',
            'body': 'New text',
            'author': self.user,
        } )       
        self.assertEqual(response.status_code,200)
        self.assertContains(response,'New title')
        self.assertContains(response,'New text')        
   
    def test_blog_update_view(self):
        response = self.client.post(reverse('myedit', args='1'), {
            'title': 'Updated title',
            'body': 'Updated text',            
        } )       
        self.assertEqual(response.status_code,302)

    def test_blog_delete_view(self):
        response = self.client.get(reverse('mydelete', args='1'))               
        self.assertEqual(response.status_code,200)
 



