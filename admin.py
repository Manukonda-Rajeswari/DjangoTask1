from django.contrib import admin
from.models import Conversation


@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_user', 'get_created_at')

    def get_user(self, obj):
        return obj.user.username

    def get_created_at(self, obj):
        return obj.created_at

    get_user.short_description = 'User'
    get_created_at.short_description = 'Created At'
