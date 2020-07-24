from django.shortcuts import render, redirect
from .models import *
from django.db.models.query_utils import Q
import requests

def db(request): # '127.0.0.1:8000/db'
    url = "http://18.214.131.153:5000/course"
    response = requests.get(url)
    data = response.json()['data']

    for i in data :
        lecture = Lecture()
        lecture.rq_year = i['rq_year']
        lecture.rq_semester = i['rq_semester']
        lecture.department = i['dept']
        lecture.area = i['area']
        lecture.instruction_number = i['instruction_number']
        lecture.title = i['subject']
        lecture.credit = i['credit']
        lecture.time = i['time']
        lecture.professor = i['professor']
        lecture.save()

    return redirect('/')
# Create your views here.
def detail(request, id):
    selected_lecture = Lecture.objects.get(id=id)
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
    year = int(request.POST['year'][2:])
    semester = int(request.POST['semester'])
    dept = request.POST['dept']
    searchList = Lecture.objects.filter(rq_year=year, rq_semester = semester,department=dept)
    print(searchList)
    return render(request, 'home.html', {'lectures': lectures, 'deptList': deptList,'isTable' : isTable,'searchList' :searchList})

def new(request, id):
    selected_lecture = Lecture.objects.get(id=id)
    return render(request, 'new.html', {'selected_lecture' : selected_lecture})

def update(request, title, id):
    #selected_lecture = Lecture.objects.get(title=title)
    post = Post.objects.get(id=id)
    if ( request.method == "POST" ):
        post.writer = request.user
        lecture_title = request.POST['title']
        post.lecture = Lecture.objects.get(id=post.lecture.id)
        post.body = request.POST['body']
        post.rating = request.POST['rating']
        post.save()
        return redirect('detail' , str(post.lecture.))

    return render(request, 'update.html', {'selected_lecture' : selected_lecture, 'post' : post})


def create(request, id):
    post = Post()
    post.writer = request.user
    lecture_title = request.GET['title']
    post.lecture = Lecture.objects.get(id=id)
    post.body = request.GET['body']
    post.rating = request.GET['rating']
    post.save()
    return redirect('detail' , id)

def delete (request, id):
    post = Post.objects.get(id=id)
    k= post.lecture.id
    post.delete()
    return redirect('detail' , k)

# def db(request): # '127.0.0.1:8000/db'
#     url = "http://18.214.131.153:5000/course"
#     response = requests.get(url)
#     data = response.json()['data'][0]

#     for i in data :
#         course = Course()
#         course.subject = i['subject']

#         course.save

#         return redirect('/')