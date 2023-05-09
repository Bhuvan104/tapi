from django.forms import ModelForm
from polls.models import Person
class ContactForm(ModelForm):
   class Meta:
      model = Person
      fields = ['first_name','last_name','email_address','password','cpassword']

   
