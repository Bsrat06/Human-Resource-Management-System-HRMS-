from .models import Notification

# method for creation of notifications
def create_notification(user, message):
    notification = Notification.objects.create(user=user, message=message)
    notification.save()

# method for retrieval of notifications
def get_notifications(user):
    return Notification.objects.filter(user=user).order_by('-timestamp')