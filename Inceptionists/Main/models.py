from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Addresses(models.Model):
    addressid = models.AutoField(db_column='addressID', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('Users', db_column='userID')  # Field name made lowercase.
    name = models.CharField(max_length=255)
    phone = models.DecimalField(max_digits=11, decimal_places=0, blank=True, null=True)
    streetaddr = models.CharField(db_column='streetAddr', max_length=255)  # Field name made lowercase.
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    zip = models.DecimalField(max_digits=5, decimal_places=0)
    zip_ext = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'addresses'

class Users(models.Model):
    userid = models.AutoField(db_column='userID', primary_key=True)  # Field name made lowercase.
    user_type = models.CharField(max_length=6)
    name = models.CharField(max_length=255)
    birthdate = models.DateTimeField()
    email = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'users'

class Auctions(models.Model):
    auctioneerid = models.ForeignKey('Users', db_column='auctioneerID')  # Field name made lowercase.
    itemid = models.ForeignKey('Items', db_column='itemID')  # Field name made lowercase.
    description = models.CharField(max_length=2000)
    reserve_price = models.DecimalField(max_digits=6, decimal_places=2)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'auctions'


class Bids(models.Model):
    bidderid = models.IntegerField(db_column='bidderID')  # Field name made lowercase.
    auctioneerid = models.ForeignKey(Auctions, db_column='auctioneerID', related_name='bid_auctioneerid')  # Field name made lowercase.
    itemid = models.IntegerField(db_column='itemID')  # Field name made lowercase.
    auction_start = models.ForeignKey(Auctions, db_column='auction_start', related_name='bid_start_time')
    timestamp = models.DateTimeField()
    amount = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bids'

class Categories(models.Model):
    name = models.CharField(primary_key=True, max_length=30)
    description = models.CharField(max_length=2000, blank=True, null=True)
    parent = models.ForeignKey('self', db_column='parent', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categories'

    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Categories, self).save(*args, **kwargs)

    def __unicode__(self):      #For Python 2, use __str__ on Python 3
        return self.name

class Creditcards(models.Model):
    userid = models.ForeignKey('Users', db_column='userID')  # Field name made lowercase.
    ccv = models.IntegerField()
    addressid = models.ForeignKey(Addresses, db_column='addressID')  # Field name made lowercase.
    merchant = models.CharField(max_length=20)
    ccnumber = models.DecimalField(db_column='ccNumber', primary_key=True, max_digits=16, decimal_places=0)  # Field name made lowercase.
    exp_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'creditcards'

class Items(models.Model):
    itemid = models.AutoField(db_column='itemID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Categories, db_column='category')

    class Meta:
        managed = False
        db_table = 'items'

class Ratings(models.Model):
    seller_userid = models.ForeignKey('Transactions', db_column='seller_userID', related_name='ratings_sellerid')  # Field name made lowercase.
    buyer_userid = models.ForeignKey('Transactions', db_column='buyer_userID', related_name='ratings_buyerid')  # Field name made lowercase.
    timestamp = models.ForeignKey('Transactions', db_column='timestamp', related_name='ratings_timestamp')
    itemid = models.ForeignKey('Transactions', db_column='itemID',related_name='ratings_itemid')  # Field name made lowercase.
    subject = models.CharField(max_length=255)
    rating = models.IntegerField()
    content = models.CharField(max_length=2000)

    class Meta:
        managed = False
        db_table = 'ratings'

class Reviews(models.Model):
    itemid = models.ForeignKey(Items, db_column='itemID',related_name='review_itemid')  # Field name made lowercase.
    author_userid = models.ForeignKey('Users', db_column='author_userID',related_name='review_userid')  # Field name made lowercase.
    rating = models.IntegerField()
    content = models.CharField(max_length=2000)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'reviews'

class Sells(models.Model):
    itemid = models.ForeignKey(Items, db_column='itemID',related_name='sells_itemid')  # Field name made lowercase.
    sellerid = models.ForeignKey('Users', db_column='sellerID',related_name='sellerid')  # Field name made lowercase.
    description = models.CharField(max_length=2000)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'sells'

class Transactions(models.Model):
    seller_userid = models.ForeignKey('Users', db_column='seller_userID',related_name='transactions_sellerid')  # Field name made lowercase.
    buyer_userid = models.ForeignKey('Users', db_column='buyer_userID',related_name='transactions_buyerid')  # Field name made lowercase.
    timestamp = models.DateTimeField()
    itemid = models.ForeignKey(Items, db_column='itemID',related_name='transactions_itemid')  # Field name made lowercase.
    itemct = models.IntegerField(db_column='itemCt')  # Field name made lowercase.
    carrier_trackingnum = models.CharField(db_column='carrier_trackingNum', max_length=255, blank=True, null=True)  # Field name made lowercase.
    saleprice = models.DecimalField(db_column='salePrice', max_digits=6, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'transactions'

        #unique_together = (('seller_userID', 'buyer_userID', 'itemID', 'timestamp'))
        #unique_together = (('transactions_sellerid', 'transactions_buyerid', 'transactions_itemid', 'timestamp'))

class Vendors(models.Model):
    userid = models.ForeignKey(Users, db_column='userID', primary_key=True,related_name='vendors_userid')  # Field name made lowercase.
    user_type = models.ForeignKey(Users, db_column='user_type')
    company_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'vendors'


class Page(models.Model):
    category = models.ForeignKey(Categories)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __unicode__(self):      #For Python 2, use __str__ on Python 3
        return self.title