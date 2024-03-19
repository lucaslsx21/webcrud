from django.forms import ModelForm
from app.models import Person

# Create the form class.
class PersonForm(ModelForm):
     class Meta:
         model = Person
         fields = ["nome", "telefone", "data_nascimento", "email"]