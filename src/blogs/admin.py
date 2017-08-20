from django.contrib import admin

# Register your models here.
from .models import Post


class PostAdminModels(admin.ModelAdmin):
    """This class is to update the shown thing on the django admin page of the web application"""
    # which field to display
    list_display = ["title", "postupdate", "posttime", "id"]

    # to change the field of links...so now on the table in the admin page
    # updated time "postupdate" would be clickable instead of title
    # list_display_links = ["postupdate"]

    # filter list will be displayed on the right
    list_filter = ["title", "postupdate"]

    search_fields = ["title"]
    # check other options in django's documentations

    class Meta:
        model = Post


admin.site.register(Post, PostAdminModels)
