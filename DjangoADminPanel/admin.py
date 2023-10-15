from django.contrib import admin
import csv
from django.http import HttpResponse
from .models import Articles, Clients, Filterwords, Notifications, Sites
from django.contrib.admin import ModelAdmin
from django.http import HttpRequest

# Admin class for the Articles model
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('id', 'article_name', 'site', 'clientid', 'article_date','insert_date')
    list_filter = ('site', 'clientid__username', 'article_date')
    search_fields = ('article_name', 'url', 'autor')

# Admin class for the Clients model
class ClientsAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'siteid', 'tts_enabled')
    list_filter = ('siteid', 'tts_enabled')
    search_fields = ('username',)

# Admin class for the Notifications model
class NotificationsAdmin(admin.ModelAdmin):
    list_display = ( 'client', 'sms', 'telegram', 'whatsapp', 'email')
    list_filter = ('client',)
    search_fields = ('client__username',)



class FilterwordsAdmin(admin.ModelAdmin):
    list_display = ('client', 'word', 'wordalias', 'subwordalias', 'stopword')


# Register models with their admin classes
admin.site.register(Articles, ArticlesAdmin)
admin.site.register(Clients, ClientsAdmin)
admin.site.register(Filterwords)
admin.site.register(Notifications, NotificationsAdmin)
admin.site.register(Sites)
