from mongoengine import Document, StringField, DecimalField, IntField

class Coffee:
    name = StringField(required=True, )
    description = StringField(required=True)
    image = StringField(required=True)
    quantity = IntField(required=True, min_value=1)

