from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
# Create your models here.
# class ProfileManager(models.Manager):

#     def get_all_profiles(self, me):
#         profiles = Profile.objects.all().exclude(user=me)
#         return profiles

#     def get_all_profiles_to_invite(self, sender):
#         profiles = Profile.objects.all().exclude(user=sender)
#         profile = Profile.objects.get(user=sender)
#         qs = FriendRequest.objects.filter(Q(sender=profile) | Q(reciever=profile))

#         accepted = set([])
#         for rel in qs:
#             if rel.status=='accepted':
#                 accepted.add(rel.reciever)
#                 accepted.add(rel.sender)

#         available = [profile for profile in profiles if profile not in accepted]
#         return available

class Profile(models.Model):
    # first_name = models.CharField(max_length=40, blank=True)
    # last_name = models.CharField(max_length=40, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    instagram= models.CharField(max_length=40, blank=True)
    snapchat= models.CharField(max_length=40, blank=True)
    twitter= models.CharField(max_length=40, blank=True)
    reddit= models.CharField(max_length=40, blank=True)
    facebook= models.CharField(max_length=40, blank=True)
    phone_num = models.CharField(max_length=40, blank=True)
    linkedin= models.CharField(max_length=40, blank=True)
    youtube= models.CharField(max_length=40, blank=True)
    whatsapp= models.CharField(max_length=40, blank=True)
    # clubhouse= models.CharField(max_length=40, blank=True)
    gmail= models.CharField(max_length=40, blank=True)
    avatar = models.ImageField(upload_to='photo', default="photo/image.jpg")
    friends = models.ManyToManyField(User, blank=True, related_name="profiles")
    slug = models.SlugField(unique=True, blank=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.created.strftime('%d %m %Y')}"

    def save(self, *args, **kwargs):
        self.slug = f'{self.user}'
        super().save(*args, **kwargs)


STATUS_CHOICES = (
    ('send', 'send'),
    ('accepted', 'accepted')
)

class FriendRequestManager(models.Manager):
    def invitation_recieved(self, reciever):
        qs = FriendRequest.objects.filter(reciever=reciever, status='send')
        return qs 


class FriendRequest(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="sender")
    reciever = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="reciever")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    objects = FriendRequestManager()

    def __str__(self):
        return f"{self.sender} - {self.reciever} - {self.status} - {self.updated.strftime('%X %d %m %Y')} - {self.created.strftime('%X %d %m %Y')}"