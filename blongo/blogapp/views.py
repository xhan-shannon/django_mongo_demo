import datetime
from django.shortcuts import render
from django.shortcuts import render_to_response

# Create your views here.
from django.template import RequestContext

from blogapp.models import Post


def index(request):
    if request.method == 'POST':
        # save new post
        title = request.POST['title']
        content = request.POST['content']
        post = Post(title=title)
        post.content = content
        post.last_update = datetime.datetime.now()
        post.save()

    posts = Post.objects
    return render_to_response("index.html", {'Posts': posts})
    #, context_instance=RequestContext(request))

def update(request):
    id = eval("request." + request.method + "['id']")
    post = Post.objects(id=id)[0]

    if request.method == 'POST':
        template_html = "index.html"
        post.tilte = request.POST['title']
        post.last_update = datetime.datetime.now()
        post.content = request.POST['content']
        post.save()
        params = {'Posts': Post.objects}
    else:
        template_html = 'update.html'
        params = {'post': post}

    return render_to_response(template_html,
                              params)



def delete(request):
    '''
    To delete the post which id is from user selection
    :param request:
    :return:
    '''
    id = eval("request." + request.method + "['id']")
    if request.method == 'POST':
        post = Post.objects(id=id)[0]
        post.delete()
        template_html = "index.html"
        params = {'Posts': Post.objects}
    else:
        template_html = "delete.html"
        params = {'id': id}

    return render_to_response(template_html,
                              params)