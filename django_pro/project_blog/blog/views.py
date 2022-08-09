from django.shortcuts import render,get_object_or_404
from blog.models import Post, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.forms import CommentForm
from taggit.models import Tag
from django.views.generic import ListView#this is for pagination using class based view
class PostListView(ListView):
    model=Post
    paginate_by=2
    #default template_name is 'post_list.html'
    #default context_object_name is 'post_list' OR 'object'
    #default paginator_object_name is page_obj
# Create your views here.
def post_list_view(request,tag_slug=None):#for example if anyone click the django slug then "django" is the value in the slug field Tag models in taggit application then that 'django' is assigned to tag_slug
    post_list=Post.objects.filter(status='published')#to display only the post that have status field 'published'
    tag=None
    if tag_slug:#if tag_slug have some string value (eg: "django") other than None the this if will execute
        tag=get_object_or_404(Tag,slug=tag_slug)#getting the tag clicked with the help of matching it with the slug field
        post_list=post_list.filter(tags__in=[tag])#we have all the published post_list but after clicking the tags we should display only the related post to that tag and for that we use filter on the Post object (post_list) and applying the condition filter the post_list only if that post have the tags that we got in above line

    paginator=Paginator(post_list,3)#this creates a paginator object with the posts records got at lino no 14 and a number telling how many such record(post_list) can be there in one page
    page_number=request.GET.get('page')#my understanding on this line was 'as a part of paginator object creation there was a form with 'method' =GET having a field named page is getting some value and by default its not of integer type so lets have its something lik page:"this is string" and this is what happen for the first time trying to get page field's value i.e. url without page value but, after clicking the page link which is implemented as a navigation bar by paginator then that form's page field will get that value and submitted followed by updating the request so, if we use GET on the request by specifying the form field page we get the value(user clicked page no on the paginator implemented navigation bar)'
    try:
        post_list=paginator.page(page_number)
    except PageNotAnInteger:#this will evoke if the value for the page is not an integer
        post_list=paginator.page(1)#if the url come without any page no then display first page
    except EmptyPage:#this will evoke if the value given to the page is integer but not valid (i.e. either negative or more than the available page no )
        post_list=paginator.page(paginator.num_pages)#display the last valid page (paginator.num_pages will give the last page number for the above created paginator object )
    return render(request,'blog/post_list.html',{'post_list':post_list,'tag':tag})
def post_detail_view(request,year,month,day,slug):

    #UNDERSTANDING RELATED_NAMES IN ForeignKey() FIELD (NOTE : THE FOLLOWING FIVE LINES OF CODE IS JUST FOR UNDERSTANDING HOW RELATED NAMES WORKS AND THESE VALUES ARE NOT USED ANYWHERE IN THE APPLICATION)
    from django.contrib.auth.models import User
    author_babu=get_object_or_404(User,username='babu')
    babu_posts=author_babu.blog_posts.all()
    b_p = Post.objects.filter(author=2)#ForiegnKey field will always expect id
    print('b_p',b_p)#this b_p and the babu_posts are same then you may wonder why we have to use ForiegnKey, but if you see carefully you made this possible only with the ForeignKey field "author"
    print(babu_posts)


    #post=Post.objects.get(publish__year=year,publish__month=month,publish__day=day,slug=slug,status='published')#this works fine and same as the code in line no42 but if the given model does not match then it will raise DoesNotExist error but the code in line no 42 will raise 404 error if given model does not match
    post=get_object_or_404(Post,slug=slug,status='published',publish__year=year,publish__month=month,publish__day=day)
    print("id",post.id)
    comments=post.comments.filter(active=True)#only admin not disabled comments should be displayed. this line is to take all the comments related to a single post got at line no 42
    c=Comment.objects.filter(post=post.id)#ForeignKey field will always expect id
    print("comments",c)#this c and the comments are same then you may wonder why we have to use ForiegnKey, but if you see carefully you made this possible only with the ForeignKey field "post"
    print(comments)
    comment_submit=False
    if request.method =='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            print("comment form validation completed and submitted successfully")
            new_comment=form.save(commit=False)#the form in this line will just have name, email and body but not the details of the post to which this comment is made for and so we should not save() this comment to database
            new_comment.post=post#associating this new_comment to the post got ot line no 42
            new_comment.save()
            comment_submit=True
    else:
        form=CommentForm()
    return render(request,'blog/post_detail.html',{'post':post,'form':form,'comment_submit':comment_submit,'comments':comments})


from django.core.mail import send_mail
from blog.forms import EmailSendForm
def mail_Send_view(request,id):#here you must give the same variable name as in the name capturing group of url other wise you will get this error 'mail_Send_view() got an unexpected keyword argument 'id''
    post=get_object_or_404(Post,id=id,status='published')
    sent=False
    if request.method =='POST':
        form = EmailSendForm(request.POST)
        if form.is_valid():
            print("mail form validation completed and submitted successfully")
            cd=form.cleaned_data
            if ',' in cd['to']:
                to=cd['to'].split(',')
            else:
                to=[cd['to']]
            msg=post.body
            post_url=request.build_absolute_uri(post.get_absolute_url())#here "post.get_absolute_url()" is responsible to generate the post url (/index/detail/2022/07/30/python-importance/)ie.e there is a method in the models.py of class Post and the reqest.build_absolute_uri is responsible to generate htthttp://127.0.0.1:8000/
            #msg= "Read the post At url:{}\n\n {}\'s Comments: \n {}".format(post_url,cd['name'],cd['comments'])
            subject="{} ({}) recommends you to read {}".format(cd['name'],cd['email'],post.title)
            send_mail(subject,msg,cd['email'],to,fail_silently=False)
            sent=True
    else:
        form=EmailSendForm()
    return render(request,'blog/sharebymail.html',{'form':form,'post':post,'sent':sent})
