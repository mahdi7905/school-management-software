from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Pupil(models.Model):

    GRADES=(
        ('nursery 1', 'nursery 1'),
        ('nursery 2', 'nursery 2'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )
    
    ARMS = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    other_name = models.CharField(max_length=50, null=True, blank=True)
    ADM_No = models.CharField(max_length=50, null=True, blank=True)
    passport = models.ImageField(default='profile.jpeg', upload_to='pupil_passports')
    Conventional_Grade = models.CharField(max_length=50, choices=GRADES)
    Conventional_Arm = models.CharField(max_length=50, choices=ARMS)
    Islamiya_Grade = models.CharField(max_length=50, choices=GRADES)
    Islamiya_Arm = models.CharField(max_length=50, choices=ARMS)
    DOB = models.CharField(max_length=50)
    Gender = models.CharField(max_length=50)
    Blood_Group = models.CharField(max_length=50)
    Genotype = models.CharField(max_length=50)
    Nationality = models.CharField(max_length=50)
    State_of_Origin = models.CharField(max_length=50)
    State_of_Residence = models.CharField(max_length=50)
    LGA = models.CharField(max_length=50)
    Local_Language = models.CharField(max_length=100)
    NIN = models.CharField(max_length=50, null=True, blank=True)
    Address = models.CharField(max_length=1000)
    Dad_Title = models.CharField(max_length=50, null=True, blank=True)
    Dad_First_Name = models.CharField(max_length=50)
    Dad_Surname = models.CharField(max_length=50)
    Dad_Other_Name = models.CharField(max_length=50, null=True, blank=True)
    Dad_Occupation = models.CharField(max_length=100, null=True, blank=True)
    Dad_Home_Address = models.CharField(max_length=1000)
    Dad_Work_Address = models.CharField(max_length=1000, null=True, blank=True)
    Dad_Phone_home = models.CharField(max_length=50)
    Dad_Phone_work = models.CharField(max_length=50, null=True, blank=True)
    Dad_Email = models.EmailField(null=True, blank=True)
    Mom_Title = models.CharField(max_length=50, null=True, blank=True)
    Mom_First_Name = models.CharField(max_length=50)
    Mom_Surname = models.CharField(max_length=50)
    Mom_Other_Name = models.CharField(max_length=50, null=True, blank=True)
    Mom_Occupation = models.CharField(max_length=100, null=True, blank=True)
    Mom_Home_Address = models.CharField(max_length=1000)
    Mom_Work_Address = models.CharField(max_length=1000, null=True, blank=True)
    Mom_Phone_home = models.CharField(max_length=50)
    Mom_Phone_work = models.CharField(max_length=50, null=True, blank=True)
    Mom_Email = models.EmailField(null=True, blank=True)
    Sicknesses = models.CharField(max_length=500, null=True, blank=True)
    Disabilities = models.CharField(max_length=500, null=True, blank=True)
    Allergies = models.CharField(max_length=500, null=True, blank=True)
    Symptoms = models.CharField(max_length=500, null=True, blank=True)
    Registered_Hospoital = models.CharField(max_length=200, null=True, blank=True)
    Card_Number = models.CharField(max_length=50, null=True, blank=True)
    Hospital_Address = models.CharField(max_length=500, null=True, blank=True)
    Hospital_Phone = models.CharField(max_length=50, null=True, blank=True)
    Medical_Contact = models.CharField(max_length=50)
    Medical_Contact_Address = models.CharField(max_length=1000)
    Medical_Contact_Relationship = models.CharField(max_length=50)
    Medical_Contact_Phone = models.CharField(max_length=50)
    Medical_Emergency_Hospital = models.CharField(max_length=200, null=True, blank=True)
    Medical_Emergency_Hospital_Address = models.CharField(max_length=1000, null=True, blank=True)
    Birth_Cert = models.FileField(upload_to='pupil_attachments')
    Indigene_Cert = models.FileField(upload_to='pupil_attachments')
    Medical_Cert = models.FileField(upload_to='pupil_attachments')
    National_id = models.FileField(upload_to='pupil_attachments')

    #First Term 
    #Resuslts Conventional
    First_Term_Grade_1_Result = models.FileField(upload_to='Conventional_Grade_One', null=True, blank=True)
    First_Term_Grade_2_Result = models.FileField(upload_to='Conventional_Grade_Two', null=True, blank=True)
    First_Term_Grade_3_Result = models.FileField(upload_to='Conventional_Grade_Three', null=True, blank=True)
    First_Term_Grade_4_Result = models.FileField(upload_to='Conventional_Grade_Four', null=True, blank=True)
    First_Term_Grade_5_Result = models.FileField(upload_to='Conventional_Grade_Five', null=True, blank=True)
    First_Term_Grade_6_Result = models.FileField(upload_to='Conventional_Grade_Six', null=True, blank=True)

    #Mid-Term Reports Conventional
    First_Term_Grade_1_Report = models.FileField(upload_to='Conventional_Grade_One', null=True, blank=True)
    First_Term_Grade_2_Report = models.FileField(upload_to='Conventional_Grade_Two', null=True, blank=True)
    First_Term_Grade_3_Report = models.FileField(upload_to='Conventional_Grade_Three', null=True, blank=True)
    First_Term_Grade_4_Report = models.FileField(upload_to='Conventional_Grade_Four', null=True, blank=True)
    First_Term_Grade_5_Report = models.FileField(upload_to='Conventional_Grade_Five', null=True, blank=True)
    First_Term_Grade_6_Report = models.FileField(upload_to='Conventional_Grade_Six', null=True, blank=True)

    #Resuslts Islamiyyah
    First_Term_Saff_1_Result = models.FileField(upload_to='Conventional_Saff_One', null=True, blank=True)
    First_Term_Saff_2_Result = models.FileField(upload_to='Conventional_Saff_Two', null=True, blank=True)
    First_Term_Saff_3_Result = models.FileField(upload_to='Conventional_Saff_Three', null=True, blank=True)
    First_Term_Saff_4_Result = models.FileField(upload_to='Conventional_Saff_Four', null=True, blank=True)
    First_Term_Saff_5_Result = models.FileField(upload_to='Conventional_Saff_Five', null=True, blank=True)
    First_Term_Saff_6_Result = models.FileField(upload_to='Conventional_Saff_Six', null=True, blank=True)

    #Second Term 
    #Resuslts Conventional
    Second_Term_Grade_1_Result = models.FileField(upload_to='Conventional_Grade_One', null=True, blank=True)
    Second_Term_Grade_2_Result = models.FileField(upload_to='Conventional_Grade_Two', null=True, blank=True)
    Second_Term_Grade_3_Result = models.FileField(upload_to='Conventional_Grade_Three', null=True, blank=True)
    Second_Term_Grade_4_Result = models.FileField(upload_to='Conventional_Grade_Four', null=True, blank=True)
    Second_Term_Grade_5_Result = models.FileField(upload_to='Conventional_Grade_Five', null=True, blank=True)
    Second_Term_Grade_6_Result = models.FileField(upload_to='Conventional_Grade_Six', null=True, blank=True)

    #Mid-Term Reports Conventional
    Second_Term_Grade_1_Report = models.FileField(upload_to='Conventional_Grade_One', null=True, blank=True)
    Second_Term_Grade_2_Report = models.FileField(upload_to='Conventional_Grade_Two', null=True, blank=True)
    Second_Term_Grade_3_Report = models.FileField(upload_to='Conventional_Grade_Three', null=True, blank=True)
    Second_Term_Grade_4_Report = models.FileField(upload_to='Conventional_Grade_Four', null=True, blank=True)
    Second_Term_Grade_5_Report = models.FileField(upload_to='Conventional_Grade_Five', null=True, blank=True)
    Second_Term_Grade_6_Report = models.FileField(upload_to='Conventional_Grade_Six', null=True, blank=True)

    #Resuslts Islamiyyah
    Second_Term_Saff_1_Result = models.FileField(upload_to='Conventional_Saff_One', null=True, blank=True)
    Second_Term_Saff_2_Result = models.FileField(upload_to='Conventional_Saff_Two', null=True, blank=True)
    Second_Term_Saff_3_Result = models.FileField(upload_to='Conventional_Saff_Three', null=True, blank=True)
    Second_Term_Saff_4_Result = models.FileField(upload_to='Conventional_Saff_Four', null=True, blank=True)
    Second_Term_Saff_5_Result = models.FileField(upload_to='Conventional_Saff_Five', null=True, blank=True)
    Second_Term_Saff_6_Result = models.FileField(upload_to='Conventional_Saff_Six', null=True, blank=True)

    #Third Term 
    #Resuslts Conventional
    Third_Term_Grade_1_Result = models.FileField(upload_to='Conventional_Grade_One', null=True, blank=True)
    Third_Term_Grade_2_Result = models.FileField(upload_to='Conventional_Grade_Two', null=True, blank=True)
    Third_Term_Grade_3_Result = models.FileField(upload_to='Conventional_Grade_Three', null=True, blank=True)
    Third_Term_Grade_4_Result = models.FileField(upload_to='Conventional_Grade_Four', null=True, blank=True)
    Third_Term_Grade_5_Result = models.FileField(upload_to='Conventional_Grade_Five', null=True, blank=True)
    Third_Term_Grade_6_Result = models.FileField(upload_to='Conventional_Grade_Six', null=True, blank=True)

    #Mid-Term Reports Conventional
    Third_Term_Grade_1_Report = models.FileField(upload_to='Conventional_Grade_One', null=True, blank=True)
    Third_Term_Grade_2_Report = models.FileField(upload_to='Conventional_Grade_Two', null=True, blank=True)
    Third_Term_Grade_3_Report = models.FileField(upload_to='Conventional_Grade_Three', null=True, blank=True)
    Third_Term_Grade_4_Report = models.FileField(upload_to='Conventional_Grade_Four', null=True, blank=True)
    Third_Term_Grade_5_Report = models.FileField(upload_to='Conventional_Grade_Five', null=True, blank=True)
    Third_Term_Grade_6_Report = models.FileField(upload_to='Conventional_Grade_Six', null=True, blank=True)

    #Resuslts Islamiyyah
    Third_Term_Saff_1_Result = models.FileField(upload_to='Conventional_Saff_One', null=True, blank=True)
    Third_Term_Saff_2_Result = models.FileField(upload_to='Conventional_Saff_Two', null=True, blank=True)
    Third_Term_Saff_3_Result = models.FileField(upload_to='Conventional_Saff_Three', null=True, blank=True)
    Third_Term_Saff_4_Result = models.FileField(upload_to='Conventional_Saff_Four', null=True, blank=True)
    Third_Term_Saff_5_Result = models.FileField(upload_to='Conventional_Saff_Five', null=True, blank=True)
    Third_Term_Saff_6_Result = models.FileField(upload_to='Conventional_Saff_Six', null=True, blank=True)


    def __str__(self):
        name = self.first_name + ' ' + self.surname + ' '
        if self.other_name:
            name += self.other_name
        return name
    
class Teacher(models.Model):

    GRADES=(
        ('nursery 1', 'nursery 1'),
        ('nursery 2', 'nursery 2'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )
    
    ARMS = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
    )
    POSITION = (
        ('CONVENTIONAL TEACHER', 'CONVENTIONAL TEACHER'),
        ('NURSERY TEACHER', 'NURSERY TEACHER'),
        ('ISLAMIYA TEACHER', 'ISLAMIYA TEACHER'),
        ('PRIMARY HEAD', 'PRIMARY HEAD'),
        ('NURSERY HEAD', 'NURSERY HEAD'),
        ('ISLAMIYA HEAD', 'ISLAMIYA HEAD'),
        ('CONVENTIONAL HEAD', 'CONVENTIONAL HEAD'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    other_name = models.CharField(max_length=50, blank=True, null=True)
    position = models.CharField(max_length=50, choices=POSITION)
    Grade = models.CharField(max_length=50, blank=True, null=True, choices=GRADES)
    Arm = models.CharField(max_length=50, blank=True, null=True, choices=ARMS)
    Phone = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        name = self.first_name + ' ' + self.surname
        return name


