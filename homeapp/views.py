from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def detail(request, num):
    
    return render(request, 'detail.html')

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

# def db(request): # '127.0.0.1:8000/db'
#     url = "http://18.214.131.153:5000/course"
#     response = requests.get(url)
#     data = response.json()['data'][0]

#     for i in data :
#         course = Course()
#         course.subject = i['subject']

#         course.save

#         return redirect('/')