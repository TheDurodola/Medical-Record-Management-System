from administration import Admin
import tkinter as tk
from tkinter import messagebox


admin = Admin()


def show_main_menu():
    clear_window()
    tk.Label(root, text="Welcome to \nJBL General Hospital", font=("Arial", 16), pady=10).pack()

    tk.Button(root, text="Login as Administrator", width=30,command=show_admin_login).pack(pady=5)
    tk.Button(root, text="Login as Doctor", width=30, command=show_doctor_login).pack(pady=5)
    tk.Button(root, text="Login as Patient", width=30, command=show_patient_login).pack(pady=5)
    tk.Button(root, text="Exit", width=30, command=root.quit).pack(pady=5)


def show_admin_login():
    clear_window()
    tk.Label(root, text="Administrator Login", font=("Arial", 14)).pack(pady=10)

    global admin_id_entry, admin_password_entry
    tk.Label(root, text="Admin ID:").pack()
    admin_id_entry = tk.Entry(root)
    admin_id_entry.pack()

    tk.Label(root, text="Password:").pack()
    admin_password_entry = tk.Entry(root, show="*")
    admin_password_entry.pack()

    tk.Button(root, text="Login", command=handle_admin_login).pack(pady=10)
    tk.Button(root, text="Back to Menu", command=show_main_menu).pack()

def view_all_patient():
    clear_window()
    tk.Label(root, text="All Patients", font=("Arial", 14)).pack(pady=10)
    patients = admin.retrieve_all_patient_records()
    if not patients:
        tk.Label(root, text="No patients registered.").pack(pady=10)
    else:
        for patient in patients.values():
            tk.Label(root, text=f"{patient.get_patient_id()} -{patient.get_first_name()} {patient.get_last_name()}").pack()
    tk.Button(root, text="Back", command=show_admin_menu).pack(pady=10)


def view_all_doctors():
    clear_window()
    tk.Label(root, text="All Doctors", font=("Arial", 14)).pack(pady=10)
    doctors = admin.retrieve_all_doctor_records()
    if not doctors:
        tk.Label(root, text="No doctors registered.").pack(pady=10)
    else:
        for doctor in doctors.values():
            tk.Label(root, text=doctor.get_doctor_info()).pack()
    tk.Button(root, text="Back", command=show_admin_menu).pack(pady=10)


def handle_admin_login():
    admin_id = admin_id_entry.get()
    password = admin_password_entry.get()
    if admin_id == "ADMIN" and password == "<PASSWORD>":
        messagebox.showinfo("Login Successful", "Welcome, Administrator!")
        show_admin_menu()
    else:
        messagebox.showerror("Login Failed", "Invalid credentials.")





def show_admin_menu():
    clear_window()
    tk.Label(root, text="Admin Menu", font=("Arial", 14)).pack(pady=10)
    tk.Button(root, text="Register New Patient", command=register_patient).pack(pady=5)
    tk.Button(root, text="Register New Doctor", command=register_doctor).pack(pady=5)
    tk.Button(root, text="View All Patients", command=view_all_patient).pack(pady=5)
    tk.Button(root, text="View All Doctors", command=view_all_doctors).pack(pady=5)
    tk.Button(root, text="Update Patient Information", command=register_doctor).pack(pady=5)
    tk.Button(root, text="Update Doctor Information", command=register_doctor).pack(pady=5)
    tk.Button(root, text="Find Doctor by ID", command=show_find_doctor_by_id).pack(pady=5)
    tk.Button(root, text="Find Patient by ID", command=register_doctor).pack(pady=5)
    # tk.Button(root, text="Print Schedule Report", command=show_print_schedule).pack(pady=5)

    tk.Button(root, text="Logout", command=show_main_menu).pack(pady=5)

def handle_patient_register():
    first_name = patient_first_name_entered.get()
    last_name = patient_last_name_entered.get()
    dob = patient_dob_entered.get()
    gender = patient_gender_entered.get()
    phone_number = patient_phone_number_entered.get()
    email = patient_email_entered.get()
    try:
        admin.register_patient(first_name, last_name, dob, gender, phone_number, email)
        messagebox.showinfo("Success", "Registration Successful.")
        admin.assign_doctor_to_patient()
        show_admin_menu()
    except ValueError as e:
        messagebox.showerror("Registration Unsuccessful!", "Please check your input.\n" + str(e))


