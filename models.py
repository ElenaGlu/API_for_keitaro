from tortoise import fields
from tortoise.models import Model


class AffiliateNetwork(Model):
    name = fields.CharField(max_length=256, unique=True)
    postback_url = fields.CharField(max_length=256)
    offer_param = fields.CharField(max_length=256)
    keitaro_id = fields.IntField(null=True)


class Offer(Model):
    name = fields.CharField(max_length=256, unique=True)
    affiliate_network = fields.ForeignKeyField('models.AffiliateNetwork', related_name='AffiliateNetwork')
    offer_type = fields.CharField(max_length=256, default='local')
    action_payload = fields.CharField(max_length=256)
    keitaro_id = fields.IntField(null=True)
