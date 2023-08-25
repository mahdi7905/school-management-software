from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.forms import inlineformset_factory
from django.http import HttpResponse


from core.models import *
from .models import *
from .forms import *
from .decorators import *

# Create your views here.
@login_required(login_url='login')
@redirector
def emptypage(request):
    return render(request, 'emptypage.html')

@authenticatedUser
def loginpage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('portal')
        else:
            messages.info(request, 'Username or Passwor Incorrect')
            return redirect('login')

    return render(request, 'login.html')

@login_required(login_url='login')
def logoutpage(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def page(request):

    return render(request, 'page.html')

#Content Creator Views
@login_required(login_url='login')
@allowedUser(allowed_roles=['creator'])
def contentCreator(request):
    posts = Post.objects.all().order_by('-id')

    context = {'posts': posts}
    return render(request, 'creatorpanel.html', context)

@login_required(login_url='login')
@allowedUser(allowed_roles=['creator'])
def creatPost(request):
    postForm = ContentCreationForm()

    if request.method == 'POST':
        postForm = ContentCreationForm(request.POST, request.FILES)
        if postForm.is_valid():
            postForm.save()
            return redirect('contentCreator')

    context = {'postForm':postForm}
    return render(request, 'createpost.html', context)

@login_required(login_url='login')
@allowedUser(allowed_roles=['creator'])
def editPost(request, pk):
    post = Post.objects.get(id=pk)
    postForm = ContentCreationForm(instance=post)

    if request.method == 'POST':
        postForm = ContentCreationForm(request.POST, request.FILES, instance=post)
        if postForm.is_valid():
            postForm.save()
            return redirect('contentCreator')

    context = {'post':post, 'postForm':postForm}
    return render(request, 'editpost.html', context)

@login_required(login_url='login')
@allowedUser(allowed_roles=['creator'])
def deletePost(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('contentCreator')

    context = {'post':post}
    return render(request, 'deletepost.html', context)


#Admin Views
@login_required(login_url='login')
@allowedUser(allowed_roles=['kia admin'])
def kiaAdmin(request):
    pupils = Pupil.objects.all()
    c_g1 = pupils.filter(Conventional_Grade='1')
    c_g2 = pupils.filter(Conventional_Grade='2')
    c_g3 = pupils.filter(Conventional_Grade="3")
    c_g4 = pupils.filter(Conventional_Grade='4')
    c_g5 = pupils.filter(Conventional_Grade='5')
    c_g6 = pupils.filter(Conventional_Grade='6')

    i_g1 = pupils.filter(Islamiya_Grade='1')
    i_g2 = pupils.filter(Islamiya_Grade='2')
    i_g3 = pupils.filter(Islamiya_Grade='3')
    i_g4 = pupils.filter(Islamiya_Grade='4')
    i_g5 = pupils.filter(Islamiya_Grade='5')
    i_g6 = pupils.filter(Islamiya_Grade='6')

    context = {
        'c_g1':c_g1,
        'c_g2':c_g2,
        'c_g3':c_g3,
        'c_g4':c_g4,
        'c_g5':c_g5,
        'c_g6':c_g6,
        'i_g1':i_g1,
        'i_g2':i_g2,
        'i_g3':i_g3,
        'i_g4':i_g4,
        'i_g5':i_g5,
        'i_g6':i_g6,
    }
    return render(request, 'admin.html', context)

@login_required(login_url='login')
@allowedUser(allowed_roles=['kia admin'])
def teacherReg(request):

    conventionalHead = Group.objects.get(name='conventional head')
    islamiyaHead = Group.objects.get(name='islamiya head')
    primaryHead = Group.objects.get(name='primary head')
    nurseryHead = Group.objects.get(name='nursery head')
    primaryTeachers = Group.objects.get(name='primary teachers')
    nurseryTeachers = Group.objects.get(name='nursery teachers')
    IslamiyaTeachers = Group.objects.get(name='islamiya teachers')

    if request.method == 'POST':
        first_name = request.POST['f_name']
        surname = request.POST['surname']
        other_name = request.POST['o_name']
        username = request.POST['username']
        phone = request.POST['phone']
        email = request.POST['email']
        account_role = request.POST['role']
        password = request.POST['password']

        if User.objects.filter(username = username).exists():
            messages.info(request, 'Username Already Taken')
            return redirect('teacher-reg')
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'Email Already Taken')
            return redirect('teacher-reg')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            Teacher.objects.create(user=user, first_name=first_name, surname=surname, other_name=other_name, Phone=phone, email=email, position=account_role)
            if account_role == 'CONVENTIONAL HEAD':
                user.groups.add(conventionalHead)
            elif account_role == 'ISLAMIYA HEAD':
                user.groups.add(islamiyaHead)
            elif account_role == 'PRIMARY HEAD':
                user.groups.add(primaryHead)
            elif account_role == 'NURSERY HEAD':
                user.groups.add(nurseryHead)
            elif account_role == 'CONVENTIONAL TEACHER':
                user.groups.add(primaryTeachers)
            elif account_role == 'NURSERY TEACHER':
                user.groups.add(nurseryTeachers)
            elif account_role == 'ISLAMIYA TEACHER':
                user.groups.add(IslamiyaTeachers)
            return redirect('kia-admin')
    return render(request, 'teacherreg.html')

@login_required(login_url='login')
@allowedUser(allowed_roles=['kia admin'])
def pupilReg(request):
    pupils = Group.objects.get(name='pupils')
    if request.method == 'POST':
        first_name = request.POST['fname']
        surname = request.POST['surname']
        other_name = request.POST['oname']
        username = request.POST['username']
        c_grade = request.POST['c_grade']
        i_grade = request.POST['i_grade']
        password = request.POST['password']
        if username == password:
            if User.objects.filter(username = username).exists():
                messages.info(request, 'Admission Number Already in Use')
                return redirect('pupil-reg')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                Pupil.objects.create(user=user, first_name=first_name, surname=surname, other_name=other_name, ADM_No=username, Conventional_Grade=c_grade, Islamiya_Grade=i_grade)
                user.groups.add(pupils)
                return redirect('kia-admin')
        else:
            messages.info(request, 'Admission Number and Password Must be Thesame')
            return redirect('pupil-reg')
    return render(request, 'pupilreg.html')

@login_required(login_url='login')
@allowedUser(allowed_roles=['kia admin'])
def applications(request):
    teachingapp = Application.objects.all().order_by('id')

    context = {'teachingapp':teachingapp}
    return render(request, 'applications.html', context)

@login_required(login_url='login')
@allowedUser(allowed_roles=['kia admin'])
def viewApplication(request, pk):
    app = Application.objects.get(id=pk)

    context = {'app':app}
    return render(request, 'appview.html', context)

@login_required(login_url='login')
@allowedUser(allowed_roles=['kia admin'])
def deleteApplication(request, pk):
    app = Application.objects.get(id=pk)
    if request.method == 'POST':
        app.delete()
        return redirect('applications')
    context = {'app':app}
    return render(request, 'deleteapp.html', context)

@login_required(login_url='login')
@allowedUser(allowed_roles=['kia admin', 'conventional head', 'islamiya head', 'primary head', 'nursery head'])
def details(request, pk):
    pupil = Pupil.objects.get(id=pk)

    context = {'pupil':pupil}
    return render(request, 'details.html', context)

@login_required(login_url='login')
@allowedUser(allowed_roles=['kia admin', 'conventional head', 'islamiya head', 'primary head', 'nursery head'])
def medicalEmergency(request, pk):
    pupil = Pupil.objects.get(id=pk)

    context = {'pupil':pupil}
    return render(request, 'medicalEmergency.html', context)

@login_required(login_url='login')
@allowedUser(allowed_roles=['kia admin', 'pupils'])
def updatePupil(request, pk):
    pupil = Pupil.objects.get(id=pk)
    form = PupilForm(instance=pupil)

    if request.method == 'POST':
        form = PupilForm(request.POST, request.FILES, instance=pupil)
        if form.is_valid():
            form.save()
            group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
            if group == 'kia admin':
                return redirect('kia-admin')
            if group == 'pupils':
                return redirect('dashboard')

    context = {'form':form, 'pupil':pupil}
    return render(request, 'updatebio.html', context)

@login_required(login_url='login')
@allowedUser(allowed_roles=['conventional head'])
def kiaHead(request):
    pupils = Pupil.objects.all()
    c_g1 = pupils.filter(Conventional_Grade="1")
    c_g2 = pupils.filter(Conventional_Grade="2")
    c_g3 = pupils.filter(Conventional_Grade="3")
    c_g4 = pupils.filter(Conventional_Grade="4")
    c_g5 = pupils.filter(Conventional_Grade="5")
    c_g6 = pupils.filter(Conventional_Grade="6")
    nursery1 = pupils.filter(Conventional_Grade="nursery1")
    nursery2 = pupils.filter(Conventional_Grade="nursery2")
    context = {
        'c_g1':c_g1,
        'c_g2':c_g2,
        'c_g3':c_g3,
        'c_g4':c_g4,
        'c_g5':c_g5,
        'c_g6':c_g6,
        'nursery1':nursery1,
        'nursery2':nursery2,
    }
    return render(request, 'headteacher.html', context)

@login_required(login_url='login')
@allowedUser(allowed_roles=['islamiya head'])
def islamiyaHead(request):
    pupils = Pupil.objects.all()
    c_g1 = pupils.filter(Islamiya_Grade="1")
    c_g2 = pupils.filter(Islamiya_Grade="2")
    c_g3 = pupils.filter(Islamiya_Grade="3")
    c_g4 = pupils.filter(Islamiya_Grade="4")
    c_g5 = pupils.filter(Islamiya_Grade="5")
    c_g6 = pupils.filter(Islamiya_Grade="6")
    
    context = {
        'c_g1':c_g1,
        'c_g2':c_g2,
        'c_g3':c_g3,
        'c_g4':c_g4,
        'c_g5':c_g5,
        'c_g6':c_g6,
    }
    return render(request, 'islamiyahead.html', context)

@login_required(login_url='login')
@allowedUser(allowed_roles=['primary head', 'nursery head'])
def sectionalHead(request):
    pupils = Pupil.objects.all()
    c_g1 = pupils.filter(Conventional_Grade="1")
    c_g2 = pupils.filter(Conventional_Grade="2")
    c_g3 = pupils.filter(Conventional_Grade="3")
    c_g4 = pupils.filter(Conventional_Grade="4")
    c_g5 = pupils.filter(Conventional_Grade="5")
    c_g6 = pupils.filter(Conventional_Grade="6")
    nursery1 = pupils.filter(Conventional_Grade="nursery1")
    nursery2 = pupils.filter(Conventional_Grade="nursery2")
    
    context = {
        'c_g1':c_g1,
        'c_g2':c_g2,
        'c_g3':c_g3,
        'c_g4':c_g4,
        'c_g5':c_g5,
        'c_g6':c_g6,
        'nursery1':nursery1,
        'nursery2':nursery2,
    }
    return render(request, 'sectionalhead.html', context)

@login_required(login_url='login')
@allowedUser(allowed_roles=['conventional head', 'islamiya head', 'primary head', 'nursery head'])
def Teachers(request):
    teachers = Teacher.objects.all()
    conventional = teachers.filter(position="CONVENTIONAL TEACHER")
    nursery = teachers.filter(position = "NURSERY TEACHER")
    islamiya = teachers.filter(position = "ISLAMIYA TEACHER")
    
    context = {'conventional':conventional, 'nursery':nursery, 'islamiya':islamiya,}
    return render(request, 'teachers.html', context)

def pupilGradeUpdate(request):
    

    context = {}
    return render(request, 'pupilupgrade.html', context)

@login_required(login_url='login')
@allowedUser(allowed_roles=['conventional head', 'islamiya head', 'primary head', 'nursery head'])
def teacherGradeUpdate(request, pk):
    teacher = Teacher.objects.get(id=pk)
    upgradeForm = teacherUpgrade_Form(instance=teacher)
    if request.method == 'POST':
        upgradeForm = teacherUpgrade_Form(request.POST, instance=teacher)
        if upgradeForm.is_valid():
            upgradeForm.save()
            return redirect('teachers')
    context = {'teacher':teacher, 'upgradeForm':upgradeForm}
    return render(request, 'teacherupgrade.html', context)



#Pupil Panel
@login_required(login_url='login')
@allowedUser(allowed_roles=['pupils'])
def pupilPanel(request):

    context = {}
    return render(request, 'dashboard.html', context)

@login_required(login_url='login')
@allowedUser(allowed_roles=['pupils'])
def admissionLetter(request):

    context = {}
    return render(request, 'admission.html', context)

@login_required(login_url='login')
@allowedUser(allowed_roles=['pupils'])
def attachments(request):

    context = {}
    return render(request, 'attachments.html', context)

@login_required(login_url='login')
@allowedUser(allowed_roles=['pupils'])
def results(request):

    context = {}
    return render(request, 'result.html', context)

@login_required(login_url='login')
@allowedUser(allowed_roles=['pupils'])
def reports(request):

    context = {}
    return render(request, 'report.html', context)

@login_required(login_url='login')
@allowedUser(allowed_roles=['primary teachers', 'nursery teachers', 'islamiya teachers'])
def teacherPanel(request):
    pupils = Pupil.objects.all()
    c_pupils = pupils.filter(Conventional_Grade=request.user.teacher.Grade, Conventional_Arm=request.user.teacher.Arm)
    i_pupils = pupils.filter(Islamiya_Grade=request.user.teacher.Grade, Islamiya_Arm=request.user.teacher.Arm)

    context = {'c_pupils':c_pupils, 'i_pupils':i_pupils}
    return render(request, 'teacherpanel.html', context)

@login_required(login_url='login')
@allowedUser(allowed_roles=['primary teachers', 'nursery teachers', 'islamiya teachers'])
def resultUpload(request, pk):
    pupil = Pupil.objects.get(id=pk)
    Grade1_Result = Grade1_Form(instance=pupil)
    Grade2_Result = Grade2_Form(instance=pupil)
    Grade3_Result = Grade3_Form(instance=pupil)
    Grade4_Result = Grade4_Form(instance=pupil)
    Grade5_Result = Grade5_Form(instance=pupil)
    Grade6_Result = Grade6_Form(instance=pupil)

    Saff1_Result = Saff1_Form(instance=pupil)
    Saff2_Result = Saff2_Form(instance=pupil)
    Saff3_Result = Saff3_Form(instance=pupil)
    Saff4_Result = Saff4_Form(instance=pupil)
    Saff5_Result = Saff5_Form(instance=pupil)
    Saff6_Result = Saff6_Form(instance=pupil)
   

    context = { 'pupil':pupil, 
                'Grade1_Result':Grade1_Result, 
                'Grade2_Result':Grade2_Result,
                'Grade1_Result':Grade3_Result,
                'Grade4_Result':Grade4_Result,
                'Grade5_Result':Grade5_Result,
                'Grade6_Result':Grade6_Result,
                'Saff1_Result':Saff1_Result,
                'Saff2_Result':Saff2_Result,
                'Saff3_Result':Saff3_Result,
                'Saff4_Result':Saff4_Result,
                'Saff5_Result':Saff5_Result,
                'Saff6_Result':Saff6_Result,
              }
    return render(request, 'uploadresult.html', context)

@login_required(login_url='login')
@allowedUser(allowed_roles=['primary teachers', 'nursery teachers', 'islamiya teachers'])
def g1_process(request, pk):
    pupil = Pupil.objects.get(id=pk)
    Grade1_Result = Grade1_Form(instance=pupil)
    if request.method == 'POST':
        Grade1_Result = Grade1_Form(request.POST, request.FILES, instance=pupil)
        if Grade1_Result.is_valid():
            Grade1_Result.save()
            return redirect('teachers-panel')

@login_required(login_url='login')
@allowedUser(allowed_roles=['primary teachers', 'nursery teachers', 'islamiya teachers'])
def g2_process(request, pk):
    pupil = Pupil.objects.get(id=pk)
    Grade2_Result = Grade2_Form(instance=pupil)
    if request.method == 'POST':
        Grade2_Result = Grade2_Form(request.POST, request.FILES, instance=pupil)
        if Grade2_Result.is_valid():
            Grade2_Result.save()
            return redirect('teachers-panel')

@login_required(login_url='login')
@allowedUser(allowed_roles=['primary teachers', 'nursery teachers', 'islamiya teachers'])
def g3_process(request, pk):
    pupil = Pupil.objects.get(id=pk)
    Grade3_Result = Grade3_Form(instance=pupil)
    if request.method == 'POST':
        Grade3_Result = Grade3_Form(request.POST, request.FILES, instance=pupil)
        if Grade3_Result.is_valid():
            Grade3_Result.save()
            return redirect('teachers-panel')

@login_required(login_url='login')
@allowedUser(allowed_roles=['primary teachers', 'nursery teachers', 'islamiya teachers'])
def g4_process(request, pk):
    pupil = Pupil.objects.get(id=pk)
    Grade4_Result = Grade4_Form(instance=pupil)
    if request.method == 'POST':
        Grade4_Result = Grade4_Form(request.POST, request.FILES, instance=pupil)
        if Grade4_Result.is_valid():
            Grade4_Result.save()
            return redirect('teachers-panel')

@login_required(login_url='login')
@allowedUser(allowed_roles=['primary teachers', 'nursery teachers', 'islamiya teachers'])
def g5_process(request, pk):
    pupil = Pupil.objects.get(id=pk)
    Grade5_Result = Grade5_Form(instance=pupil)
    if request.method == 'POST':
        Grade5_Result = Grade5_Form(request.POST, request.FILES, instance=pupil)
        if Grade5_Result.is_valid():
            Grade5_Result.save()
            return redirect('teachers-panel')

@login_required(login_url='login')
@allowedUser(allowed_roles=['primary teachers', 'nursery teachers', 'islamiya teachers'])
def g6_process(request, pk):
    pupil = Pupil.objects.get(id=pk)
    Grade6_Result = Grade6_Form(instance=pupil)
    if request.method == 'POST':
        Grade6_Result = Grade6_Form(request.POST, request.FILES, instance=pupil)
        if Grade6_Result.is_valid():
            Grade6_Result.save()
            return redirect('teachers-panel')

@login_required(login_url='login')
@allowedUser(allowed_roles=['primary teachers', 'nursery teachers', 'islamiya teachers'])
def s1_process(request, pk):
    pupil = Pupil.objects.get(id=pk)
    Saff1_Result = Saff1_Form(instance=pupil)
    if request.method == 'POST':
        Saff1_Result = Saff1_Form(request.POST, request.FILES, instance=pupil)
        if Saff1_Result.is_valid():
            Saff1_Result.save()
            return redirect('teachers-panel')

@login_required(login_url='login')
@allowedUser(allowed_roles=['primary teachers', 'nursery teachers', 'islamiya teachers'])
def s2_process(request, pk):
    pupil = Pupil.objects.get(id=pk)
    Saff2_Result = Saff2_Form(instance=pupil)
    if request.method == 'POST':
        Saff2_Result = Saff2_Form(request.POST, request.FILES, instance=pupil)
        if Saff2_Result.is_valid():
            Saff2_Result.save()
            return redirect('teachers-panel')

@login_required(login_url='login')
@allowedUser(allowed_roles=['primary teachers', 'nursery teachers', 'islamiya teachers'])
def s3_process(request, pk):
    pupil = Pupil.objects.get(id=pk)
    Saff3_Result = Saff3_Form(instance=pupil)
    if request.method == 'POST':
        Saff3_Result = Saff3_Form(request.POST, request.FILES, instance=pupil)
        if Saff3_Result.is_valid():
            Saff3_Result.save()
            return redirect('teachers-panel')

@login_required(login_url='login')
@allowedUser(allowed_roles=['primary teachers', 'nursery teachers', 'islamiya teachers'])
def s4_process(request, pk):
    pupil = Pupil.objects.get(id=pk)
    Saff4_Result = Saff4_Form(instance=pupil)
    if request.method == 'POST':
        Saff4_Result = Saff4_Form(request.POST, request.FILES, instance=pupil)
        if Saff4_Result.is_valid():
            Saff4_Result.save()
            return redirect('teachers-panel')

@login_required(login_url='login')
@allowedUser(allowed_roles=['primary teachers', 'nursery teachers', 'islamiya teachers'])
def s5_process(request, pk):
    pupil = Pupil.objects.get(id=pk)
    Saff5_Result = Saff5_Form(instance=pupil)
    if request.method == 'POST':
        Saff5_Result = Saff5_Form(request.POST, request.FILES, instance=pupil)
        if Saff5_Result.is_valid():
            Saff5_Result.save()
            return redirect('teachers-panel')

@login_required(login_url='login')
@allowedUser(allowed_roles=['primary teachers', 'nursery teachers', 'islamiya teachers'])
def s6_process(request, pk):
    pupil = Pupil.objects.get(id=pk)
    Saff6_Result = Saff6_Form(instance=pupil)
    if request.method == 'POST':
        Saff6_Result = Saff6_Form(request.POST, request.FILES, instance=pupil)
        if Saff6_Result.is_valid():
            Saff6_Result.save()
            return redirect('teachers-panel')

@login_required(login_url='login')
@allowedUser(allowed_roles=['primary teachers', 'nursery teachers', 'islamiya teachers'])
def reportUpload(request, pk):
    pupil = Pupil.objects.get(id=pk)
    Grade1_Report = Report1_Form(instance=pupil)
    Grade2_Report = Report2_Form(instance=pupil)
    Grade3_Report = Report3_Form(instance=pupil)
    Grade4_Report = Report4_Form(instance=pupil)
    Grade5_Report = Report5_Form(instance=pupil)
    Grade6_Report = Report6_Form(instance=pupil)

    context = {
        'pupil':pupil,
        'Grade1_Report':Grade1_Report,
        'Grade2_Report':Grade2_Report,
        'Grade3_Report':Grade3_Report,
        'Grade4_Report':Grade4_Report,
        'Grade5_Report':Grade5_Report,
        'Grade6_Report':Grade6_Report,
    }
    return render(request, 'uploadreports.html', context)

@login_required(login_url='login')
@allowedUser(allowed_roles=['primary teachers', 'nursery teachers', 'islamiya teachers'])
def R1_process(request, pk):
    pupil = Pupil.objects.get(id=pk)
    Grade1_Report = Report1_Form(instance=pupil)
    if request.method == 'POST':
        Grade1_Report = Report1_Form(request.POST, request.FILES, instance=pupil)
        if Grade1_Report.is_valid():
            Grade1_Report.save()
            return redirect('teachers-panel')

@login_required(login_url='login')
@allowedUser(allowed_roles=['primary teachers', 'nursery teachers', 'islamiya teachers'])
def R2_process(request, pk):
    pupil = Pupil.objects.get(id=pk)
    Grade2_Report = Report2_Form(instance=pupil)
    if request.method == 'POST':
        Grade2_Report = Report2_Form(request.POST, request.FILES, instance=pupil)
        if Grade2_Report.is_valid():
            Grade2_Report.save()
            return redirect('teachers-panel')

@login_required(login_url='login')
@allowedUser(allowed_roles=['primary teachers', 'nursery teachers', 'islamiya teachers'])
def R3_process(request, pk):
    pupil = Pupil.objects.get(id=pk)
    Grade3_Report = Report3_Form(instance=pupil)
    if request.method == 'POST':
        Grade3_Report = Report3_Form(request.POST, request.FILES, instance=pupil)
        if Grade3_Report.is_valid():
            Grade3_Report.save()
            return redirect('teachers-panel')

@login_required(login_url='login')
@allowedUser(allowed_roles=['primary teachers', 'nursery teachers', 'islamiya teachers'])
def R4_process(request, pk):
    pupil = Pupil.objects.get(id=pk)
    Grade4_Report = Report4_Form(instance=pupil)
    if request.method == 'POST':
        Grade4_Report = Report4_Form(request.POST, request.FILES, instance=pupil)
        if Grade4_Report.is_valid():
            Grade4_Report.save()
            return redirect('teachers-panel')

@login_required(login_url='login')
@allowedUser(allowed_roles=['primary teachers', 'nursery teachers', 'islamiya teachers'])
def R5_process(request, pk):
    pupil = Pupil.objects.get(id=pk)
    Grade5_Report = Report5_Form(instance=pupil)
    if request.method == 'POST':
        Grade5_Report = Report5_Form(request.POST, request.FILES, instance=pupil)
        if Grade5_Report.is_valid():
            Grade5_Report.save()
            return redirect('teachers-panel')

@login_required(login_url='login')
@allowedUser(allowed_roles=['primary teachers', 'nursery teachers', 'islamiya teachers'])
def R6_process(request, pk):
    pupil = Pupil.objects.get(id=pk)
    Grade6_Report = Report6_Form(instance=pupil)
    if request.method == 'POST':
        Grade6_Report = Report6_Form(request.POST, request.FILES, instance=pupil)
        if Grade6_Report.is_valid():
            Grade6_Report.save()
            return redirect('teachers-panel')

@login_required(login_url='login')
@allowedUser(allowed_roles=['pupils'])
def noRecord(request):
    return HttpResponse('Record Not Available')