def show_patient_login():
    clear_window()
    tk.Label(root, text="Patient Login", font=("Arial", 14)).pack(pady=10)

    global admin_id_entry, admin_password_entry
    tk.Label(root, text="Patient ID:").pack()
    admin_id_entry = tk.Entry(root)
    admin_id_entry.pack()

    tk.Label(root, text="Password:").pack()
    admin_password_entry = tk.Entry(root, show="*")
    admin_password_entry.pack()

    tk.Button(root, text="Login", command=handle_admin_login).pack(pady=10)
    tk.Button(root, text="Back to Menu", command=show_main_menu).pack()


def register_patient():
    clear_window()
    tk.Label(root, text="Register Patient", font=("Arial", 14)).pack(pady=10)

    tk.Label(root, text="Note: Only Nigerian Number is acceptable", font=("Arial", 10)).pack(pady=10)

    global patient_first_name_entered, patient_last_name_entered, patient_dob_entered, patient_phone_number_entered, patient_gender_entered, patient_email_entered

    tk.Label(root, text="First Name:").pack()
    patient_first_name_entered = tk.Entry(root)
    patient_first_name_entered.pack()

    tk.Label(root, text="Last Name:").pack()
    patient_last_name_entered = tk.Entry(root)
    patient_last_name_entered.pack()

    tk.Label(root, text="Date Of Birth (YYYY-MM-DD):").pack()
    patient_dob_entered = tk.Entry(root)
    patient_dob_entered.pack()

    tk.Label(root, text="Gender (M/F):").pack()
    patient_gender_entered = tk.Entry(root)
    patient_gender_entered.pack()

    tk.Label(root, text="Email Address:").pack()
    patient_email_entered = tk.Entry(root)
    patient_email_entered.pack()

    tk.Label(root, text="Phone number:").pack()
    patient_phone_number_entered = tk.Entry(root)
    patient_phone_number_entered.pack()

    tk.Button(root, text="Submit", command=handle_patient_register).pack(pady=10)
    tk.Button(root, text="Back", command=show_admin_menu).pack()

def show_doctor_login():
    clear_window()
    tk.Label(root, text="Doctor Login", font=("Arial", 14)).pack(pady=10)

    global admin_id_entry, admin_password_entry
    tk.Label(root, text="Doctor ID:").pack()
    admin_id_entry = tk.Entry(root)
    admin_id_entry.pack()

    tk.Label(root, text="Password:").pack()
    admin_password_entry = tk.Entry(root, show="*")
    admin_password_entry.pack()

    tk.Button(root, text="Login", command=handle_doctor_login).pack(pady=10)
    tk.Button(root, text="Back to Menu", command=show_main_menu).pack()


def show_find_doctor_by_id():
    clear_window()
    tk.Label(root, text="Doctor Login", font=("Arial", 14)).pack(pady=10)


    global doctor_id_entry
    tk.Label(root, text="Doctor ID:").pack()
    doctor_id_entry = tk.Entry(root)
    doctor_id_entry.pack()

    tk.Button(root, text="Submit", command=handle_find_doctor_by_id).pack(pady=10)


def handle_find_doctor_by_id():
    pass


def show_doctor_menu():
    clear_window()
    tk.Label(root, text="Welcome Doctor", font=("Arial", 14)).pack(pady=10)
    tk.Button(root, text="View Profile", command=register_patient).pack(pady=5)
    tk.Button(root, text="View Appointments", command=register_doctor).pack(pady=5)
    tk.Button(root, text="Search Patient Profile", command=view_all_patient).pack(pady=5)
    tk.Button(root, text="Logout", command=show_main_menu).pack(pady=5)


def handle_doctor_login():
    show_doctor_menu()
    pass

