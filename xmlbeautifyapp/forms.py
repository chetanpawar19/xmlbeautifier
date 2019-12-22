from django.core import form
from xmlbeautifyapp.models import Main
#comment= forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20})

#ModelForm
class MainForm(forms.ModelForm):
    class Meta:
        model = Main
        fields = '__all__'
