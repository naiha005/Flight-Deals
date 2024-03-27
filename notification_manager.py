import smtplib
import requests
from twilio.rest import Client

TWILIO_SID = "YOUR TWILIO SID"
TWILIO_AUTH_TOKEN = "YOUR AUTH TOKEN"
TWILIO_VIRTUAL_NUMBER = "YOUR VIRTUAL MOBILE NUMBER"
TWILIO_VERIFIED_NUMBER = "YOUR MOBILE NUMBER"


SHEETY_USER_ENDPOINT = "https://api.sheety.co/670bd5b7865748332674b8e31ee750e1/flightDeals/users"
sender_email = "YOUR EMAIL"
password = "YOUR PASSWORD"
# securesally@gmail.com



class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        print(message.sid)

    def send_emails(self, emails, message):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=sender_email, password=password)
            for email in emails:
                connection.sendmail(
                    from_addr=sender_email,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8')
                )
