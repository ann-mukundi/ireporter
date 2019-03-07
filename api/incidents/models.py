from django.db import models
import uuid
from django.contrib.auth import get_user_model


class Incident(models.Model):
    """The incident model."""

    incident_id = models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4)
    createdBy = models.ForeignKey(
        get_user_model(),
        related_name='createdBy',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None
    )
    incident_type = models.CharField(max_length=30)
    title = models.CharField(max_length=128)
    location = models.CharField(max_length=150)
    status = models.CharField(max_length=30)
    Image = models.URLField(blank=True, null=True)
    Video = models.URLField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    createdOn = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return "{} - {}".format(self.title, self.incident_id)


    class Meta:
        ordering = ["-createdOn"]