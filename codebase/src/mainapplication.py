from administration import Admin
import tkinter as tk
from tkinter import messagebox

admin = Admin()

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


def handle_admin_login():
    admin_id = admin_id_entry.get()
    password = admin_password_entry.get()
    if admin_id and password == "<PASSWORD>":
        messagebox.showinfo("Login Successful", "Welcome, Administrator!")
        show_admin_menu()
    else:
        messagebox.showerror("Login Failed", "Invalid credentials.")

def show_main_menu():
    clear_window()
    tk.Label(root, text="Welcome to \nJBL General Hospital", font=("Arial", 16), pady=10).pack()

    tk.Button(root, text="Login as Administrator", width=30, command=show_admin_login).pack(pady=5)
    tk.Button(root, text="Login as Doctor", width=30, command=handle_doctor_login).pack(pady=5)
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

def show_admin_menu():
    clear_window()
    tk.Label(root, text="Admin Menu", font=("Arial", 14)).pack(pady=10)
    tk.Button(root, text="Register New Patient", command=register_patient).pack(pady=5)
    tk.Button(root, text="Register New Doctor", command=register_doctor).pack(pady=5)
    tk.Button(root, text="View All Patients", command=view_all_patient).pack(pady=5)
    tk.Button(root, text="View All Doctor", command=register_doctor).pack(pady=5)
    tk.Button(root, text="Update Patient Information", command=register_doctor).pack(pady=5)
    tk.Button(root, text="Update Doctor Information", command=register_doctor).pack(pady=5)
    tk.Button(root, text="Find Doctor by ID", command=register_doctor).pack(pady=5)
    tk.Button(root, text="Find Patient by ID", command=register_doctor).pack(pady=5)
    tk.Button(root, text="Print Schedule Report", command=register_doctor).pack(pady=5)


    tk.Button(root, text="Logout", command=show_main_menu).pack(pady=5)

def handle_patient_register():
    title = title_enter.get()
    first_name = patient_first_name_entered.get()
    last_name = patient_last_name.get()
    year_of_birth = int(patient_year_of_birth.get())
    month_of_birth = int(patient_month_of_birth.get())
    day_of_birth = int(patient_day_of_birth.get())
    phone_number = patient_phone_number.get()
    try:
        admin.register_patient(title, first_name, last_name, year_of_birth, month_of_birth, day_of_birth, phone_number)
        messagebox.showinfo("Success", "Registration Successful.")
        show_admin_menu()
    except ValueError as e:
        messagebox.showerror("Registration Unsuccessful!", "Please check your input.\n" + str(e))


def register_patient():
    clear_window()
    tk.Label(root, text="Register Patient", font=("Arial", 14)).pack(pady=10)

    global title_enter, patient_first_name_entered, patient_last_name, patient_year_of_birth, patient_month_of_birth, patient_day_of_birth, patient_phone_number
    tk.Label(root, text="Title:").pack()
    title_enter = tk.Entry(root)
    title_enter.pack()

    tk.Label(root, text="First Name:").pack()
    patient_first_name_entered = tk.Entry(root)
    patient_first_name_entered.pack()

    tk.Label(root, text="Last Name:").pack()
    patient_last_name = tk.Entry(root)
    patient_last_name.pack()

    tk.Label(root, text="Year of birth:").pack()
    patient_year_of_birth = tk.Entry(root)
    patient_year_of_birth.pack()

    tk.Label(root, text="Month of birth:").pack()
    patient_month_of_birth = tk.Entry(root)
    patient_month_of_birth.pack()

    tk.Label(root, text="Day of birth:").pack()
    patient_day_of_birth = tk.Entry(root)
    patient_day_of_birth.pack()

    tk.Label(root, text="Phone number:").pack()
    patient_phone_number = tk.Entry(root)
    patient_phone_number.pack()

    tk.Button(root, text="Submit", command=handle_patient_register).pack(pady=10)
    tk.Button(root, text="Back", command=show_admin_menu).pack()

def handle_doctor_login():
    pass

def register_doctor():
    clear_window()
    tk.Label(root, text="Register Doctor", font=("Arial", 14)).pack(pady=10)

    global doctor_password_enter, doctor_first_name_entered, doctor_last_name_entered, doctor_specialization_entered, doctor_phone_number_entered
    tk.Label(root, text="Enter Password:").pack()
    doctor_password_enter = tk.Entry(root)
    doctor_password_enter.pack()

    tk.Label(root, text="First Name:").pack()
    doctor_first_name_entered = tk.Entry(root)
    doctor_first_name_entered.pack()

    tk.Label(root, text="Last Name:").pack()
    doctor_last_name_entered = tk.Entry(root)
    doctor_last_name_entered.pack()

    tk.Label(root, text="Specialization:").pack()
    doctor_specialization_entered = tk.Entry(root)
    doctor_specialization_entered.pack()

    tk.Label(root, text="Phone Number:").pack()
    doctor_phone_number_entered = tk.Entry(root)
    doctor_phone_number_entered.pack()


    tk.Button(root, text="Submit", command=handle_doctor_registration).pack(pady=10)
    tk.Button(root, text="Back", command=show_admin_menu).pack()



def handle_doctor_registration():
    try:
        admin.register_doctor(doctor_password_enter.get(), doctor_first_name_entered.get(), doctor_last_name_entered.get(), doctor_specialization_entered.get(), doctor_phone_number_entered.get())
        messagebox.showinfo("Success", "Registration Successful.")
        show_admin_menu()
    except ValueError as e:
        messagebox.showerror("Registration Unsuccessful!", "Please check your input.\n" + str(e))

def clear_window():
    for widget in root.winfo_children():
        widget.destroy()


root = tk.Tk()
root.title("Hospital Management System")
root.geometry("300x450")

show_main_menu()

root.mainloop()
