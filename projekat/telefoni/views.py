from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, authenticate
from .models import Article
from .models import Comment
from .forms import ArticleForm
from .forms import CommentForm
from .forms import SignUpForm


def index(req):
    if not req.user.is_authenticated:
        return render(req, 'index.html', {'page_title': 'Mobiles'})
    else:
        return redirect('telefoni:articles')


@login_required
def articles(req):
    tmp = Article.objects.all()
    return render(req, 'articles.html', {'articles': tmp})


@login_required
def allcomments(req, id):
    tmp = Comment.objects.filter(article_id=id)
    return render(req, 'comments.html', {'comments': tmp})


@login_required
def article(req, id):
    tmp = get_object_or_404(Article, id=id)
    return render(req, 'article.html', {'article': tmp, 'page_title': tmp.producer})


@permission_required('telefoni.change_article')
def edit(req, id):
    if req.method == 'POST':
        form = ArticleForm(req.POST)

        if form.is_valid():
            a = Article.objects.get(id=id)
            a.producer = form.cleaned_data['producer']
            a.model = form.cleaned_data['model']
            a.save()
            return redirect('telefoni:articles')
        else:
            return render(req, 'edit.html', {'form': form, 'id': id})
    else:
        a = Article.objects.get(id=id)
        form = ArticleForm(instance=a)
        return render(req, 'edit.html', {'form': form, 'id': id})


@permission_required('telefoni.delete_article')
def delete(req, id):
    a = Article.objects.get(id=id)
    a.delete()
    return redirect('telefoni:articles')


@permission_required('telefoni.add_article')
def new(req):
    if req.method == 'POST':
        form = ArticleForm(req.POST)

        if form.is_valid():
            a = Article(
                producer=form.cleaned_data['producer'], model=form.cleaned_data['model'], owner=req.user)
            a.save()
            return redirect('telefoni:articles')
        else:
            return render(req, 'new.html', {'form': form})
    else:
        form = ArticleForm()
        return render(req, 'new.html', {'form': form})


@login_required
def newcomment(req, id):
    if req.method == 'POST':
        form = CommentForm(req.POST)
        if form.is_valid():
            a = Article.objects.get(id=id)
            c = Comment(content = form.cleaned_data['content'], article = a)
            c.save()
            return redirect('telefoni:articles')
        else:
            return render(req, 'newcomment.html', {'form': form, 'id': id})
    else:
        c = Comment(content = "")
        form = CommentForm(instance=c)
        return render(req, 'newcomment.html', {'form': form, 'id': id})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('telefoni:articles')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
