from django.forms import Form, IntegerField


class MarkAsRead(Form):
    post_id = IntegerField()
