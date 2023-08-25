from django.db import models

# Create your models here.



#Teaching Application Model
class Application(models.Model):
    First_Name = models.CharField(max_length=50)
    Surname = models.CharField(max_length=50)
    Other_Name = models.CharField(max_length=50, blank=True, null=True)
    Gender = models.CharField(max_length=50)
    Nationality = models.CharField(max_length=50)
    State_of_Origin = models.CharField(max_length=50)
    State_of_residence = models.CharField(max_length=50)
    Address = models.CharField(max_length=500)
    Phone_Number = models.CharField(max_length=50)
    Email = models.EmailField()
    DOB = models.CharField(max_length=50)
    Marital_Status = models.CharField(max_length=50)
    Qualification = models.CharField(max_length=50)
    Field_of_Study = models.CharField(max_length=50)
    Course_of_study = models.CharField(max_length=50)
    CV = models.FileField(upload_to='docs')
    Application_letter = models.FileField(upload_to='docs')
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        name = self.First_Name + ' ' + self.Surname
        return name

#Content-Creation Model
class Post(models.Model):
    Headline = models.CharField(max_length=1000)
    Content = models.TextField(max_length=10000)
    Image = models.ImageField(upload_to='contentImages', null= True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Headline
