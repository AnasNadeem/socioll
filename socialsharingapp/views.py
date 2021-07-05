from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .models import FriendRequest, Profile
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.

@login_required(login_url='account_login')
def home(request):
    profile_info = Profile.objects.filter(user=request.user)
    profile = Profile.objects.get(user=request.user)
    fr_rq = FriendRequest.objects.invitation_recieved(profile)
    context = {
        'profile':profile_info,
        'fr_req':fr_rq,
    }
    if request.method=="POST":
        # profile_pic = request.FILES.get('profile_pic')
        instagram= request.POST['instagram']
        snapchat= request.POST['snapchat']
        twitter= request.POST['twitter']
        reddit= request.POST['reddit']
        facebook= request.POST['facebook']
        phone_num =request.POST['phone_num']
        linkedin= request.POST['linkedin']
        youtube= request.POST['youtube']
        whatsapp= request.POST['whatsapp']
        gmail= request.POST['gmail']

        profile_in = Profile.objects.get(user=request.user)
        profile_in.instagram = instagram
        profile_in.snapchat = snapchat
        profile_in.twitter = twitter
        profile_in.reddit = reddit
        profile_in.facebook = facebook
        profile_in.phone_num = phone_num
        profile_in.linkedin = linkedin
        profile_in.youtube = youtube
        profile_in.whatsapp = whatsapp
        profile_in.gmail = gmail
        profile_in.save()
        messages.info(request, f"Social Account added.")

    return render(request, 'index.html', context)

@login_required(login_url='account_login')
def friend_list(request):
    profile_info = Profile.objects.filter(user=request.user)

    context = {
        'profile':profile_info
    }
    return  render(request, 'friendlist.html', context)

@login_required(login_url='account_login')
def invites_recieved_view(request):
    profile = Profile.objects.get(user=request.user)
    fr_rq = FriendRequest.objects.invitation_recieved(profile)

    # Filter my profile
    fr_req_rec = FriendRequest.objects.filter(sender=profile)
    fr_req_sen = FriendRequest.objects.filter(reciever=profile)

    fr_req_reciever = [item.reciever.user.username for item in fr_req_rec]
    fr_req_sender = [item.sender.user.username for item in fr_req_sen]

    # Search Fun 
    if request.method=="POST":
        usernamefriend= request.POST['usernamefriend']
        try:
            get_user = User.objects.get(username=usernamefriend)

            get_profile = Profile.objects.filter(user=get_user)
           
            context = {
                'search':get_profile,
                'friend_req':fr_rq,
                'fr_rq_reciever':fr_req_reciever,
                'fr_rq_sender':fr_req_sender,
            }
            return render(request, 'friendrequest.html', context)
        except:
            messages.info(request, f"No such user exist.")

    context = {
        'friend_req':fr_rq
    }
    return render(request, 'friendrequest.html', context)

def send_friend_request(request):
    if request.method=="POST":
        sen_fr_rq_pk= request.POST['sen_fr_rq_pk']
        
        sender = Profile.objects.get(user=request.user)
        reciever = Profile.objects.get(pk=sen_fr_rq_pk)
        
        fr_req = FriendRequest.objects.create(sender=sender, reciever=reciever, status="send")
        messages.info(request, f"Friend request sent.")
        return redirect(request.META.get('HTTP_REFERER'))

    return redirect('frrequest')

def remove_from_friend(request):
    if request.method=="POST":
        rem_fr_pk= request.POST['rem_fr_pk']
        
        sender = Profile.objects.get(user=request.user)
        reciever = Profile.objects.get(pk=rem_fr_pk)

        fr_req = FriendRequest.objects.get((Q(sender=sender) & Q(reciever=reciever)) | (Q(sender=reciever) & Q(reciever=sender)))
        fr_req.delete()
        return redirect(request.META.get('HTTP_REFERER'))

    return redirect('frrequest')
        
def accept_friend_request(request):
    if request.method=="POST":
        acc_fr_rq_pk= request.POST['acc_fr_rq_pk']

        reciever = Profile.objects.get(user=request.user)
        sender = Profile.objects.get(pk=acc_fr_rq_pk)

        fr_req = FriendRequest.objects.get(sender=sender, reciever=reciever, status="send")
        fr_req.status = "accepted"
        fr_req.save()

        return redirect(request.META.get('HTTP_REFERER'))

    return redirect('frrequest')

def decline_friend_request(request):
    if request.method=="POST":
        dec_fr_rq_pk= request.POST['dec_fr_rq_pk']

        reciever = Profile.objects.get(user=request.user)
        sender = Profile.objects.get(pk=dec_fr_rq_pk)

        fr_req = FriendRequest.objects.get(sender=sender, reciever=reciever, status="send")
        fr_req.delete()

        return redirect(request.META.get('HTTP_REFERER'))

    return redirect('frrequest')