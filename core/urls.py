from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name="homepage"),
    path('vacancy', views.vacancy, name="vacancy"),
    path('exam-time-table', views.examTable, name="exam-time-table"),
    path('test-time-table', views.testTable, name="test-time-table"),
    path('meal-table', views.mealTable, name="meal-table"),
    path('tables', views.tables, name="tables"),
    path('term-calendar', views.termCalendar, name="term-calendar"),
    path('admission', views.admission, name="admission"),
    path('our-programmes', views.ourProgrammes, name="our-programmes"),
    path('job-application', views.jobApplication, name="job-application"),
    path('congrats', views.congrats, name="congrats"),

]