from django.db import models
from apps.my_users.models import User

class Message(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    writer = models.ForeignKey(User, related_name="messages")

    def __repr__(self):
        return f" msg: {self.message}, create_date: {self.created_at}, update_date: {self.updated_at}, msg_from: {self.writer}"


class Comment(models.Model):
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Message, related_name="comments")
    users = models.ForeignKey(User, related_name="comments")

    def __repr__(self):
        return f" comment: {self.comment}, created: {self.created_at}, updated: {self.updated_at}, comm_on: {self.post}, by: {self.users}"