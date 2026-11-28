import re

def email_sender(email_content):
    match = re.search(r'^From:\s*(.*)', email_content, re.MULTILINE)
    return match.group(1) if match else "Not found"

def email_recipient(email_content):
    match = re.search(r'^To:\s*(.*)', email_content, re.MULTILINE)
    return match.group(1) if match else "Not found"

def email_subject(email_content):
    match = re.search(r'^Subject:\s*(.*)', email_content, re.MULTILINE)
    return match.group(1) if match else "Not found"

def email_body(email_content):
    match = re.search(r'\n\n(.*)', email_content, re.DOTALL)
    return match.group(1).strip() if match else "Not found"
