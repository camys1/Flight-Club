import smtplib
import os
from twilio.rest import Client # type: ignore
from dotenv import load_dotenv # type: ignore

load_dotenv()

class NotificationManager:

    def __init__(self):
        # Retrieve environment variables only once
        self.smtp_address = os.getenv("EMAIL_PROVIDER_SMTP_ADDRESS")
        self.email = os.getenv("MY_EMAIL")
        self.email_password = os.getenv("MY_EMAIL_PASSWORD")
        self.twilio_virtual_number = os.getenv("TWILIO_VIRTUAL_NUMBER")
        self.twilio_verified_number = os.getenv("TWILIO_VERIFIED_NUMBER")

        self.client = Client(os.getenv('TWILIO_SID'), os.getenv("TWILIO_AUTH_TOKEN"))
        self.connection = smtplib.SMTP(os.getenv("EMAIL_PROVIDER_SMTP_ADDRESS"), port=587)

    def send_sms(self, message_body):
        
        message = self.client.messages.create(
            from_=self.twilio_virtual_number,
            body=message_body,
            to=self.twilio_verified_number
        )
        # Prints if successfully sent.
        print(message.sid)


    def send_emails(self, email_body):
        with self.connection:
            self.connection.starttls()
            self.connection.login(self.email, self.email_password)
            
            self.connection.sendmail(
                from_addr=self.email,
                to_addrs="samuilac@gmail.com",
                msg=f"Subject:New Low Price Flight!\n\n{email_body}".encode('utf-8')
            )
