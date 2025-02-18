from logging_config import logger


def create_contact(first_name,last_name,address,city,state,zipcode,phone_number,email):
    """
    Description: The functions creates a dictionary using the given information from user

    Parameter: first_name: first name of the contact
               last_name: last name of the contact
               address: address of the contact
               city: City of the contact
               state: state of the contact
               zipcode: zipcode of the contact
               phone_number: phone number of the contact
               email: email of the contact

    return: returns the dictionary with all details
    """

    contact_dict={
        "First Name":first_name,
        "Last Name":last_name,
        "Address":address,
        "City":city,
        "State":state,
        "Zipcode":zipcode,
        "Phone Number":phone_number,
        "Email":email
    }
    logger.info("Created the dictionary successfully.")
    return contact_dict

def main():
    """
    Description: Driver code

    parameter: None

    return: Prints the dictionary
    """

    try:
        print("\nWelcome to the Address Book:\n")
        first_name=input("Enter the first name: ")
        last_name=input("Enter the last name: ")
        address=input("Enter the address: ")
        city=input("Enter the name of city: ")
        state=input("Enter the name of state: ")
        zipcode=input("Enter the zipcode: ")
        phone_number=input("Enter the phone number: ")
        email=input("Enter the email: ")

        if not zipcode.isdigit():
            raise ValueError("The zipcode should only contain numbers.")
            logger.error("Error on the zipcode.")

        if not phone_number.isdigit():
            raise ValueError("The phone number should only contain number.")
            logger.error("Error on the phone number.")
        
        contact_dict=create_contact(first_name,last_name,address,city,state,zipcode,phone_number,email)
        print()
        for key,value in contact_dict.items():
            print(f"{key} - {value}")
        
        logger.info("Printed the dictionary successfully.")

    except ValueError as ve:
        print(f"Invalid error: {ve}")
        logger.error(f"Value Error: {ve}")

    except Exception as e:
        print(f"Invalid error: {e}")
        logger.error(f"Value Error: {e}")


if __name__=="__main__":
    main()
