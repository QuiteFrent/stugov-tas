from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Post, Vote
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .forms import PostForm, CommentForm



@login_required
def index(request):
    posts = Post.objects.order_by('votes')[:5]
    context = {'posts': posts}
    return render(request, 'petitions/index.html', context)


@login_required
def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comment_form = CommentForm(request.POST or None, initial={'author': request.user, 'post': post})
    if comment_form.is_valid():
        comment_form.save(commit=True)

    return render(request, 'petitions/detail.html',
                  {'post': post, 'comment_form': comment_form, 'current_user': request.user})


@login_required
def create(request):
    post_form = PostForm(request.POST or None, initial={'author': request.user})

    if post_form.is_valid():
        post_form.save(commit=True)
        # post.title = post_form.cleaned_data['title']
        # post.body = post_form.cleaned_data['body']
        # post.save()
        return redirect(reverse('petitions:index'))

    return render(request, 'petitions/create.html', {'form': post_form})


@login_required
def vote(request, pk):
    user = request.user

    if user.is_authenticated:
        post = Post.objects.get(pk=pk)
        user_vote = Vote.objects.filter(post=post, user=user)

        if not user_vote.exists():  # If already upvoted, delete vote. If not, upvote.
            Vote.objects.get_or_create(post=post, user=user)
        else:
            user_vote.delete()
        return JsonResponse({'votes': post.votes_count()})
    else:
        return JsonResponse({})
