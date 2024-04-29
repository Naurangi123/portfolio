from django.core.validators import MinLengthValidator
from django.db import models


# Create your models here.
class Project(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=16)
    address = models.CharField(max_length=16)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=25)
    zip_code = models.CharField(max_length=25)
    country = models.CharField(max_length=25)

    def __str__(self):
        return (f"{self.first_name} {self.last_name}")


class Data(models.Model):
    title = models.CharField(max_length=100)
    descriptions = models.TextField(max_length=250)
    technology = models.CharField(max_length=20)
    image = models.ImageField(upload_to="project_images/", blank=True)

    def __str__(self):
        return {self.title}


class BMI_Calculater(models.Model):
    weight = models.CharField(max_length=250)
    height = models.CharField(max_length=250)

    def __str__(self):
        return self.weight


class Gallery(models.Model):
    image = models.ImageField(upload_to="gallery/", blank=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.image)


class Video(models.Model):
    video = models.FileField(upload_to="video/", blank=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.video)


class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption


class Auther(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_addr = models.EmailField()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200)
    image_name = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    auther = models.ForeignKey(Auther, on_delete=models.SET_NULL, null=True, related_name="posts")
    tag = models.ManyToManyField(Tag)

    def full_content(self):
        return f"{self.title} {self.date} {self.auther}"

    def __str__(self):
        return self.full_content()


# Chat Room

