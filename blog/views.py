from django.shortcuts import render, redirect
from blog.models import BlogComment,Blogs
from django.contrib.auth import authenticate, login as auth_login

# Create your views here.
def blogHome(request):
    return render(request, 'home/blog.html')

def blogPost(request, slug):
    post = Blogs.objects.filter(slug=slug).first()
    comments = BlogComment.objects.filter(post=post, parent = None)
    replies = BlogComment.objects.filter(post=post).exclude(parent= None)
    repDict = {}
    for reply in replies:
        if reply.parent.sno not in repDict.keys():
            repDict[reply.parent.sno] = [reply]
        else:
            repDict[reply.parent.sno].append(reply)


    context = {"post": post, "comments": comments, "user": request.user, "repDict": repDict}
    return render(request, "blog/blogPost.html", context)


def blogpostComment(request):
    
    if request.method == "POST":
        comment = request.POST.get("comment")
        user = request.user
        postSno = request.POST.get("postSno")
        post = Blogs.objects.get(sno=postSno)
        parentSno = request.POST.get("parentSno")
        if(parentSno == ""):
            comment = BlogComment(comment=comment, user=user, post=post)

        else:
            parent = BlogComment.objects.get(sno=parentSno)
            comment = BlogComment(comment=comment, user=user, post=post, parent=parent)
       
        comment.save()
    return redirect(f"/blog/{post.slug}")


def blogsearch(request):
    query = request.GET['query']
    if len(query)>70:
        allPosts = Blogs.objects.none()
    else:
        allPostsTitle = Blogs.objects.filter(title__icontains=query)
        allPostsContent = Blogs.objects.filter(subtitle__icontains=query)
        allPosts = allPostsTitle.union(allPostsContent)
    params = {"allPosts": allPosts, "query": query}
    return render(request, "home/search.html", params)