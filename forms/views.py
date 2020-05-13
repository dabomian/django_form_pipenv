from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy

from .forms import Form1


class Home(TemplateView):
    template_name = 'forms/home.html'


class Form1View(FormView):
    template_name = 'forms/form1.html'
    form_class = Form1
    success_url = reverse_lazy('forms:form1')

    def form_valid(self, form):
        context = self.get_context_data()
        #context['form'] = form # this is not necessery becaues of cruspty form ?
        data = self.request.POST
        print(form) 
        print('******************')
        print(data)
        return self.render_to_response(context)




