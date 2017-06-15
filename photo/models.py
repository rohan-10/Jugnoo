from django.db import models

class Asset(models.Model):

    key = models.CharField(max_length=8, unique=True, editable=False)
    name = models.CharField(('name'), max_length=200)
    source = models.FileField(('file'), upload_to=upload_to, storage=default_storage)

    ext = models.CharField(max_length=15, editable=False)
    type = models.PositiveIntegerField(choices=ASSET_TYPE, max_length=15, editable=False)
    size = models.PositiveIntegerField(max_length=32, default=0, editable=False)

    _file_meta = models.TextField(editable=False, null=True, blank=True)

    public = models.BooleanField(default=False)
    position = models.PositiveIntegerField(default=1)

    object_id = models.PositiveIntegerField(default=1)
    content_type = models.ForeignKey(ContentType, blank=True, null=True)
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True, auto_now=True)
