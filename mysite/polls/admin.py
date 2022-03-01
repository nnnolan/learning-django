from django.contrib import admin

from .models import Choice, Question


class ChoiceInline(admin.TabularInline): 
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin): #registers question model in admin
    fieldsets = [
        (None,               {'fields': ['question_text']}), #sets question_text as the only field
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}), #sets pub_date as the only field
    ]
    inlines = [ChoiceInline]

    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    
admin.site.register(Question, QuestionAdmin)