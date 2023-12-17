from gmail import GmailService

def input_email_from_user():
    to = input("Enter recipient's email address: ")
    subject = input("Enter email subject: ")
    message = input("Enter email message: ")
    return to, subject, message

def main():
    service = GmailService()
    print('---')
    to, subject, message = input_email_from_user()
    service.create_draft(to, subject, message)

if __name__ == "__main__":
  main()