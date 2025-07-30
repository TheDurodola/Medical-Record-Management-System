from administration import Admin

main_menu = """\t\t\tWelcome to Harvey Road General Hospital\t\t\t

1) Login as Administrator
2) Login as Doctor
0) Exit the application"""

admin = Admin()
loop_condition = True

while loop_condition:
    print(main_menu)
    navigate = input("Enter your choice: ")


    match navigate:
        case "1":
            print("You are now logging in as an Administrator")
            admin_id = input("Enter Administrator ID: ")
            admin_password = input("Enter Administrator password: ")
            if admin_id and admin_password == "<PASSWORD>":
                print("Login successful.")
            else:
                print("Invalid credentials. Please try again.")
                continue
            inner_loop = True
            while inner_loop:
                print("""
1) Register a new patient
2) Register a new doctor 
3) View all patients
4) View all doctors
5) Update doctor information
6) Update patient information
7) Find doctor by ID
8) Find patient by ID
9) Print Schedule Report

0) Logout to main menu
""")
                choice = input("Enter your choice: ")
                match choice:
                    case "1":
                        title = input("Enter patient's title: ")
                        first_name = input("Enter patient's first name: ")
                        last_name = input("Enter patient's last name: ")
                        try:
                            year_of_birth = int(input("Enter year of birth(yyyy): "))
                            month_of_birth = int(input("Enter month of birth(mm): "))
                            day_of_birth = int(input("Enter day of birth(dd): "))
                        except ValueError:
                            print("Please enter a number.")
                        phone_number = input("Enter phone number: ")
                        try:
                            print(admin.register_patient(title, first_name, last_name, year_of_birth, month_of_birth, day_of_birth, phone_number))
                            print("Patient registered successfully.")
                        except ValueError as e:
                            print(f"Error registering patient: {e}")
                            continue


                        if admin.check_doctor_database_size() != 0:
                            admin.assign_doctor_to_patient()

                    case "2":
                        password = input("Enter doctor's password: ")
                        first_name = input("Enter doctor's first name: ")
                        last_name = input("Enter doctor's last name: ")
                        specialization = input("Enter doctor's specialization: ")
                        phone_number = input("Enter doctor's phone number: ")
                        try:
                            print(admin.register_doctor(password, first_name, last_name, specialization, phone_number))
                            print("Doctor registered successfully.")
                        except ValueError as e:
                            print(f"Error registering doctor: {e}")
                            continue
                        if admin.check_doctor_database_size() != 0:
                            admin.assign_doctor_to_patient()

                    case "3":
                        if admin.check_patient_database_size() != 0:
                            patients = admin.retrieve_all_patient_records()
                            for patient in patients.values():
                                print(patient)
                        if admin.check_patient_database_size() == 0:
                            print("No patients registered yet.")

                    case "4":
                        if admin.check_doctor_database_size() != 0:
                            doctors = admin.retrieve_all_doctor_records()
                            for doctor in doctors.values():
                                print(doctor.get_doctor_info()+"\n")
                        if admin.check_doctor_database_size() == 0:
                            print("No doctors registered yet.")


                    case "5":
                        id_number = input("Enter doctor's ID number to update: ")
                        field_to_update = input("Which field do you want to update (first_name/last_name/specialization/phone_number)? ").lower()

                        if field_to_update == "first_name":
                            new_value = input("Enter new first name: ")
                            try:
                                admin.update_doctor_first_name(id_number, new_value)
                            except ValueError as e:
                                print(f"Error updating first name: {e}")
                                continue
                        elif field_to_update == "last_name":
                            new_value = input("Enter new last name: ")
                            try:
                                admin.update_doctor_last_name(id_number, new_value)
                            except ValueError as e:
                                print(f"Error updating last name: {e}")
                                continue
                        elif field_to_update == "specialization":
                            new_value = input("Enter new specialization: ")
                            try:
                                admin.update_doctor_specialization(id_number, new_value)
                            except ValueError as e:
                                print(f"Error updating specialization: {e}")
                        elif field_to_update == "phone_number":
                            new_value = input("Enter new phone number: ")
                            try:
                                admin.update_doctor_phone_number(id_number, new_value)
                            except ValueError as e:
                                print(f"Error updating phone number: {e}")
                                continue
                        print("Doctor's information updated.")

                    case "6":
                        id_number = input("Enter patient's ID number to update: ")
                        field_to_update = input("Which field do you want to update (first name/last name/phone number)? ").lower().strip(' ') .strip('_')

                        if field_to_update == "firstname":
                            new_value = input("Enter new first name: ")
                            admin.update_patient_first_name(id_number, new_value)
                        elif field_to_update == "lastname":
                            new_value = input("Enter new last name: ")
                            admin.update_patient_last_name(id_number, new_value)
                        elif field_to_update == "phonenumber":
                            new_value = input("Enter new phone number: ")
                            admin.update_patient_phone_number(id_number, new_value)
                        print("Patient's information updated.")

                    case "7":
                        id_number = input("Enter doctor's ID number to find: ").upper()
                        try:
                            doctor = admin.find_doctor_by_id(id_number)
                            print(doctor.get_doctor_info())
                            print("")
                        except ValueError as e:
                            print(f"Error finding doctor: {e}")

                    case "8":
                        id_number = input("Enter patient's ID number to find: ").upper()
                        try:
                            patient = admin.find_patient_by_id(id_number)
                            print(patient.__str__())
                        except ValueError as e:
                            print(f"Error finding patient: {e}")

                    case "9":
                        print("Printing schedule report...")
                        print(admin.print_schedule_report())

                    case "0":
                        print("Logging out to main menu.")
                        inner_loop = False

                    case _:
                        print("Invalid choice. Please try again.")

        case "2":
            if admin.check_doctor_database_size() == 0:
                print("No doctors registered yet.")

            else:
                doctor_id = input("Enter doctor's ID number: ").upper()
                password = input("Enter doctor's password: ")

                if admin.authenticate_doctor(doctor_id, password):
                    print(f"You are now logged in as a {admin.find_doctor_by_id(doctor_id).get_full_name()}")

                    inner_loop = True
                    while inner_loop:
                        print("""
1) View your information
2) Check your schedule
3) Find patient by ID

                        
0) Logout to main menu""")

                        choice = input("Enter your choice: ")
                        match choice:
                            case "1":
                                doctor = admin.find_doctor_by_id(doctor_id)
                                print(doctor.get_doctor_info())

                            case "2":
                                doctor = admin.find_doctor_by_id(doctor_id)
                                if doctor.get_list_of_patients():
                                    print(f"Patients assigned to {doctor.get_full_name()}:")
                                    for patient in doctor.get_list_of_patients():
                                        print(f"- {patient}")
                                else:
                                    print("No patients assigned.")

                            case "3":
                                id_number = input("Enter patient's ID number to find: ").upper()

                                try:
                                    patient = admin.find_patient_by_id(id_number)
                                    print(patient.__str__())

                                    navigator = input("Do you want to update this patient's medical record? (yes/no): ").lower()
                                    if navigator == "yes":
                                        diagnosis = input("Enter diagnosis: ")
                                        treatment = input("Enter treatment: ")
                                        admin.find_patient_by_id(id_number).add_medical_record(f"Diagnosis: {diagnosis}, Treatment: {treatment}")
                                    else:
                                        print("No changes made to the patient's record.")

                                except ValueError as e:
                                    print(f"Error finding patient: {e}")

                            case "0":
                                print("Logging out to main menu.")
                                inner_loop = False

                            case _:
                                print("Invalid choice. Please try again.")



        case "0":
            print("Exiting the application.")
            loop_condition = False

        case _:
            print("Invalid input. Try again.")
