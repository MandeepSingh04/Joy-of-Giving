from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import validate_comma_separated_integer_list
from django.template.defaultfilters import slugify

User= settings.AUTH_USER_MODEL
# Create your models here.
class Post(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    Title = models.CharField(max_length=100)
    Description = models.TextField()
    Image = models.ImageField(upload_to='static/')
    Amount = models.IntegerField(null=True)
    slug = models.SlugField(max_length = 250, null = True, blank = True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.url= slugify(self.Title)
        super(Post, self).save(*args, **kwargs)

    #to view name instead of "contact object" in admin
    def __str__(self):
        return self.Title

    # def get_absolute_url(self):
    #     return reverse('mypost', kwargs={'slug': self.slug})

#makemigrations - create changes and store in a file
#migrate - apply the pending changes created by makemigrations
