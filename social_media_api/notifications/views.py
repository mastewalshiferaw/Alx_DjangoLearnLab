from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Notification


# Endpoint to fetch notifications
@login_required
def notification_list(request):
    # Order unread notifications first, then newest first
    notifications = Notification.objects.filter(recipient=request.user).order_by("read", "-timestamp")
    return render(request, "notifications/notification_list.html", {"notifications": notifications})
