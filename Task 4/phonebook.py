def create_phone_book():
    return {}

def insert_number(dict, person, number, label = ""):
    for existing_person, entries in dict.items():
        for entry in entries:
            if entry['number'] == number:
                print(f"The number {number} already exists for {existing_person}")
                return dict
    existing_numbers = dict.get(person, [])
    if label != "":
        label += ":"
    existing_numbers.append({'number': number, 'label': label})
    dict[person] = existing_numbers
    return dict
   

def retrieve_number(dict, person):
    if person not in dict:
        return "Person not found"
    entries = dict[person]
    formatted_numbers = [f"{entry['label']} {entry['number']}" for entry in entries]
    return f"{person}: " + ", ".join(formatted_numbers)

def delete_number(dict, person, number):
    if person in dict:
        dict[person] = [entry for entry in dict[person] if entry['number'] != number]
    if not dict[person]:  
        del dict[person]
    return dict


def print_phone_book(dict):
    print("Your phone book: ")
    for key, value in dict.items():
        formatted_numbers = [f"{entry['label']} {entry['number']}" for entry in value]
        print(f"{key}: " + ", ".join(formatted_numbers))

if __name__ == "__main__":
    #creating a dictionary
    phone_book = create_phone_book()

    #inserting numbers, can be with labels
    #a) I chose a string to store names, a tuple would also work, but a two-element list not as it is mutable
    phone_book = insert_number(phone_book, "Ala Wesołowska", "+048 513 056 121", "main")
    phone_book = insert_number(phone_book, "Ala Wesołowska", "274-294-999", "work")
    phone_book = insert_number(phone_book, "Ala Wesołowska", "+ 048 798-123-422")
    phone_book = insert_number(phone_book, "John Smith", "0 800 241 6331", "main")
    phone_book = insert_number(phone_book, "John Smith", "469 - 452 - 199", "work")
    phone_book = insert_number(phone_book, "Susan Brown", "315-728-3639", "work")
    phone_book = insert_number(phone_book, "Bobby Brown", "346 1909 123")
    
    #trying to insert the same number for a different person - questions c) and d)
    phone_book = insert_number(phone_book, "John Smith", "315-728-3639", "work")
    print("-----------------")
    #retrieving a number
    print(retrieve_number(phone_book, "Ala Wesołowska"))
    print("-----------------")
    #deleting a number
    phone_book = delete_number(phone_book, "Ala Wesołowska","274-294-999")
    phone_book = delete_number(phone_book, "Bobby Brown", "346 1909 123") #deletes the whole contact as there is no number left
    
    #printing our phone book
    print_phone_book(phone_book)
 