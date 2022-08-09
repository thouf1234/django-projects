from django import template
from blog.models import Post
register=template.Library()
@register.simple_tag#since there is no name attribute specified while registering you can use the same name as the function below
def total_posts():
    return Post.objects.filter(status='published').count()
@register.inclusion_tag('blog/latest_post_123.html')
def show_latest_post(count=3):#default value is 3
    latest_post=Post.objects.filter(status='published').order_by('-updated')[:count]
    return {'latest_posts':latest_post}
@register.inclusion_tag('blog/most_commented_123.html')#either use get_most_commented_post(n) or use get_top_commented_post(n) . here get_most_commented_post(n) is made by mohamed thoufeeq
def get_most_commented_post(n=3):
    max_count_of_comment_on_post={}
    final=[]
    posts_list=Post.objects.filter(status='published')
    for post in posts_list:
        comment_count=post.comments.filter(active=True).count()
        max_count_of_comment_on_post[post]=comment_count
    max_count_of_comment_on_post_list=list(max_count_of_comment_on_post.items())
    def myFunc(e):
        return e[1]
    max_count_of_comment_on_post_list.sort(reverse=True,key=myFunc)
    for i in max_count_of_comment_on_post_list:
        final.append(i[0])
    return {"final":final[:n]}
from django.db.models import Count
@register.simple_tag
def get_top_commented_post(count=3):
    #to get arrange the post records by ID we have Post.objects.filter(status='published').order_by('id')
    #but if the id column is not there in the Post table then we create a temperary ID column and assign value for the respective rows
    #and to create a temporary column(field) we have to use annotate(temperory_new_field(column name)=logic).order_by('temperory_new_field') 
    return Post.objects.filter(status='published').annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]
