from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser): 
    #This is where I would put custom fields - like fave colour, pet name etc.
    pass

    def __str__(self):
        return self.username

