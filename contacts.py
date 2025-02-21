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
        self.address_book={}
        self.system_book={}
        self.contact_dict={
            "Address":self.address,
            "City":self.city,
            "State":self.state,
            "Zipcode":self.zipcode,
            "Phone Number":self.phone_number,
            "Email":self.email
        }
        self.address_book[self.first_name+" "+self.last_name]=self.contact_dict
        self.address_book_name=input("Enter the name of the address book your adding the contact to: ")
        if self.address_book_name not in self.system_book:
            self.system_book[self.address_book_name] = {}

        self.system_book[self.address_book_name].update(self.address_book)
        self.address_book={}
        logger.info("Uploaded a contact into the system")

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

        if not self.system_book:
            print("The Address book is empty!!")
            logger.warning("Trying to print a empty Address Book.")

        print()
        for key,value in self.system_book.items():
            print(f"\n{key}")
            for key1,value1 in value.items():
                print(f"\nName - {key1}")
                for key2,value2 in value1.items():
                    print(f"{key2} - {value2}")
        
        logger.info("Printed the Contact details successfully.")

    def update_contact(self):
        """
        Description: Function for updating the contact details

        Parameter: self: object

        Return: None
        """

        print("Updating the contacts again.....\nRe-Enter the details: \n")
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
        self.address_book_name=input("Enter the name of the address book your adding the contact to: ")
        if self.address_book_name not in self.system_book:
            self.system_book[self.address_book_name] = {}

        self.dupe_check()
        self.system_book[self.address_book_name].update(self.address_book)
        self.address_book={}
        logger.info("Updated the dictionary successfully.")
        print("Updated the Dictionary!!\n")

    def delete_contact(self):
        """
        Description: This function removes the contact from the Address Book

        Parameter: self: object

        Return: None
        """

        if not self.system_book:
            print("The Address Book is empty!! Cant delete anything..")
            logger.warning("The Address is Empty and tried to delete a contact.")
        
        else:
            self.print_address_book()
            self.address_book_name=input("Enter the address book name you want to delete the contact from: ")
            if self.address_book_name in self.system_book.keys():
                print("\nEnter the first name and last name to delete the contact..")
                self.first_name=input("Enter the First name: ")
                self.last_name=input("Enter the Last name: ")
                full_name=self.first_name+" "+self.last_name
                if full_name in self.system_book[self.address_book_name]:
                    self.system_book[self.address_book_name].pop(full_name)
                    print(f"\nRemoved {self.first_name+" "+self.last_name} from the Address Book.")
                    logger.info("Removed a contact from Address Book.")

                else:
                    print(f"The {self.first_name+" "+self.last_name} was not in the Address Book.")
                    logger.warning("Tried to delete a contact which wasn't there in the Address Book.")
            
            else:
                print("The Address book is not in the system. ")
                logger.warning("The User tried accessing a address book which doesn't exist.")

    def print_address_book(self):
        """
        Description: This function is used to print the available Address book in the system

        Parameter: Self: Object

        Return: Prints the available Address Book
        """

        if not self.system_book:
            print("The System doesnt have any Address book.")
            logger.info("The System has no Address book!")
        
        else:
            print("\nThe Address book in the system as follow:\n")
            for key in self.system_book.keys():
                print(f"{key}")
            logger.info("The Address Book available in the system was printed.")

    def dupe_check(self):
        full_name=self.first_name+" "+self.last_name
        if full_name in self.system_book[self.address_book_name]:
            print("The Contact already existed in the system...\nIt is being overwritten!!")
            logger.warning("The user tried adding the contact which was already there and it got overwritten.")
    
def main():
    """
    Description: Driver code

    parameter: None

    Return: Prints the dictionary
    """

    try:
        logger.info("Started the Script!!!")
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
        print("\nEnter the choice:\n1. Print the Contact book.\n2. Print the Contact Details.\n3. Update the Contact.\n4. Delete contact.\n5. Exit")
        choice=input("\nThe Choice: ")

        while True:
            match choice:
                case "1":
                    contact_one.print_address_book()

                case "2":
                    contact_one.print_contact()
                
                case "3":
                    counter=int(input("How many contacts you have decided to add: "))
                    logger.info(f"The user has decided to add {counter} contacts")
                    for i in range(counter):
                        contact_one.update_contact()
                
                case "4":
                    contact_one.delete_contact()

                case "5":
                    print("Exiting the program!!!")
                    logger.info("Closed the Script!!!!")
                    break

                case default:
                    print("\nInvalid Input!\nTry the other options available!")

            print("\nEnter the choice:\n1. Print the Contact book.\n2. Print the Contact Details.\n3. Update the Contact.\n4. Delete contact.\n5. Exit")
            choice=input("\nThe Choice: ")

    except ValueError as ve:
        print(f"Invalid error: {ve}")
        logger.error(f"Value Error: {ve}")

    except Exception as e:
        print(f"Invalid error: {e}")
        logger.error(f"Value Error: {e}")


if __name__=="__main__":
    main()



"""

system_book={'Book1': {
    'Ashwin Kumar': {'Address': 'asdasd', 'City': 'asdas', 'State': 'sadas', 'Zipcode': '21312', 'Phone Number': '123123', 'Email': 'asdasda'}, 
    'Ash Kuma': {'Address': 'asdasd', 'City': 'adasd', 'State': 'sadasd', 'Zipcode': '123123', 'Phone Number': '213123', 'Email': 'asfdasfas'}
    }, 
    'Book2': {
    'Ash k': {'Address': 'adsasd', 'City': 'asdas', 'State': 'sadasd', 'Zipcode': '21312', 'Phone Number': '231321', 'Email': 'sadsad'}
    }, 
    'Book3': {
    'Ash kum': {'Address': 'adsad', 'City': 'sadasd', 'State': 'asdasd', 'Zipcode': '321', 'Phone Number': '12312', 'Email': 'asdasd'}
    }
    }
for key,value in d1.items():
    # print(key,value)    #Key- Book Name.... Value- Contact Book
    # print()
    for key1,value1 in value.items():
        # print(key1,value1)    #Key- Full_name... Value- Contact_details
        # print()
        for key2,value2 in value1.items():
            print(key2,value2)   #Key2- Address, City, state.blehbleh value2- The details
            
"""