import emails

def main():
    try:
        with open('email.txt', 'r', encoding='utf-8') as file:
            content = file.read()
            
        print(f"Sender: {emails.email_sender(content)}")
        print(f"Recipient: {emails.email_recipient(content)}")
        print(f"Subject: {emails.email_subject(content)}")
        print(f"Body:\n{emails.email_body(content)}")
        
    except FileNotFoundError:
        print("File 'email.txt' not found.")

if __name__ == "__main__":
    main()
