from django.urls import path
from . import views


urlpatterns = [
    path('', views.emptypage, name="portal"),
    path('login', views.loginpage, name="login"),
    path('logout', views.logoutpage, name="logout"),
    path('content-creator', views.contentCreator, name="contentCreator"),
    path('create-post', views.creatPost, name="create-post"),
    path('edit-post/<str:pk>', views.editPost, name="edit-post"),
    path('delete-post/<str:pk>', views.deletePost, name="delete-post"),
    path('kia-admin', views.kiaAdmin, name="kia-admin"),
    path('teacher-reg', views.teacherReg, name="teacher-reg"),
    path('pupil-reg', views.pupilReg, name="pupil-reg"),
    path('update-pupil/<str:pk>', views.updatePupil, name="update-pupil"),
    path('applications', views.applications, name="applications"),
    path('view-application/<str:pk>', views.viewApplication, name="view-application"),
    path('delete-application/<str:pk>', views.deleteApplication, name="delete-application"),
    path('details/<str:pk>', views.details, name="details"),
    path('medical-emergency/<str:pk>', views.medicalEmergency, name="medical-emergency"),
    path('kia-head-teacher', views.kiaHead, name="kia-head-teacher"),
    path('islamiya-head', views.islamiyaHead, name="islamiya-head"),
    path('kia-sectional-head', views.sectionalHead, name="sectional-head"),
    path('teachers', views.Teachers, name="teachers"),
    path('update-pupils-grade', views.pupilGradeUpdate, name="pupil-upgrade"),
    path('update-teachers-grade/<str:pk>', views.teacherGradeUpdate, name="teacher-upgrade"),
    path('dashboard', views.pupilPanel, name="dashboard"),
    path('admission-letter', views.admissionLetter, name="admission-letter"),
    path('attachments', views.attachments, name="attachments"),
    path('results', views.results, name="result"),
    path('reports', views.reports, name="report"),
    path('page', views.page, name="page"),
    path('teachers-panel', views.teacherPanel, name="teachers-panel"),
    path('result-upload/<str:pk>', views.resultUpload, name="result-upload"),
    path('process-result1/<str:pk>', views.g1_process, name="process-result1"),
    path('process-result2/<str:pk>', views.g2_process, name="process-result2"),
    path('process-result3/<str:pk>', views.g3_process, name="process-result3"),
    path('process-result4/<str:pk>', views.g4_process, name="process-result4"),
    path('process-result5/<str:pk>', views.g5_process, name="process-result5"),
    path('process-result6/<str:pk>', views.g6_process, name="process-result6"),
    path('process-saff1/<str:pk>', views.s1_process, name="process-saff1"),
    path('process-saff2/<str:pk>', views.s2_process, name="process-saff2"),
    path('process-saff3/<str:pk>', views.s3_process, name="process-saff3"),
    path('process-saff4/<str:pk>', views.s4_process, name="process-saff4"),
    path('process-saff5/<str:pk>', views.s5_process, name="process-saff5"),
    path('process-saff6/<str:pk>', views.s6_process, name="process-saff6"),
    path('report-upload/<str:pk>', views.reportUpload, name="report-upload"),
    path('process-report1/<str:pk>', views.R1_process, name="process-report1"),
    path('process-report2/<str:pk>', views.R2_process, name="process-report2"),
    path('process-report3/<str:pk>', views.R3_process, name="process-report3"),
    path('process-report4/<str:pk>', views.R4_process, name="process-report4"),
    path('process-report5/<str:pk>', views.R5_process, name="process-report5"),
    path('process-report6/<str:pk>', views.R6_process, name="process-report6"),
    path('not-available', views.noRecord, name="no-record"),

]
    