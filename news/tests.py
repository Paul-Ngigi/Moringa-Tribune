from django.test import TestCase
from .models import Editor, Tags, Article
import datetime as dt


# Create your tests here.
class EditorTestClass(TestCase):
    # Set up method
    def setUp(self) -> None:
        self.new_editor = Editor(first_name='Paul', last_name='Ngigi', email='paulkush7777@gmail.com')

    def tearDown(self) -> None:
        Editor.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_editor, Editor))

    def test_save_editor(self):
        self.new_editor.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)

    def test_delete_editor(self):
        editors = Editor.objects.all()
        self.new_editor.save_editor()
        self.new_editor.delete_editor()
        self.assertTrue(len(editors) < 1)

    def test_display_all(self):
        self.new_editor.save_editor()
        # editors = Editor.objects.all()
        self.assertEqual(len(Editor.display_all()), 1)


class TagsTestClass(TestCase):
    # Set up method

    def setUp(self) -> None:
        self.new_tag = Tags(name="Hello")

    def tearDown(self) -> None:
        Tags.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_tag, Tags))

    def test_save_tag(self):
        self.new_tag.save_tag()
        tags = Tags.objects.all()
        self.assertTrue(len(tags) > 0)

    def test_delete_tag(self):
        self.new_tag.save_tag()
        tags = Tags.objects.all()
        self.new_tag.delete_tag()
        self.assertTrue(len(tags) < 1)


class ArticleTestClass(TestCase):
    def setUp(self) -> None:
        # Creating a new editor and saving it
        self.new_editor = Editor(first_name='Paul', last_name='Ngigi', email='paulkush7777@gmail.com')
        self.new_editor.save_editor()

        # Creating a new tag and saving it
        self.new_tag = Tags(name="Hello")
        self.new_tag.save()

        # Creating a new article and saving it
        self.new_article = Article(title='Test Article', post='This is a random test post', editor=self.new_editor)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)

    def tearDown(self) -> None:
        Editor.objects.all().delete()
        Tags.objects.all().delete()
        Article.objects.all().delete()

    def test_get_news_today(self):
        today_news = Article.todays_news()
        self.assertTrue(len(today_news) > 0)

    def test_get_news_by_date(self):
        test_date = '2020-03-12'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d')
        news_by_date = Article.days_news(date)
        self.assertTrue(len(news_by_date) == 0)
