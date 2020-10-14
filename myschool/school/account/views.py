from django.shortcuts import render , redirect , reverse ,get_object_or_404
from django.contrib import messages

from .forms import   AccountAuthenticationForm , RegistrationForm , NoteForm
from django.contrib.auth import login , authenticate , logout
from .models import Subject , Videos , Grades , Account , TeacherNotes
from datetime import datetime

# Create your views here.

def reg(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            the_id_number = form.cleaned_data.get('the_id_number')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(the_id_number=the_id_number, password=raw_password)
            login(request, account)
            return redirect('account:home')
        else:
            context['registration_form'] = form
    else: #GET request
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'account/reg.html', context)




def Login(request):
     context = {}
     

     user = request.user
     if user.is_authenticated:
         if   user.is_staff :
            return redirect( 'account:teacherp' , id=user.id) 
         else:
            return redirect( 'account:profile' , id=user.id)

     if request.POST:
         form = AccountAuthenticationForm(request.POST)
         if form.is_valid():
             
             the_id_number = request.POST['the_id_number']
             password = request.POST['password']
             user = authenticate(the_id_number=the_id_number, password=password)
             # edit here
             if user.is_staff:
                login(request, user)
                return redirect('account:teacherp' , id=user.id) 
             elif user:
                
                login(request, user)
                return redirect("account:profile" , id=user.id)
         else:
            messages.error(request, 'Something is not right!')
     else:
         form = AccountAuthenticationForm()

     context['login_form'] = form
     return render(request, 'account/login.html', context)

def Profile(request , id):
    context ={}
    context["notes"] = TeacherNotes.objects.filter(student_id = id)
    student = TeacherNotes.objects.filter(student_id = id).update(is_read=True)

        
    if  len(context["notes"]) < 1:
        context["notes"] = ["لا يوجد ملاحظات على الطالب "]
    context["id"] = id
   
    return render(request, 'account/profile.html' ,context)


def Logout (request):
     
     logout(request)
     return render(request, 'main/home.html')



def GradesV(request):
     context = {}
     if request.POST :
         gradeID = request.POST['id']
         subject = Subject.objects.filter(subject_id = gradeID)
         print(subject)
     else:
         grades = Grades.objects.all()
         context['grades'] = grades
         print(grades)
         return render (request , 'account/grade.html' , context)
         
def SubjectV( request , id):
         context = {}
         
         subjects = Subject.objects.filter(grade_id = id)
         context['subjects'] = subjects
         
         print(context['subjects'])
         return render(request , 'account/subject.html' , context )

def VideosView(request , id):
    
    context = {}
    context["videos"] = Videos.objects.filter(subject_id=id)
    
    return render(request , 'account/videos.html' , context )
    

def FormsGoogle(request , id):
    print(id)
    return  render (request , 'account/examform.html')

def Teacher(request , id):
    context = {}
    
    context["grades"] = Grades.objects.all()
    context["note_sent"] = TeacherNotes.objects.filter(teacher_id = id)
    
    student_grade = 0
    student_id = 0
    note = ""
    date = ""
   
    if request.POST: 
                date =str( datetime.now().year)+'/'+str(datetime.now().month)+'/'+str(datetime.now().day)
                note = request.POST["note"]
                student_id = request.POST.get("student-id")
                print("studentid" , student_id,  'note' , note)
                Note = TeacherNotes(teacher_id=id , note=note , date=date , student_id= student_id )
                Note.save()
                return render(request , 'account/teacher.html')
        
                
                # return  render (request , 'account/teacher.html' , context)
    else: # get
               
                 students = Account.objects.all()
                
                 
                 context["students"] = students
                        
                 return  render (request , 'account/teacher.html' , context)


from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.core import serializers

def ToSelecStudent(request):
    if request.POST:
        input = request.POST.get('inp' , None) 
        students = Account.objects.filter(username__contains=input)

        

        studentsList =[]
        for s in students:
            studentsList.append({"username" : s.username , 'id' : s.id})
           
        print(studentsList)
        
        return JsonResponse({'students' : studentsList} , status=200)