import sendgrid
import os
from sendgrid.helpers.mail import Mail, Email, To, Content

sg = sendgrid.SendGridAPIClient(api_key='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')
from_email = Email("jameskarthi1121@gmail.com")  # Change to your verified sender
to_email = To("rajalingamraju19062002@gmail.com")  # Change to your recipient
subject = "Sending with SendGrid is Fun"
content = Content("text/plain", "and easy to do anywhere, even with Python")
mail = Mail(from_email, to_email, subject, content)

# Get a JSON-ready representation of the Mail object
mail_json = mail.get()

# Send an HTTP POST request to /mail/send
response = sg.client.mail.send.post(request_body=mail_json)
print(response.status_code)
print(response.headers)
