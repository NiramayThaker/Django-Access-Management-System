from django.apps import AppConfig
from django.conf import settings


class MainConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "main"

    def ready(self):
        # Has to import inside so it gets load every time when function is triggered
        from django.contrib.auth.models import Group
        from django.db.models.signals import post_save

        # Will take to arguments **kwargs has user info
        def add_to_default_group(sender, **kwargs):

            user = kwargs['instance']
            if kwargs['created']:
                group, ok = Group.objects.get_or_create(name="default")
                group.user_set.add(user)

        post_save(add_to_default_group, sender=settings.AUTH_USER_MODEL)
