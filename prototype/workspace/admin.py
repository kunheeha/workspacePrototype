from django.contrib import admin
from .models import Workspace, Folder, Notebook, Note, TodoItem, File

# Register your models here.
admin.site.register(Workspace)
admin.site.register(Folder)
admin.site.register(Notebook)
admin.site.register(Note)
admin.site.register(TodoItem)
admin.site.register(File)
