from django.db import models
CHOICES = [
    ("active","Active")
]
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to="images/",blank=False, null=False)
    author= models.ForeignKey("auth.User", on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=CHOICES,default="active")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=False, null=False)


## 1 - 1 Relationship
# 1 user can have only 1 profile   => 1
# 1 profile is associated to only 1 user  => 1
# OneToOneField() => Any Model

## 1 - M Relationship
# 1 user can add M post  => M
# 1 post is associated to only 1 user => 1
# In django use ForeignKey() => Use in Many side Model

## M - M Relationship
# 1 student can learn from M teachers => M
# 1 teacher can teach M students => M
# ManyToManyField() => Any Place