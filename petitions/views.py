from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.forms import modelformset_factory
from .forms import PostForm, CommentForm, PostImageForm
from .models import Post, Vote, PostImage


@login_required
def index(request):
    posts = Post.objects.order_by('votes')[:5]
    context = {'posts': posts}
    return render(request, 'petitions/index.html', context)


@login_required
def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        print(request.POST)
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            comment_form.save(commit=True)
        else:
            print(comment_form.errors)
    else:
        print(request.user)
        print(post)
        comment_form = CommentForm(initial={'author': request.user, 'post': post})

    show_comments = False
    for x in post.comments.all():
        print(x.author == request.user)
        if x.status == 'a' or x.author == request.user:
            show_comments = True

    return render(request, 'petitions/detail.html',
                  {'post': post, 'comment_form': comment_form, 'current_user': request.user,
                   'show_comments': show_comments})


@login_required
def create(request):
    ImageFormSet = modelformset_factory(PostImage, form=PostImageForm, extra=3)
    if request.method == 'POST':
        post_form = PostForm(request.POST)

        if post_form.is_valid():
            post = post_form.save()
            image_form_set = ImageFormSet(request.POST, request.FILES, queryset=PostImage.objects.none())
            for image_form in image_form_set:
                print()
                if image_form.is_valid() and image_form.cleaned_data.get('image') is not None:
                    image = PostImage(post=post, image=image_form.cleaned_data.get('image'))
                    image.save()

            return redirect(reverse('petitions:index'))
    else:
        post_form = PostForm(initial={'author': request.user})
        image_form_set = ImageFormSet(queryset=PostImage.objects.none())

    return render(request, 'petitions/create.html', {'post_form': post_form, 'image_form_set': image_form_set})


# post.title = post_form.cleaned_data['title']
# post.body = post_form.cleaned_data['body']
# post.save()

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
