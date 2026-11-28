from contact import Contact
from contact_list import Contact_List

def main():
    contacts = Contact_List()
    contacts.add_contact(Contact("John Brown", "brown@onet.pl", "555234000"))
    contacts.add_contact(Contact("Anna May", "am@o2.pl", "232000199"))
    contacts.add_contact(Contact("George Small", "smallg@google.pl", "222999100"))
    contacts.add_contact(Contact("Paola Big", "bigpaola@poczta.pl", "100200300"))

    contacts.display_contacts()

if __name__ == "__main__":
    main()
