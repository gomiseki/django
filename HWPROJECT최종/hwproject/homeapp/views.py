from django.shortcuts import render, redirect
from .models import *
from django.db.models.query_utils import Q

# Create your views here.
def detail(request, title):
    selected_lecture = Lecture.objects.get(title=title)
    posts = Post.objects.all()
    postsList = []

    for post in posts:
        if(post.lecture.title == selected_lecture.title):
            postsList.append(post)
            
    return render(request, 'detail.html', {'selected_lecture' : selected_lecture, 'postsList' : postsList})

def home(request):
    lectures = Lecture.objects.all()
    deptList = list()
    for lecture in lectures:
        deptList.append(lecture.department)
    deptList = set(deptList)
    deptList = list(deptList)
    isTable = False

    return render(request,'home.html',{'lectures': lectures, 'deptList': deptList, 'isTable': isTable})

def search(request):
    lectures = Lecture.objects.all()
    deptList = list()
    for lecture in lectures:
        deptList.append(lecture.department)
    deptList = set(deptList)
    deptList = list(deptList)
    isTable = True
    year = request.POST['year']
    semester = request.POST['semester']
    dept = request.POST['dept']
    searchList = lectures.filter(rq_year=year, rq_semester = semester,department=dept)

    return render(request, 'home.html', {'lectures': lectures, 'deptList': deptList,'isTable' : isTable,'searchList' :searchList})

def new(request):
    elected_lecture = Lecture.objects.get(title=title)
    return render(request, 'new.html', {'selected_lecture' : selected_lecture})

def update(request, title, id):
    selected_lecture = Lecture.objects.get(title=title)
    post = Post.objects.get(id=id)
    if ( request.method == "POST" ):
        post.writer = request.user
        lecture_title = request.POST['title']
        post.lecture = Lecture.objects.get(title=lecture_title)
        post.body = request.POST['body']
        post.rating = request.POST['rating']
        post.save()
        return redirect('detail' , str(post.lecture.title))

    return render(request, 'update.html', {'selected_lecture' : selected_lecture, 'post' : post})


def create(request):
    post = Post()
    post.writer = request.user
    lecture_title = request.GET['title']
    post.lecture = Lecture.objects.get(title=lecture_title)
    post.body = request.GET['body']
    post.rating = request.GET['rating']
    post.save()
    return redirect('detail' , str(post.lecture.title))

def delete (request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('detail' , str(post.lecture.title))

# def db(request): # '127.0.0.1:8000/db'
#     url = "http://18.214.131.153:5000/course"
#     response = requests.get(url)
#     data = response.json()['data'][0]

#     for i in data :
#         course = Course()
#         course.subject = i['subject']

#         course.save

#         return redirect('/')