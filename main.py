
        

print("===== Blood Bank Management System =====")

donors = []
receivers = []

def add_donor():
    name = input("Enter donor name: ")
    age = input("Enter donor age: ")
    blood_group = input("Enter blood group: ")
    phone = input("Enter phone number: ")
    address = input("Enter address: ")

    donor = {
        "Name": name,
        "Age": age,
        "Blood Group": blood_group,
        "Phone": phone,
        "Address": address
    }

    donors.append(donor)
    print("Donor added successfully!\n")

def view_donors():
    if not donors:
        print("No donors available.\n")
    else:
        print("---- Donor List ----")
        for d in donors:
            print(d)
        print()

def add_receiver():
    name = input("Enter receiver name: ")
    age = input("Enter receiver age: ")
    blood_group = input("Enter required blood group: ")
    phone = input("Enter phone number: ")
    address = input("Enter address: ")

    receiver = {
        "Name": name,
        "Age": age,
        "Blood Group": blood_group,
        "Phone": phone,
        "Address": address
    }

    receivers.append(receiver)
    print("Receiver added successfully!\n")

def view_receivers():
    if not receivers:
        print("No receivers available.\n")
    else:
        print("---- Receiver List ----")
        for r in receivers:
            print(r)
        print()

def main():
    while True:
        print("1. Add Donor")
        print("2. View Donors")
        print("3. Add Receiver")
        print("4. View Receivers")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_donor()
        elif choice == "2":
            view_donors()
        elif choice == "3":
            add_receiver()
        elif choice == "4":
            view_receivers()
        elif choice == "5":
            print("Thank you for using Blood Bank System.")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
