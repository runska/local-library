from django.contrib import admin
from catalog.models import Author, Genre, Book, BookInstance, Language

admin.site.register(Book)
admin.site.register(Language)
admin.site.register(Author)
admin.site.register(Genre)

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
  """Administration object for BookInstance models.
  Defines:
  - fields to be displayed in list view (list_display)
  - filters that will be displayed in sidebar (list_filter)
  - grouping of fields into sections (fieldsets)
  """
  list_display = ('book', 'status', 'borrower', 'due_back', 'id')
  list_filter = ('status', 'due_back')

  fieldsets = (
    (None, {
    'fields': ('book','imprint', 'id')
    }),
    ('Availability', {
    'fields': ('status', 'due_back','borrower')
    }),
  )

