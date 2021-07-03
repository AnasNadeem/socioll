from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile, FriendRequest

@receiver(post_save, sender=User)
def post_save_create_profile(sender, instance, created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=FriendRequest)
def post_save_add_to_friends(sender, instance, created, **kwargs):
    sender_ = instance.sender
    reciever_ = instance.reciever
    if instance.status== "accepted":
        sender_.friends.add(reciever_.user)
        reciever_.friends.add(sender_.user)
        sender_.save()
        reciever_.save()

@receiver(pre_delete, sender=FriendRequest)
def pre_delete_remove_from_friends(sender, instance, **kwargs):
    sender = instance.sender
    reciever = instance.reciever
    sender.friends.remove(reciever.user)
    reciever.friends.remove(sender.user)

    sender.save()
    reciever.save()