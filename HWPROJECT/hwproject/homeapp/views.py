from django.shortcuts import render, redirect
from .models import *

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

    print(lectures)

    for lecture in lectures:
        deptList.append(lecture.department)

    deptList = set(deptList)
    deptList = list(deptList)
    isTable = False
    print(isTable)

    return render(request,'home.html',{'lectures': lectures, 'deptList': deptList, 'isTable': isTable})

def search(request):
    lectures = Lecture.objects.all()
    isTable = True
    year = request.POST['year']
    semester = request.POST['semester']
    dept = request.POST['dept']
    searchList = list()
    for lecture in lectures:
        if(lecture.rq_year==year and lecture.rq_semester==semester and lecture.department==dept):
            searchList.append(lecture)
        
    return render(request, 'home.html', {'isTable' : isTable,'searchList' :searchList} )


def new(request):
    return render(request, 'new.html')

def create(request):
    post = Post()
    post.body = request.GET['body']
    post.rating = request.GET['rating']
    post.save()
    return redirect('/detail/' + str(post.id))
# def db(request): # '127.0.0.1:8000/db'
#     url = "http://18.214.131.153:5000/course"
#     response = requests.get(url)
#     data = response.json()['data'][0]

#     for i in data :
#         course = Course()
#         course.subject = i['subject']

#         course.save

#         return redirect('/')