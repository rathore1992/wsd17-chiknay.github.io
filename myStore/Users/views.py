

from .forms import UserRegForm

import uuid
from django.db import transaction, IntegrityError
from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Profile
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages

from django.contrib.auth.models import Group, User
from django.contrib.auth.views import login
from django.contrib.auth.decorators import login_required

# Create your views here.
@transaction.atomic
def registerUser(request):

    if request.user.is_authenticated():
        messages.warning(request, "You are already logged in.")
        return HttpResponseRedirect(reverse('home'))

    if request.method == 'POST':
        form = UserRegForm(request.POST)

        if not form.is_valid():
            return render(request, "Registration/register.html", {'form': form})
        else:
            form.instance.is_active = False
            new_user = form.save()

            actToken = uuid.uuid4()
            print actToken
            p = Profile.objects.create(user=new_user, activationToken=actToken)
            p.save()

            if form.cleaned_data["signupAsDeveloper"]:
                try:
                    print("I am in 3")
                    devs = Group.objects.get_or_create(name='developers')[0]
                    devs.user_set.add(p.user)
                except Group.DoesNotExist:
                    devs = None
            else:
                players = Group.objects.get_or_create(name='players')[0]
                players.user_set.add(p.user)

            print "Click on this link to activate account:   http://127.0.0.1:8003"+reverse(viewname='activate'
                                                                                            , args=(actToken,))
            return HttpResponseRedirect(reverse("home"))

    elif request.method == 'GET':
        form = UserRegForm()

        return render(request, "Registration/register.html", {
            'form': form,
        })



def activateAccount(request, activationCode=None):

    if request.method == 'GET':

        if not is_uuid_valid(activationCode):
            messages.error(request=request, message='Activation ID is invalid.')
        else:
            p = None
            try:
                with transaction.atomic():
                    p = Profile.objects.get(activationToken=activationCode)
                    if p.user.is_active:
                        messages.error(request=request, message='Account is already active.')
                    else:
                        p.user.is_active = True
                        p.user.save()
                        messages.success(request=request, message='You account has been activated!')

            except ObjectDoesNotExist:
                messages.error(request=request, message='Problem during activation. Please try again.')

        return HttpResponseRedirect(redirect_to=reverse("home"))


def is_uuid_valid(uuid_str):
    try:
        val = uuid.UUID(uuid_str, version=4)
        return True
    except:
         return False




def NormalLogin(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('account'))
    else:
        return login(request, template_name='Registration/login.html')


def profile(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('home'))
