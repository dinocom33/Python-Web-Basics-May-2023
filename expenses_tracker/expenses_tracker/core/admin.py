from django.contrib import admin

from expenses_tracker.core.models import Profile, Expense


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'budget')
    list_filter = ('first_name', 'last_name', 'budget')
    search_fields = ('first_name', 'last_name', 'budget')


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('titles', 'price', 'description')
    list_filter = ('titles', 'price')
    search_fields = ('titles', 'price')
