# from home.models import Cheatsheets, Blogs
from django.shortcuts import render, redirect
from sheets.models import Cheatsheets
from sheets.models import  CheetsheetComment
# from home.models import Cheatsheets, Blogs
# from django.contrib.auth import authenticate, login as auth_login

# Create your views here.
def blogHome(request):
    return render(request, 'home/sheets.html')


def cheatsheetPost(request, slug):
    post = Cheatsheets.objects.filter(slug=slug).first()
    comments = CheetsheetComment.objects.filter(post=post, parent = None)
    replies = CheetsheetComment.objects.filter(post=post).exclude(parent= None)
    repDict = {}
    for reply in replies:
        if reply.parent.sno not in repDict.keys():
            repDict[reply.parent.sno] = [reply]
        else:
            repDict[reply.parent.sno].append(reply)


    context = {"post": post, "comments": comments, "user": request.user, "repDict": repDict}
    return render(request, "sheets/cheatsheetPost.html", context)


def postComment(request):
    
    if request.method == "POST":
        comment = request.POST.get("comment")
        user = request.user
        postSno = request.POST.get("postSno")
        post = Cheatsheets.objects.get(sno=postSno)
        parentSno = request.POST.get("parentSno")
        if(parentSno == ""):
            comment = CheetsheetComment(comment=comment, user=user, post=post)

        else:
            parent = CheetsheetComment.objects.get(sno=parentSno)
            comment = CheetsheetComment(comment=comment, user=user, post=post, parent=parent)
       
        comment.save()
    return redirect(f"/sheets/{post.slug}")


def sheetsearch(request):
    query = request.GET['query']
    if len(query)>70:
        allPosts = Cheatsheets.objects.none()
    else:
        allPostsTitle = Cheatsheets.objects.filter(title__icontains=query)
        allPostsContent = Cheatsheets.objects.filter(subtitle__icontains=query)
        allPosts = allPostsTitle.union(allPostsContent)
    params = {"allPosts": allPosts, "query": query}
    return render(request, "home/sheetsearch.html", params)