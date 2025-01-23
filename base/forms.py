from django import forms
from agency.models import Post, EmergencyReport

class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

class EmergencyForm(forms.ModelForm):
    class Meta:
        model = EmergencyReport
        fields = ['name', 'phone_number', 'emergency_type', 'number_of_people']

    name = forms.CharField(max_length=100)
    phone_number = forms.CharField(max_length=20)
    emergency_type = forms.ChoiceField(choices=[
        ('medical', 'Medical'),
        ('fire', 'Fire'),
        ('earthquake', 'Earthquake'),
        ('flood', 'Flood'),
        ('other', 'Other')
    ])
    number_of_people = forms.IntegerField()