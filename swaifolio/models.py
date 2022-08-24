from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from PIL import Image

class Profile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True, null=True, upload_to = "avatar")
    about = models.TextField(blank=True, null=True)
    cv = models.FileField(blank=True, null=True, upload_to="cv")

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
    


class Contact(models.Model):
    
    class Meta:
    
        ordering = ["timestamp"]

    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(verbose_name="Name", max_length=100)
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name="Message")

    def __str__(self):
        return f'{self.name}'

class Portfolio(models.Model):
    
    class Meta:
        verbose_name_plural = 'Portfolio Profiles'
        verbose_name = 'Portfolio'
        ordering = ["name"]
    date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    body = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="portfolio")
    fk = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)


class Services(models.Model):

    class Meta:
        ordering = ["name"]

    name = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="simage")
    description = models.CharField(max_length=500, blank=True, null=True)
    fk_serv = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class Skill(models.Model):

    name = models.CharField(max_length=20, blank=True, null=True)
    score = models.IntegerField(default=80, blank=True, null=True)
    image = models.FileField(blank=True, null=True, upload_to="skills")
    fk_skill = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

#for use with PIL
#def save(self, *args, **kwargs):
#        super(Profile, self).save(*args, **kwargs)
#
#        img = Image.open(self.avatar.path)
#
#        if img.height > 300 or img.width > 300:
#            output_size = (100,100)
#            img.thumbnail(output_size)
#            img.save(self.avatar.path)
