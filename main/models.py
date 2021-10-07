from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=200)
    category_image = models.ImageField(upload_to='imgs/')

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class News(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=300, default="")
    image = models.ImageField(upload_to='imgs/')
    detail = models.TextField()
    add_time = models.DateField()

    class Meta:
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title


class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    comment = models.TextField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.comment


class Person(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(upload_to='imgs/')

    class Meta:
        verbose_name_plural = 'People'

    def __str__(self):
        return self.name
