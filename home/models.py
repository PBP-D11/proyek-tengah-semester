from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.utils.translation import gettext_lazy as _
from django.dispatch import receiver #add this
from django.db.models.signals import post_save #add this

# Create your models here.
class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=12, default='-')
    is_contributor = models.BooleanField(_('contributor status'), default=False,
        help_text=_('Allow user to create news and catalog'))
    
    
class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='user')

    def __unicode__(self):
          return "%s" % (self.user) 

    @receiver(post_save, sender=CustomUser)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)