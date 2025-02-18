from logging_config import logger


class AddressBookMain:
    """
        This class contains the functions for the multiple operations of the address book
    """

    def __init__(self,first_name,last_name,address,city,state,zipcode,phone_number,email):
        """
        Description: Constructor which initializes all the values when object is created

        Parameter: self: object
                   first_name: first name of the contact
                   last_name: last name of the contact
                   address: address of the contact
                   city: City of the contact
                   state: state of the contact
                   zipcode: zipcode of the contact
                   phone_number: phone number of the contact
                   email: email of the contact

        Return: None
        """

        self.first_name=first_name
        self.last_name=last_name
        self.address=address
        self.city=city
        self.state=state
        self.zipcode=zipcode
        self.phone_number=phone_number
        self.email=email
        self.address_book=dict()
        self.contact_dict={
            "Address":self.address,
            "City":self.city,
            "State":self.state,
            "Zipcode":self.zipcode,
            "Phone Number":self.phone_number,
            "Email":self.email
        }
        self.address_book[self.first_name+" "+self.last_name]=self.contact_dict
        logger.info("Created the dictionary successfully.")

    def except_hand(self):
        """
        Description: This function is used for finding Value error in zipcode and phone number

        Parameter: Self: object

        Return: Raises error if True else nothing
        """

        if not self.zipcode.isdigit():
            raise ValueError("The zipcode should only contain numbers.")
            logger.error("Error on the zipcode.")

        if not self.phone_number.isdigit():
            raise ValueError("The phone number should only contain number.")
            logger.error("Error on the phone number.")

    def print_contact(self):
        """
        Description: Function for printing the contact details

        Parameter: self: object

        Return: None
        """

        print()
        for key,value in self.address_book.items():
            print(f"\nName - {key}")
            for key1,value1 in value.items():
                print(f"{key1} - {value1}")
        
        logger.info("Printed the details successfully.")

    def update_contact(self):
        """
        Description: Function for updating the contact details

        Parameter: self: object

        Return: None
        """

        print("Updating the contacts again...\nRe-Enter the details: \n")
        try:
            self.first_name=input("Enter the first name: ")
            self.last_name=input("Enter the last name: ")
            self.address=input("Enter the address: ")
            self.city=input("Enter the name of city: ")
            self.state=input("Enter the name of state: ")
            self.zipcode=input("Enter the zipcode: ")
            self.phone_number=input("Enter the phone number: ")
            self.email=input("Enter the email: ")
            self.except_hand()

        except ValueError as ve:
            print(f"Invalid error: {ve}")
            logger.error(f"Value Error: {ve}")

        except Exception as e:
            print(f"Invalid error: {e}")
            logger.error(f"Value Error: {e}")
        
        self.contact_dict={
            "Address":self.address,
            "City":self.city,
            "State":self.state,
            "Zipcode":self.zipcode,
            "Phone Number":self.phone_number,
            "Email":self.email
            }

        self.address_book[self.first_name+" "+self.last_name]=self.contact_dict
        logger.info("Updated the dictionary successfully.")
        print("Updated the Dictionary!!")
    

def main():
    """
    Description: Driver code

    parameter: None

    Return: Prints the dictionary
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
        
        contact_one=AddressBookMain(first_name,last_name,address,city,state,zipcode,phone_number,email)
        print("\nEnter the choice:\n1. Print the Contact.\n2. Update the Contact.\n3. Exit")
        choice=input("\nThe Choice: ")

        while True:
            match choice:
                case "1":
                    contact_one.print_contact()
                
                case "2":
                    contact_one.update_contact()
                
                case "3":
                    print("Exiting the program!!!")
                    break

                case default:
                    print("\nInvalid Input!\nTry the other options available!")

            print("\nEnter the choice:\n1. Print the Contact.\n2. Update the Contact.\n3. Exit")
            choice=input("\nThe Choice: ")


    except ValueError as ve:
        print(f"Invalid error: {ve}")
        logger.error(f"Value Error: {ve}")

    except Exception as e:
        print(f"Invalid error: {e}")
        logger.error(f"Value Error: {e}")


if __name__=="__main__":
    main()
