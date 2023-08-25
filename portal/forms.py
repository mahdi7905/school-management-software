from django.forms import ModelForm


from .models import *
from core.models import Post

class ContentCreationForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['date_created']

class PupilForm(ModelForm):
    class Meta:
        model = Pupil
        fields = '__all__'
        exclude = [
            'user', 
            'ADM_No', 
            'Conventional_Grade', 
            'Conventional_Arm', 
            'Islamiya_Grade', 
            'Islamiya_Arm',
            'First_Term_Grade_1_Result',
            'First_Term_Grade_2_Result',
            'First_Term_Grade_3_Result',
            'First_Term_Grade_4_Result',
            'First_Term_Grade_5_Result',
            'First_Term_Grade_6_Result',
            'First_Term_Grade_1_Report',
            'First_Term_Grade_2_Report',
            'First_Term_Grade_3_Report',
            'First_Term_Grade_4_Report',
            'First_Term_Grade_5_Report',
            'First_Term_Grade_6_Report',
            'First_Term_Saff_1_Result',
            'First_Term_Saff_2_Result',
            'First_Term_Saff_3_Result',
            'First_Term_Saff_4_Result',
            'First_Term_Saff_5_Result',
            'First_Term_Saff_6_Result',
            'Second_Term_Grade_1_Result',
            'Second_Term_Grade_2_Result',
            'Second_Term_Grade_3_Result',
            'Second_Term_Grade_4_Result',
            'Second_Term_Grade_5_Result',
            'Second_Term_Grade_6_Result',
            'Second_Term_Grade_1_Report',
            'Second_Term_Grade_2_Report',
            'Second_Term_Grade_3_Report',
            'Second_Term_Grade_4_Report',
            'Second_Term_Grade_5_Report',
            'Second_Term_Grade_6_Report',
            'Second_Term_Saff_1_Result',
            'Second_Term_Saff_2_Result',
            'Second_Term_Saff_3_Result',
            'Second_Term_Saff_4_Result',
            'Second_Term_Saff_5_Result',
            'Second_Term_Saff_6_Result',
            'Third_Term_Grade_1_Result',
            'Third_Term_Grade_2_Result',
            'Third_Term_Grade_3_Result',
            'Third_Term_Grade_4_Result',
            'Third_Term_Grade_5_Result',
            'Third_Term_Grade_6_Result',
            'Third_Term_Grade_1_Report',
            'Third_Term_Grade_2_Report',
            'Third_Term_Grade_3_Report',
            'Third_Term_Grade_4_Report',
            'Third_Term_Grade_5_Report',
            'Third_Term_Grade_6_Report',
            'Third_Term_Saff_1_Result',
            'Third_Term_Saff_2_Result',
            'Third_Term_Saff_3_Result',
            'Third_Term_Saff_4_Result',
            'Third_Term_Saff_5_Result',
            'Third_Term_Saff_6_Result',
            ]
class pupilConventionalUpgrade_Form(ModelForm):
    class Meta:
        model = Pupil
        fields = ['Conventional_Grade', 'Conventional_Arm']
class pupilIslamiyaUpgrade_Form(ModelForm):
    class Meta:
        model = Pupil
        fields = ['Conventional_Grade', 'Conventional_Arm']
class teacherUpgrade_Form(ModelForm):
    class Meta:
        model = Teacher
        fields = ['Grade', 'Arm', 'position']


# Conventional Result Forms
class Grade1_Form(ModelForm):
    class Meta:
        model = Pupil
        fields = ['First_Term_Grade_1_Result', 'Second_Term_Grade_1_Result', 'Third_Term_Grade_1_Result']

class Grade2_Form(ModelForm):
    class Meta:
        model = Pupil
        fields = ['First_Term_Grade_2_Result', 'Second_Term_Grade_2_Result', 'Third_Term_Grade_2_Result']

class Grade3_Form(ModelForm):
    class Meta:
        model = Pupil
        fields = ['First_Term_Grade_3_Result', 'Second_Term_Grade_3_Result', 'Third_Term_Grade_3_Result']

class Grade4_Form(ModelForm):
    class Meta:
        model = Pupil
        fields = ['First_Term_Grade_4_Result', 'Second_Term_Grade_4_Result', 'Third_Term_Grade_4_Result']

class Grade5_Form(ModelForm):
    class Meta:
        model = Pupil
        fields = ['First_Term_Grade_5_Result', 'Second_Term_Grade_5_Result', 'Third_Term_Grade_5_Result']

class Grade6_Form(ModelForm):
    class Meta:
        model = Pupil
        fields = ['First_Term_Grade_6_Result', 'Second_Term_Grade_6_Result', 'Third_Term_Grade_6_Result']


#Islamiyyah Result Forms
class Saff1_Form(ModelForm):
    class Meta:
        model = Pupil
        fields = fields = ['First_Term_Saff_1_Result', 'Second_Term_Saff_1_Result', 'Third_Term_Saff_1_Result']

class Saff2_Form(ModelForm):
    class Meta:
        model = Pupil
        fields = fields = ['First_Term_Saff_2_Result', 'Second_Term_Saff_2_Result', 'Third_Term_Saff_2_Result']

class Saff3_Form(ModelForm):
    class Meta:
        model = Pupil
        fields = fields = ['First_Term_Saff_3_Result', 'Second_Term_Saff_3_Result', 'Third_Term_Saff_3_Result']

class Saff4_Form(ModelForm):
    class Meta:
        model = Pupil
        fields = fields = ['First_Term_Saff_4_Result', 'Second_Term_Saff_4_Result', 'Third_Term_Saff_4_Result']

class Saff5_Form(ModelForm):
    class Meta:
        model = Pupil
        fields = fields = ['First_Term_Saff_5_Result', 'Second_Term_Saff_5_Result', 'Third_Term_Saff_5_Result']

class Saff6_Form(ModelForm):
    class Meta:
        model = Pupil
        fields = fields = ['First_Term_Saff_6_Result', 'Second_Term_Saff_6_Result', 'Third_Term_Saff_6_Result']


# Conventional Report Forms
class Report1_Form(ModelForm):
    class Meta:
        model = Pupil
        fields = ['First_Term_Grade_1_Report', 'Second_Term_Grade_1_Report', 'Third_Term_Grade_1_Report']

class Report2_Form(ModelForm):
    class Meta:
        model = Pupil
        fields = ['First_Term_Grade_2_Report', 'Second_Term_Grade_2_Report', 'Third_Term_Grade_2_Report']

class Report3_Form(ModelForm):
    class Meta:
        model = Pupil
        fields = ['First_Term_Grade_3_Report', 'Second_Term_Grade_3_Report', 'Third_Term_Grade_3_Report']

class Report4_Form(ModelForm):
    class Meta:
        model = Pupil
        fields = ['First_Term_Grade_4_Report', 'Second_Term_Grade_4_Report', 'Third_Term_Grade_4_Report']

class Report5_Form(ModelForm):
    class Meta:
        model = Pupil
        fields = ['First_Term_Grade_5_Report', 'Second_Term_Grade_5_Report', 'Third_Term_Grade_5_Report']

class Report6_Form(ModelForm):
    class Meta:
        model = Pupil
        fields = ['First_Term_Grade_6_Report', 'Second_Term_Grade_6_Report', 'Third_Term_Grade_6_Report']