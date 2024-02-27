from django.db import models


class UpdatedModel(models.Model):
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CreatedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class CreatedUpdatedModel(UpdatedModel, CreatedModel):
    class Meta:
        abstract = True
