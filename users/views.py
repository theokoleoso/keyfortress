from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, ListView
from django.urls import reverse_lazy, reverse
from allauth.account.views import SignupView, LoginView, PasswordResetView, PasswordChangeView, _ajax_response

from users.forms import CustomUserChangeForm


# Create your views here
class MySignupView(SignupView):
    success_url = reverse_lazy('login')
    template_name = 'account/signup.html'


class MyLoginView(LoginView):
    template_name = 'account/login.html'


class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'account/password_change.html'
    success_url = reverse_lazy('password_change_done')

# Get form for view, validate form, and respond with success URL or error response
    def post(self):
        # get form class for view
        form_class = self.get_form_class()
        # instance for above form class
        form = self.get_form(form_class)  # User form data
        if form.is_valid():
            response = self.form_valid(form)
        else:
            response = self.form_invalid(form)
        return _ajax_response(
            self.request, response, form=form, data=self._get_ajax_data_if()  # Provide feedback without a refresh
        )


class CustomPasswordChangeDoneView(TemplateView):
    template_name = 'account/password_change_done.html'


class Profile(LoginRequiredMixin, TemplateView):
    context_object_name = 'data'
    template_name = 'profile.html'

# Shows users current details on the profile page
    def get_context_data(self):
        context = super().get_context_data()
        context['form'] = CustomUserChangeForm(instance=self.request.user)
        return context

# If form is valid updated data saved, if not valid form errors display
    def post(self, request):
        # Takes user input saves it if the form is valid
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('profile'))


class Tips(TemplateView):
    template_name = "tips.html"


class About(TemplateView):
    template_name = "about.html"
