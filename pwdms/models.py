from django.contrib.auth import get_user_model
from django.db import models

from .utils import PwdCrypto

crypto_store = PwdCrypto()

# Create your models here.
user = get_user_model()


class PassStore(models.Model):
    """Model for storing passwords for websites"""
    website_name = models.CharField(max_length=128)
    website_url = models.URLField(max_length=256)
    creator = models.ForeignKey(user, on_delete=models.CASCADE)
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def decrypt_password(self):
        """Decrypt password using cryptography"""
        return crypto_store.decrypt(self.password)

