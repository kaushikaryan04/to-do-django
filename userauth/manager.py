from django.contrib.auth.base_user import BaseUserManager
# from .models import *


class UserManager(BaseUserManager):
    
    def create_user(self , email , password , username , name , **otherfields ):
        if not email:
            raise ValueError("email is not given")
        email = self.normalize_email(email)
        user = self.model(email = email , username = username ,name = name , **otherfields )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self ,email ,password , username,name , **otherfield):
        #this will change the defalut from false to true 
        otherfield.setdefault("is_staff" , True)
        otherfield.setdefault("is_superuser" , True)
        otherfield.setdefault("is_active" , True)
        # but still if the user gives false for is staff or super user then raise a error
        if otherfield.get("is_staff") is False:
            raise ValueError("is staff must be true")
        if otherfield.get("is_superuser") is False:
            raise ValueError("superuser status must be true")
        return self.create_user(email , password , username,name , **otherfield)

        