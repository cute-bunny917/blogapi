# posts/tests.py
# A test case is the individual unit of testing. It checks for a specific response to a particular set of inputs.
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post

# We want to ensure a logged-in user can create a blog post with a title and body


class BlogTests(TestCase):
    """
    @classmethod means: when this method is called, we pass the class 
    as the first argument instead of the instance of that class (as we normally do with methods).
    This means you can use the class and its properties inside that method rather than a particular instance.

    self vs cls. The difference between the keywords self and cls reside only in the method type. 
    If the created method is an instance method then the reserved word self has to be used,
    but if the method is a class method then the keyword cls must be used.
    """
    @classmethod
    def setUpTestData(cls):
        # Create a user
        testuser1 = User.objects.create_user(
            username='testuser1', password='abc123')
        testuser1.save()
        # Create a blog post
        test_post = Post.objects.create(
            author=testuser1, title='Blog title', body='Body content...')
        test_post.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'
        self.assertEqual(author, 'testuser1')
        self.assertEqual(title, 'Blog title')
        self.assertEqual(body, 'Body content...')
