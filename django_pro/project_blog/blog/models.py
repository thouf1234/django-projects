from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from taggit.managers import TaggableManager
# Create your models here.
class Post(models.Model):
    STATUS_CHOICES =(('draft','Draft'),('published','Published'))
    title=models.CharField(max_length=256)
    slug=models.SlugField(max_length=256,unique_for_date='publish')
    author=models.ForeignKey(User,related_name='blog_posts',on_delete=models.CASCADE)
    body=models.TextField()
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)#date time of create() action
    updated=models.DateTimeField(auto_now=True)#date time of save() action
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    tags=TaggableManager()
    class Meta:
        ordering=('-publish',)#return the post data in ascending order of post when we use Post.objects.all()
    def __str__(self):#if we try to print publish object internally __str__(self) method will be called and we just overriding it and returning title of that publish
        return self.title
    def get_absolute_url(self):
        return reverse('post_detail',args=[self.publish.year,self.publish.strftime('%m'),self.publish.strftime('%d'),self.slug])
    def mail_absolute_url(self):
        return reverse('send_mail',args=[self.id])
#model related to Comments
class Comment(models.Model):
    #in the admin dashboard if you try to add the post field then you can add only by selecting the dropdown having the vaues that we get while trying to print the Post object i.e. __str__, as you mentioned Post inside the ForiegnKey
    post=models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)#ForeignKey key is used when there is a many to one or one to many relatipnship exist. here one post can have multiple comments and the related_name is used to get the all comments related to single post


    name=models.CharField(max_length=32)
    email=models.EmailField()
    body=models.TextField()
    created=models.DateTimeField(auto_now_add=True)#date time of create() action
    updated=models.DateTimeField(auto_now=True)#date time of save() action
    active=models.BooleanField(default=True)#some times as=dmin should diable most vulgar Comments
    class Meta:
        ordering=('-created',)#return the comments data in ascending order of post when we use Post.objects.all()
    def __str__(self):
        return "Commented By {} on {}".format(self.name,self.created)
