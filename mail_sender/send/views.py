from email import message
from django.conf import settings
from django.dispatch import receiver
from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.core.mail import EmailMessage
from .forms import SendEmailForm



class CustomLoginView(LoginView):
    template_name = 'send/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('index')

class RegisterPage(FormView):
    template_name = 'send/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
            
        return super(RegisterPage, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('index')    
        return super(RegisterPage, self).get(*args, **kwargs)

@login_required()
def index(request):
    if request.method == 'POST':
        form = SendEmailForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            receiver_name = form.cleaned_data['receiver_name']
            subject = f'{receiver_name}, ' + form.cleaned_data['subject']
            message = form.cleaned_data['message']
            receiver_email = form.cleaned_data['receiver_email']
            file = form.cleaned_data['file']
            email = EmailMessage(
                subject,
                message,
                '200103323@stu.sdu.edu.kz',
                ['sirab65763@svcache.com', receiver_email]
            )
            email.attach(file.name, file.read(), file.content_type)
            email.send()
            return redirect('index') 

    else:
        form = SendEmailForm()
    return render(request, 'send/index.html', {'form': form})


