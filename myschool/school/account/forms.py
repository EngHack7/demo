from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Account , TeacherNotes
from django.contrib.auth import authenticate

class NoteForm(forms.ModelForm):
    class Meta:
        model = TeacherNotes
        fields  = ('is_read' , 'teacher_id','note' , 'date' , 'student_id')
           
        

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60 , help_text="Requierd , Add Valid Email")

    class Meta:
        model = Account
        fields = ('email' , 'password1' , 'password2' )


class AccountAuthenticationForm(forms.ModelForm):

    # the_id_number = forms.IntegerField(label='the_id_number', widget=forms.TextInput)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('the_id_number', 'password')

    def clean(self):
        if self.is_valid():
            the_id_number = self.cleaned_data['the_id_number']
            password = self.cleaned_data['password']
            print(the_id_number,password)
            if not authenticate(the_id_number=the_id_number, password=password):
                print("authenticated reject")
                raise forms.ValidationError("Invalid login")
            #i'll try to delete db and makemigrations again 


