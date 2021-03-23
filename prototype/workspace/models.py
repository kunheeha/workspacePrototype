from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Workspace(models.Model):
    title = models.CharField(max_length=100)
    users = models.ManyToManyField(User)

    def __str__(self):
        return f'{self.title}, id={self.pk}'


def user_directory_path(instance, filename):
    return f'folder_{instance.folder.id}/{filename}'


class Folder(models.Model):
    title = models.CharField(max_length=100)
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE)

    def __str__(self):
        return f'folder title: {self.title}'


class File(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=100)
    filename = models.FileField(upload_to=user_directory_path)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)

    def __str__(self):
        return f'file name: {self.name}'

    def delete(self, *args, **kwargs):
        self.filename.delete()
        super().delete(*args, **kwargs)


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

    def get_absolute_url(self):
        return reverse('notebook', kwargs={'workspaceid': self.notebook.folder.workspace.id, 'notebookid': self.notebook.id})


class TodoItem(models.Model):
    name = models.CharField(max_length=100)
    due_date = models.DateField(null=True, blank=True)
    urgent = models.BooleanField(default=False)
    complete = models.BooleanField(default=False)
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE)

    def __str__(self):
        return f'todoname: {self.name}'
