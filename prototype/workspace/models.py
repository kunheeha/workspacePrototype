from django.db import models
from django.contrib.auth.models import User


class Workspace(models.Model):
    title = models.CharField(max_length=100)
    users = models.ManyToManyField(User)

    def __str__(self):
        return f'{self.title}, id={self.pk}'


class Folder(models.Model):
    title = models.CharField(max_length=100)
    pathname = models.CharField(max_length=100)
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE)

    def __str__(self):
        return f'folder title: {self.title}'


class Notebook(models.Model):
    title = models.CharField(max_length=100)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)

    def __str__(self):
        return f'Notebook title: {self.title}'


class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    last_edited = models.DateTimeField(auto_now=True)
    notebook = models.ForeignKey(Notebook, on_delete=models.CASCADE)

    def __str__(self):
        return f'note title: {self.title}'


class TodoItem(models.Model):
    name = models.CharField(max_length=100)
    due_date = models.DateField(null=True, blank=True)
    urgent = models.BooleanField(default=False)
    complete = models.BooleanField(default=False)
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE)

    def __str__(self):
        return f'todoname: {self.name}'