def register_doctor():
    clear_window()
    tk.Label(root, text="Register Doctor", font=("Arial", 14)).pack(pady=10)

    tk.Label(root, text="Note: Only Nigerian Number is acceptable", font=("Arial", 10)).pack(pady=10)

    global doctor_password_enter, doctor_first_name_entered, doctor_last_name_entered,doctor_dob_entered, doctor_phone_number_entered
    tk.Label(root, text="Enter Password:").pack()
    doctor_password_enter = tk.Entry(root)
    doctor_password_enter.pack()

    tk.Label(root, text="First Name:").pack()
    doctor_first_name_entered = tk.Entry(root)
    doctor_first_name_entered.pack()

    tk.Label(root, text="Last Name:").pack()
    doctor_last_name_entered = tk.Entry(root)
    doctor_last_name_entered.pack()

    tk.Label(root, text="Date of Birth (YYYY-MM-DD):").pack()
    doctor_dob_entered = tk.Entry(root)
    doctor_dob_entered.pack()

    tk.Label(root, text="Phone Number:").pack()
    doctor_phone_number_entered = tk.Entry(root)
    doctor_phone_number_entered.pack()


    tk.Button(root, text="Submit",command=choose_specialization).pack(pady=10)
    tk.Button(root, text="Back", command=show_admin_menu).pack()



def handle_doctor_registration(specialization):
    try:
        admin.register_doctor(doctor_password_enter.get(), doctor_first_name_entered.get(), doctor_last_name_entered.get(), doctor_dob_entered, doctor_phone_number_entered.get(), specialization)
        messagebox.showinfo("Success", "Registration Successful.")
        show_admin_menu()
    except ValueError as e:
        messagebox.showerror("Registration Unsuccessful!", "Please check your input.\n" + str(e))


def choose_specialization():

    clear_window()
    tk.Label(root, text="SPECIALIZATION", font=("Arial", 14)).pack(pady=10)
    tk.Button(root, text="General Practitioner/Medical Officer", command=lambda: handle_doctor_registration("General Practitioner/Medical Officer")).pack(pady=5)
    tk.Button(root, text="Family Physician", command=lambda:handle_doctor_registration("Family Physician")).pack(pady=5)
    tk.Button(root, text="Internal Medicine Physician", command=lambda:handle_doctor_registration("Internal Medicine Physician")).pack(pady=5)
    tk.Button(root, text="Pediatrician", command=lambda: handle_doctor_registration("Pediatrician")).pack(pady=5)
    tk.Button(root, text="Obstetrician/Gynecologist",  command=lambda:handle_doctor_registration("Obstetrician/Gynecologist")).pack(pady=5)
    tk.Button(root, text="General Surgeon",  command=lambda:handle_doctor_registration("General Surgeon")).pack(pady=5)
    tk.Button(root, text="Orthopedic Surgeon",  command=lambda:handle_doctor_registration("Orthopedic Surgeon")).pack(pady=5)
    tk.Button(root, text="Anesthetist/Anesthesiologist",  command=lambda:handle_doctor_registration("Anesthetist/Anesthesiologist")).pack(pady=5)
    tk.Button(root, text="Psychiatrist",  command=lambda:handle_doctor_registration("Psychiatrist",)).pack(pady=5)
    tk.Button(root, text="Radiologist",  command=lambda:handle_doctor_registration("Radiologist")).pack(pady=5)
    tk.Button(root, text="Pathologist",  command=lambda:handle_doctor_registration("Pathologist")).pack(pady=5)
    tk.Button(root, text="ENT Specialist",  command=lambda:handle_doctor_registration("ENT Specialist")).pack(pady=5)
    tk.Button(root, text="Ophthalmologist",  command=lambda:handle_doctor_registration("Ophthalmologist")).pack(pady=5)
    tk.Button(root, text="Dermatologist",  command=lambda:handle_doctor_registration("Dermatologist",)).pack(pady=5)
    tk.Button(root, text="Urologist",  command=lambda:handle_doctor_registration("Urologist")).pack(pady=5)
    tk.Button(root, text="Emergency Medicine Doctor",  command=lambda:handle_doctor_registration("Emergency Medicine Doctor")).pack(pady=5)
    tk.Button(root, text="Public Health Physician",  command=lambda:handle_doctor_registration("Public Health Physician")).pack(pady=5)


def clear_window():
    for widget in root.winfo_children():
        widget.destroy()


root = tk.Tk()
root.title("Hospital Management System")
root.geometry("500x700")

show_main_menu()

root.mainloop()
