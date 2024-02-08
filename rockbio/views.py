from django.shortcuts import render
from django.shortcuts import redirect
from individuals.models import Individual
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.http import require_GET, require_POST


from django.conf import settings
from django.contrib.auth.decorators import login_required
from djstripe.settings import djstripe_settings

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from djstripe.settings import djstripe_settings
from djstripe.models import Subscription

import stripe

from settings.models import SubscriptionHolder

def index(request):
    if request.method == 'POST':
        status = request.POST['status']
        # print('status', status)
    else:
        status = ''
    if request.user.is_staff:
        if status != '':
            individuals = Individual.objects.filter(status=status).order_by('-id')
        else:
            individuals = Individual.objects.all().order_by('-id')
    elif request.user.is_authenticated:
        individuals = Individual.objects.filter(user=request.user).order_by('-id')
    else:
        individuals = Individual.objects.filter(user=None).order_by('-id')

    n_individuals = individuals.count()

    paginator = Paginator(individuals, 1000) # Show 25 contacts per page

    page = request.GET.get('page')

    try:
        individuals = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        individuals = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        individuals = paginator.page(paginator.num_pages)


    context = {
    'n_individuals': n_individuals,
    'individuals':individuals
    }
    return render(request, 'dashboard/dashboard.html', context)


def docs(request):
    return redirect("https://rockbio.readthedocs.io/")

@login_required
def pricing_page(request):
    return render(request, 'pricing_page.html', {
        'stripe_public_key': djstripe_settings.STRIPE_PUBLIC_KEY,
        'pricing_table_id': settings.STRIPE_PRICING_TABLE_ID,
    })

@login_required
def subscription_confirm(request):
    # set our stripe keys up
    stripe.api_key = djstripe_settings.STRIPE_SECRET_KEY

    # get the session id from the URL and retrieve the session object from Stripe
    session_id = request.GET.get("session_id")
    session = stripe.checkout.Session.retrieve(session_id)

    # get the subscribing user from the client_reference_id we passed in above
    client_reference_id = int(session.client_reference_id)

    subscription_holder, created = SubscriptionHolder.objects.get_or_create(user=request.user)
    # sanity check that the logged in user is the one being updated
    #assert subscription_holder == request.user

    # get the subscription object form Stripe and sync to djstripe
    subscription = stripe.Subscription.retrieve(session.subscription)
    djstripe_subscription = Subscription.sync_from_stripe_data(subscription)

    # set the subscription and customer on our user
    subscription_holder.subscription = djstripe_subscription
    subscription_holder.customer = djstripe_subscription.customer
    subscription_holder.save()

    command = f'bash scripts/create_user_jupyterlab.sh {subscription_holder.user}'

    # show a message to the user and redirect
    messages.success(request, f"You've successfully signed up. Thanks for the support!")
    return HttpResponseRedirect(reverse("subscription_details"))


@login_required
def create_portal_session(request):
    stripe.api_key = djstripe_settings.STRIPE_SECRET_KEY
    subscription_holder, created = SubscriptionHolder.objects.get_or_create(user=request.user)
    portal_session = stripe.billing_portal.Session.create(
        customer=subscription_holder.customer.id,
        return_url="https://daivero.rockbio.io/subscription-details/",
    )
    return HttpResponseRedirect(portal_session.url)
