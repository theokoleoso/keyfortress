# views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, HttpResponse
from django.views.generic import ListView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import PassStore
from .utils import PwdCrypto
import csv


crypto_store = PwdCrypto()


class PassListView(LoginRequiredMixin, ListView):
    """View for listing passwords for websites"""
    model = PassStore
    template_name = "pwdstore/pass_list.html"
    context_object_name = "pass_list"

    # add filter by creator who is authenticated
    def get_queryset(self):
        return PassStore.objects.filter(creator=self.request.user)
    


class PassCreateView(CreateView, LoginRequiredMixin):
    """View for adding a new password for a website"""
    model = PassStore
    template_name = "pwdstore/pass_forms.html"
    fields = ["website_name", "website_url", "username", "password"]
    success_url = reverse_lazy("pass_list")

    def form_valid(self, form):
        # Set user who created password as user logged in
        form.instance.creator = self.request.user
        # Encrypt password value on form
        form.instance.password = crypto_store.encrypt(form.cleaned_data["password"])
        # Save form and redirect to success_url
        return super().form_valid(form)


class PassDeleteView(DeleteView, LoginRequiredMixin):
    """View for deleting a password for a website"""
    model = PassStore
    template_name = "pwdstore/pass_confirm_delete.html"
    success_url = reverse_lazy("pass_list")


def get_decrypted_password(request):
    """Decrypt password using cryptography"""
    password = request.GET.get("password")

    # decrypt password and return in JSON form
    decrypted_password = crypto_store.decrypt(password)
    return JsonResponse({"decrypted_password": decrypted_password})
