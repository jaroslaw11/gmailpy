import os
import base64
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/gmail.compose",]

class GmailService:
    def __init__(self):
        """
        Initializes the class instance.

        This function sets up the `_service` attribute by calling the `_auth` method.

        Parameters:
            self (class instance): The current instance of the class.

        Returns:
            None
        """
        self._service = self._auth()
    
    def _auth(self):
        """
        Authenticates the user and returns the Gmail service object.

        Returns:
            service (googleapiclient.discovery.Resource): The Gmail service object.

        Raises:
            HttpError: An error occurred during authentication.
        """
        creds = None
        if os.path.exists("token.json"):
            creds = Credentials.from_authorized_user_file("token.json", SCOPES)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file("creds_dev.json", SCOPES)
                creds = flow.run_local_server(port=0)
            with open("token.json", "w") as token:
                token.write(creds.to_json())
        try:
            service = build("gmail", "v1", credentials=creds)
            print("auth done")
            return service
        except HttpError as error:
            print(f"An error occurred: {error}")

    def create_message(self, sender, to, subject, message):
        """
        Create a message with the given sender, recipient, subject, and body.
        
        Args:
            sender (str): The email address of the sender.
            to (str): The email address of the recipient.
            subject (str): The subject of the email.
            message (str): The body of the email.
        
        Returns:
            dict: A dictionary containing the raw encoded message.
        """
        message = (
            f"From: {sender}\n"
            f"To: {to}\n"
            f"Subject: {subject}\n\n"
            f"{message}"
        )
        encoded_message = base64.urlsafe_b64encode(message.encode("utf-8")).decode("utf-8")
        return {"raw": encoded_message}

    def send_email(self, to, subject, message):
        """
        Sends an email to the specified recipient.

        Args:
            to (str): The email address of the recipient.
            subject (str): The subject of the email.
            message (str): The body of the email message.

        Returns:
            None
        """
        email_message = self.create_message("me", to, subject, message)
        result = self._service.users().messages().send(userId="me", body=email_message).execute()
        print(f"Message sent: {result['id']}")

    def create_draft(self, to, subject, message):
        """
        Creates a draft email.

        Args:
            to (str): The recipient of the email.
            subject (str): The subject of the email.
            message (str): The body of the email.

        Returns:
            None
        """
        draft = {"message": self.create_message("me", to, subject, message)}
        response = self._service.users().drafts().create(userId="me", body=draft).execute()
        print(f"Draft created with ID: {response['id']}")
