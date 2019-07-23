#1. catalog/admin.py 추가
#2. cmd 에서 python manage.py createsuperuser id : admin, password : 1234
#3. blog.naver.com/ocx2hex 에서 models.py 다운 받아서 locallibrary/catalog/models.py적용
#4. 적용 후에 cmd에서 python manage.py makemigrations -> python manage.py migrate
from django.contrib import admin
from catalog.models import Author, Genre, Book, BookInstance

#admin.site.register(Book)
#admin.site.register(Author)
admin.site.register(Genre)
#admin.site.register(BookInstance)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name','last_name',('date_of_birth','date_of_death')]
admin.site.register(Author, AuthorAdmin)

class BooksInstanceInline(admin.TabularInline):
    model =  BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book','status','borrower','due_back','id')
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields':('book','imprint','id')
        }),
        ('Availability',{
            'fields':('status','due_back','borrower')
        }),

    )


