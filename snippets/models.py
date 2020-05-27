from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
import random
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
import string, random
from django.conf import settings


LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class SystemProperties(models.Model):

    serial = random.randint(1000, 2000)

    id = models.IntegerField(primary_key=True, default=serial)
    key = models.CharField(max_length=100)
    value = models.CharField(max_length=500)
    sys_created_on = models.DateTimeField(auto_now_add=True)
    sys_updated_on = models.DateTimeField(auto_now=True)
    description = models.TextField()


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='snippets', on_delete=models.CASCADE)
    highlighted = models.TextField()
    number = models.CharField(max_length=10, blank=True)
    sys_created_on = models.DateTimeField(auto_now_add=True, blank=True)
    sys_updated_on = models.DateTimeField(auto_now=True, blank=True)

    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """
        lexer = get_lexer_by_name(self.language)
        linenos = 'table' if self.linenos else False
        options = {'title': self.title} if self.title else {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                  full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        # self.id = int(''.join(random.choices(string.digits, k=16)))
        super(Snippet, self).save(*args, **kwargs)

    class Meta:
        ordering = ['created']


# Create your models here.
