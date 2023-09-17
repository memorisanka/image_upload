from django.apps import AppConfig


class ImageUploadConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'image_upload'

    def ready(self):
        import image_upload.signals
