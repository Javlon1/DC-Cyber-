from django.db import models


class Info(models.Model):
    logo = models.ImageField(upload_to='logo/')
    t_link = models.CharField(max_length=255)
    f_link = models.CharField(max_length=255)
    i_link = models.CharField(max_length=255)
    y_link = models.CharField(max_length=255)


class Blog(models.Model):
    image = models.ImageField(upload_to='blog/')
    title = models.CharField(max_length=255)
    text = models.TextField()


class Photo(models.Model):
    photo = models.ImageField()

  
class Numbers(models.Model):
    text = models.CharField(max_length=25)
    number = models.IntegerField()


class Emails(models.Model):
    email = models.EmailField()


class Game(models.Model):
    name = models.CharField(max_length=255, unique=True)
    players = models.PositiveIntegerField(default=1)
    team_quantity = models.IntegerField()
    registrations = models.IntegerField(default=0)
    is_started = models.BooleanField(default=False)
    full = models.BooleanField(default=False)
    
    def str(self) -> str:
        return self.name


class User(models.Model):
    player_type = models.IntegerField(
        choices=(
            (1, 'one player'),
            (2, 'team'),
        ))
    name = models.CharField(max_length=255, unique=True)
    surname = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField()
    game = models.ForeignKey(Game, on_delete=models.PROTECT)
    phone = models.IntegerField()
    experience_from = models.IntegerField()
    experience_to = models.IntegerField()
    team_member = models.IntegerField(default=1)
    img = models.ImageField(upload_to="Users/")
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name


class Competition(models.Model):
    game = models.ForeignKey(Game, on_delete=models.PROTECT)
    user1 = models.ForeignKey(User, on_delete=models.PROTECT, related_name="user_1")
    user2 = models.ForeignKey(User, on_delete=models.PROTECT)
    data = models.DateTimeField()
    active = models.BooleanField(default=True)


class Champions(models.Model):
    game = models.ForeignKey(Game, on_delete=models.PROTECT)
    one = models.ForeignKey(User, on_delete=models.CASCADE)
    two = models.ForeignKey(User, on_delete=models.CASCADE, related_name="two")
    three = models.ForeignKey(User, on_delete=models.CASCADE, related_name="three")
    date = models.DateField()