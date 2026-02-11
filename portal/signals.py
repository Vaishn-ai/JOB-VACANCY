from django.contrib.auth import get_user_model
from django.db.models.signals import post_migrate
from django.dispatch import receiver

@receiver(post_migrate)
def create_default_user(sender, **kwargs):
    User = get_user_model()

    if not User.objects.filter(username="admin").exists():
        User.objects.create_user(
            username="admin",
            email="admin@gmail.com",
            password="admin123"
        )
