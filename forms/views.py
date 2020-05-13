from django.views.generic.edit import FormView
from .forms import Form1

class Form1View(FormView):
    template_name = 'forms/form1.html'
    form_class = Form1




