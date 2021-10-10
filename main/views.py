from django.shortcuts import render
from django.contrib import messages
from .models import News, Category, Comment, Person

# Create your views here.


def home(request):
    first_news = News.objects.last()
    three_news = News.objects.order_by('-id')[1:5]
    three_categories = Category.objects.all()
    return render(request, 'home.html', {
        'first_news': first_news,
        'three_news': three_news,
        'three_categories': three_categories,
    })


def all_news(request):
    all_news = News.objects.order_by('-id')
    return render(request, 'all-news.html', {
        'all_news': all_news,
    })


def detail(request, id):
    news = News.objects.get(pk=id)
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        comment = request.POST['message']
        Comment.objects.create(
            news=news,
            name=name,
            email=email,
            comment=comment
        )
        messages.success(
            request, 'Comment submitted! Please wait for it to be validated!')
    category = Category.objects.get(id=news.category.id)
    related_news = News.objects.filter(
        category=category).exclude(id=id).order_by('-id')[:4]
    comments = Comment.objects.filter(news=news, status=True).order_by('-id')
    return render(request, 'detail.html', {
        'news': news,
        'related_news': related_news,
        'comments': comments,
    })


def all_category(request):
    cats = Category.objects.all()
    return render(request, 'category.html', {
        'cats': cats,
    })


def category(request, id):
    category = Category.objects.get(id=id)
    news = News.objects.filter(category=category)
    return render(request, 'category-news.html', {
        'news': news,
        'category': category,
    })


def search_results(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        all_news = News.objects.filter(title__contains=searched)
        return render(request, 'search_results.html', {
            'searched': searched,
            'all_news': all_news,
        })
    else:
        return render(request, 'search_results.html', {

        })


def about(request):
    people = Person.objects.all()
    return render(request, 'about.html', {
        'people': people,
    })


def bio(request, id):
    person = Person.objects.get(id=id)
    news = News.objects.filter(writer=person)
    return render(request, 'bio.html', {
        'person': person,
        'news': news,
    })
