from django.contrib import admin
from blog.models import Post,Comment
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=['title','slug','author','body','publish','created','updated','status']
    list_filter=('status','author','created','publish')#to filter the post table records based on status(all,draft,published),author(babu,BMDTBTECHIT,ramu), created and publish
    search_fields=('title','body')#the provided search will be compared with title and body for match
    #raw_id_fields=('author',)#to select the aiuthor field by their ID (drop down will be gone and a search icon will appear to show the available users in User model)
    date_hierarchy='publish'#this will add a nav bar with dates and selection respective date will shows the post that published on that dater
    ordering=['status','publish']#to sort the post records based on status and publish (a arrow next to those fields in the table is added clocking which we can choose ascending or descending )
    prepopulated_fields={'slug':('title',)}#tells can you please populate slug field based on title field(i.e.the title field value will be considered as a value for slug field too)
class CommentAdmin(admin.ModelAdmin):
    list_display=['name','email','post','body','created','updated','active']
    list_filter=('active','created','updated')
    search_fields=('name','email','body')
admin.site.register(Comment,CommentAdmin)
admin.site.register(Post,PostAdmin)
