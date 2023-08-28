from django.conf import settings
import firebase_admin
from firebase_admin import messaging
from firebase_admin import credentials


cred = credentials.Certificate(settings.FIREBASE_GOOGLE_APPLICATION_CREDENTIALS)
firebase_admin.initialize_app(cred)


def send_notification(user_token, title, body):
    try:
        message = messaging.Message(notification=messaging.Notification(title=title, body=body), token=user_token)
        response = messaging.send(message)
    except:
        pass
