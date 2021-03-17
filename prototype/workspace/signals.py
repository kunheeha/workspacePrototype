from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Workspace, TodoList


@receiver(post_save, sender=Workspace)
def create_todolist(sender, instance, created, **kwargs):
    if created:
        TodoList.objects.create(workspace=instance)


@receiver(post_save, sender=Workspace)
def save_todolist(sender, instance, **kwargs):
    instance.todolist.save()
