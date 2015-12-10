from django.contrib import admin
from Main.models import Categories, Page, Addresses, Auctions, Bids, Creditcards, Items, Ratings, Reviews, Sells, Transactions, Users, Vendors

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

# Register your models here.
admin.site.register(Addresses)
admin.site.register(Auctions)
admin.site.register(Bids)
admin.site.register(Creditcards)
admin.site.register(Items)
admin.site.register(Ratings)
admin.site.register(Reviews)
admin.site.register(Sells)
admin.site.register(Transactions)
admin.site.register(Users)
admin.site.register(Vendors)
admin.site.register(Categories,CategoryAdmin)
admin.site.register(Page)