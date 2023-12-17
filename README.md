## Description
Simple Google`s Gmail API wrapper in Python. Allows you to create an email draft in your Gmail profile.

## Installation
1. Begin by setting up your Google Cloud App following the instructions in the [official Google Tutorial](https://developers.google.com/gmail/api/quickstart/python).

> For the credentials JSON file, we use the name "creds_dev.json." Remember to rename it and place it in the project's root folder in the following steps.

2. Download the source code from this repository and unpack it to your preferred location.
3. Create and activate your venv-like virtual environment, as described [here](https://docs.python.org/3/library/venv.html).
4. Install the required dependencies from step 1:
```bash
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```
5. Run the code by executing the following command in the project's root folder:.
```bash
python main.py
```

> During the first launch, the Google API will prompt your browser for authorization via your Google account to obtain necessary permissions, with the main one being *"Edit drafts and send emails"*

Once authorized you should see `auth done` message in your console.

6. To create an email draft, enter the recipient's email address, subject, and message. Upon completion, you should see something like:

`Draft created with ID: r-12345`

This indicates that your email draft has been created in your Gmail profile, and you can view it in the "Drafts" section through your browser. Enjoy!

## Design breakdown
Designed to be simple out of the box and self-sufficient, all core functionality is encapsulated within the GmailService class, located in the gmail.py file. The main.py file serves as a usage example of the GmailService class.
So, you can simply import it as a module into your own python files as as demonstrated in the main.py file:

```python
from gmail import GmailService
```

Now, when you create an instance of it, `_auth` method will be invoked. 
