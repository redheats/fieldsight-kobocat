from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from onadata.apps.fsforms.models import FieldSightXF, FInstance
from onadata.apps.users.models import UserProfile
from onadata.apps.fieldsight.models import Site


class FieldSightLog(models.Model):
    ACTION_TYPES = (
        (0, 'USER'),
        (1, 'FORM'),
        (2, 'SUBMISSION'),
        (3, 'Site'),
    )
    type = models.IntegerField(default=0, choices=ACTION_TYPES)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(UserProfile, related_name="log", null=True)
    form = models.ForeignKey(FieldSightXF, related_name="log", null=True)
    instance = models.ForeignKey(FInstance, related_name="log", null=True)
    site = models.ForeignKey(Site, related_name="log", null=True)
    is_seen = models.BooleanField(default=False)
    source = models.ForeignKey(User, related_name='log', null=True)

    class Meta:
        get_latest_by = "date"
        ordering = ["-date", "type"]
