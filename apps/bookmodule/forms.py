from apps.bookmodule import models
from django import forms
from .models import Address

class BookForm(forms.ModelForm):
    class Meta: 
        model = models.Book 
        fields = ['title', 'price', 'edition', 'author']

        title = forms.CharField(
            max_length=100,
            required=True,
            label="Title",
            widget= forms.TextInput( attrs= {
                'placeholder':'',
                'class':"mycssclass",
                'id':'jsID'
            })
        ) 
        price = forms.DecimalField(
            required=True,
            label="Price",
            initial=0
        )        
        edition = forms.IntegerField(
        required=True,
        initial=0,
        widget=forms.NumberInput()
        )
        author = forms.CharField(
            max_length=100,
            required=True,
            label="Author",
            widget= forms.TextInput( attrs= {
                'placeholder':'',
                'class':"mycssclass",
                'id':'jsID'
            })
        )  

class StudentForm(forms.ModelForm):
    class Meta: 
        model = models.Student 
        fields = ['name', 'age', 'address']

        name = forms.CharField(
            max_length=100,
            required=True,
            label="Name",
            widget= forms.TextInput( attrs= {
                'placeholder':'',
                'class':"mycssclass",
                'id':'jsID'
            })
        )      
        age = forms.IntegerField(
            label='Age',
            required=True,
            initial=0,
            widget=forms.NumberInput()
        )
        address = forms.ModelChoiceField(
            queryset=Address.objects.all(),
            
            required=True,
            label="Address",
            widget= forms.Select( attrs= {
                'placeholder':'',
                'class':"mycssclass",
                'id':'addressID'
            })
        )  

class StudentForm2(forms.ModelForm):
    class Meta: 
        model = models.Student3 
        fields = ['name', 'age', 'address']

        name = forms.CharField(
            max_length=100,
            required=True,
            label="Name",
            widget= forms.TextInput( attrs= {
                'placeholder':'',
                'class':"mycssclass",
                'id':'jsID'
            })
        )      
        age = forms.IntegerField(
            label='Age',
            required=True,
            initial=0,
            widget=forms.NumberInput()
        )
        address = forms.ModelMultipleChoiceField(
            queryset=Address.objects.all(),
            required=True,
            label="Address",
            widget= forms.SelectMultiple( attrs= {
                'placeholder':'',
                'class':"mycssclass",
                'id':'addressID'
            })
        )  


from .models import Food

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['name','image']