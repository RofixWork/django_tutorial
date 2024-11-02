from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .forms import CommentForm
from .models import Comment, Post, Tag


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    posts = Post.objects.all().order_by("-published_date")
    return render(request, "posts/index.html", {"posts": posts})


def show(request: HttpRequest, id: int) -> HttpResponse:
    post: Post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment: Comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return HttpResponseRedirect(reverse("posts.show", kwargs={"id": id}))
    else:
        form = CommentForm()
        comments = post.comment_set.all()
    return render(
        request, "posts/show.html", {"post": post, "form": form, "comments": comments}
    )


def tag_posts(request: HttpRequest, id: int) -> HttpResponse:
    tag = Tag.objects.get(id=id)
    posts = tag.post_set.all()
    return render(request, "posts/tag_posts.html", {"tag": tag, "posts": posts})
