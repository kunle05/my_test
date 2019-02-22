from __future__ import unicode_literals
from django.db import models
from datetime import datetime

import re

class UserManager(models.Manager):
    def reg_validator(self, postData):
        errors = {}

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        if len(postData['email']) == 0:
            errors["email"] = "Email cannot be empty"
        else:
            if not EMAIL_REGEX.match(postData['email']):
                errors["email"] = "Invalid email address"

        if len(postData['password']) < 8:
            errors["password"] = "Password must be at least 8 characters"
        else:
            if postData['password'] != postData['pw_conf']:
                errors["pword"] = "Passwords does not match"
        
        if len(postData['f_name']) < 2:
            errors["fname"] = "Name should be at least 2 characters"

        if len(postData['l_name']) < 2:
            errors["lname"] = "Last name should be at least 2 characters"

        if len(postData['dob']) == 0:
            errors["date"] = "Please enter a date"
        else:
            birth_day = datetime.strptime(postData['dob'], "%Y-%m-%d")
            today = datetime.today() 
            if birth_day > today:
                errors["date"] = "Date cannot be in the future"

            else:
                age = (today - birth_day).days/365
                if age < 13:
                    errors["date"] = "User must be 13 years or older"
     
        return errors

    def login_validator(self, postData):

        errors = {}

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        if len(postData['user_email']) == 0:
            errors["mail"] = "Enter a valid email"
        else:
            if not EMAIL_REGEX.match(postData['user_email']):
                errors["mail"] = "Invalid email address"

        if len(postData['user_password']) < 8:
            errors["pw_word"] = "Password must be at least 8 characters"

        return errors



class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    birthdate = models.DateField()
    objects = UserManager()

    def __repr__(self):
        return f" fn: {self.first_name}, ln: {self.last_name}, email: {self.email}, p_word: {self.password}, birthday: {self.birthdate}"