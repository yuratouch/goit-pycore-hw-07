def save_to_file(contacts:dict) -> None:  
    with open("contacts.txt", "w", encoding="utf-8") as file:
        for contact in contacts:
            line = contact + " " + contacts[contact]
            file.write(line + "\n")

def get_contacts() -> dict:
    contacts_dict = {}
    try:
        with open("contacts.txt", "r", encoding="utf-8") as file:
            contacts = file.readlines()
            for contact in contacts:
                name, phone_number = contact.split()
                contacts_dict[name] = phone_number
            return contacts_dict
        
    except FileNotFoundError:
        return contacts_dict