def load_variables(choice):
    try:
        with open("variables.dat", "rb") as file:
            file.write(b'')  # Write an empty byte string to clear the contents
    except FileNotFoundError:
        # Create an empty dat file if it doesn't exist
        with open("variables.dat", "wb") as file:
            pass
    
    if choice == "delete":
        with open("variables.dat", "rb") as file:
            file.write(b'')  # Write an empty byte string to clear the contents
        return None
    elif choice == "load":
        with open("data.dat", "rb") as file:
            data = pickle.load(file)
        return data
    elif "update":
        data = {
            'x': x,
            'parsed_title': parsed_title,
            'number_of_parsed_entries': number_of_parsed_entries
        }
        with open("variables.dat", "wb") as file:
            pickle.dump(data, file)
    


def update_variables(x, parsed_title, number_of_parsed_entries):
    data = {
        'x': x,
        'parsed_title': parsed_title,
        'number_of_parsed_entries': number_of_parsed_entries
    }
    with open("variables.dat", "wb") as file:
        pickle.dump(data, file)


def delete_variables():
    with open("variables.dat", "wb") as file:
        file.write(b'')  # Write an empty byte string to clear the contents


def load_variables():
    try:
        with open("data.dat", "rb") as file:
            data = pickle.load(file)
        return data
    except FileNotFoundError:
        with open("variables.dat", "wb") as file:
            return None



    


