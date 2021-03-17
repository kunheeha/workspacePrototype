from django.db import models
from django.contrib.auth.models import User


class Workspace(models.Model):
    title = models.CharField(max_length=100)
    users = models.ManyToManyField(User)


class Folder(models.Model):
    title = models.CharField(max_length=100)
    pathname = models.CharField(max_length=100)
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE)


class Notebook(models.Model):
    title = models.CharField(max_length=100)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)


class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    last_edited = models.DateTimeField(auto_now=True)
    notebook = models.ForeignKey(Notebook, on_delete=models.CASCADE)


class TodoList(models.Model):
    workspace = models.OneToOneField(Workspace, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super(TodoList, self).save(*args, **kwargs)


class TodoItem(models.Model):
    name = models.CharField(max_length=100)
    due_date = models.DateField(null=True, blank=True)
    importance = models.CharField(max_length=1)
    todolist = models.ForeignKey(TodoList, on_delete=models.CASCADE)
