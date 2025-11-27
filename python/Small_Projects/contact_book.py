class Contacts:
    def __init__(self,name,email_id,phone_number):
        self.name = name
        self.email_id = email_id
        self.phone_number = phone_number

    def __str__(self):
        return (f"{self.name}, {self.email_id}, {self.phone_number}")


class Contact_book:
    def __init__(self):
        self.my_contacts = []

    def add(self, contact):
        self.my_contacts.append(contact)
        print(f"{contact.name} has been added to the dictionary")
    
    def search(self,contact):
        for c in self.my_contacts:
            if c.name.lower() == contact.lower():
                return str(c)
            
    def delete(self,contact):
        for c in self.my_contacts:
            if c.name.lower() == contact.lower():
                self.my_contacts.remove(c)
                print(f"Contact {contact} has been removed from dictionary")
                break
        


contact_book=Contact_book()
contact1 = Contacts("Parker", "kparker@spider.com", 987343427)
contact2 = Contacts("Tony", "tonystark@starkinustries.com", 547384992)
contact_book.add(contact1)
contact_book.add(contact2)
print(contact_book.search("parker"))
print(contact_book.delete("parker"))