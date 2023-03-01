# Izveidosim kontaku glabāšanas aplikāciju
# Funckijas
# Datu struktūras (JSON)
# Failu I/O (ievade un izvade)
import json

contacts = []

def AddContact():
    name = input("Enter name: ")
    surname = input("Enter surname: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")

    contact = {
        'name': name,
        'surname': surname,
        'phone': phone,
        'email': email
    }

    contacts.append(contact)

def PrintContacts():
    for contact in contacts:
        print(f"{contact['name']}")

# UDZDEVUMS
# Izveido funkciju kas prasa no litotāja vārdu
# izdēš kontaktu ar to vārdu

def DeleteContact():
    name = input('Enter contact name: ')
    for contact in contacts:
        if contact['name'] == name:
            contacts.remove(contact)
            print(f"Contact {name} is deleted.")
            return
    
    print(f"Contact {name} was not found!")

def SaveContacts():
    with open('prog1-10-1200/contacts.json', 'w', encoding='UTF8') as file:
        contacts_dict = {
            'contacts': contacts
        }        
        json.dump(contacts_dict, file, indent=4)

def LoadContacts():
    # UZDEVUMS
    # izveido funkciju kas nolasīs datus no 
    # faila contacts.json uz sarakstu contacts
    with open('prog1-10-1200/contacts.json', 'r', encoding='UTF8') as file:
        dict = json.load(file)
        return dict['contacts']

contacts = LoadContacts()
while(True):
    response = input("A-add contact, D-delete,  P-print, E-exit: ")
    
    if response == 'A':
        AddContact()
        SaveContacts()
    elif response == 'D':
        DeleteContact()
        SaveContacts()
    elif response == 'P':
        PrintContacts()           
    elif response == 'E':
        break