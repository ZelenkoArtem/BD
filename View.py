from datetime import datetime


class View:

    def show_menu(self):
        self.show_message("\nMenu:")
        self.show_message("1. Add row")
        self.show_message('2. Generating `randomized` data (only for "Patient")')
        self.show_message("3. Show table")
        self.show_message("4. Update row")
        self.show_message("5. Delete row")
        self.show_message("6. Search")
        self.show_message("7. Exit")
        choice = input("Select your choice: ")
        return choice

    def show_tables(self):
        self.show_message("\nTables:")
        self.show_message("1. Patient")
        self.show_message("2. Medication")
        self.show_message("3. Medical record")
        self.show_message("4. Medical specialist")
        self.show_message("5. Specialist record")
        self.show_message("6. Back to menu")
        table = input("Select table: ")
        return table

    def show_search(self):
        self.show_message("\nSearch:")
        self.show_message("1. Number of records for each patient")
        self.show_message("2. Specialist's name, diagnosis, and corresponding patient records.")
        self.show_message("3. Upcoming patient visits.")
        self.show_message("4. Back to menu")
        choice = input("Select something: ")
        return choice


    def show_patient(self, patient):
        print("\nPatient:")
        for pat in patient:
            print(f"Patient ID: {pat[0]}, Full name: {pat[1]}, Age: {pat[2]}, Contact info: {pat[3]}")

    def show_medication(self, medication):
        print("\nMedication:")
        for med in medication:
            print(f"Medication ID: {med[0]}, Name: {med[1]}, Dosage form: {med[2]}, Side effect: {med[3]}")

    def show_medical_record(self, medical_record):
        print("\nMedical record:")
        for record in medical_record:
            print(f"Medical record ID: {record[0]}, ID patient: {record[1]}, Visit date: {record[2]}, Diagnosis: {record[3]}, Symptoms: {record[4]}")

    def show_medical_specialist(self, medical_specialist):
        print("\nMedical specialist:")
        for specialist in medical_specialist:
            print(f"Medical specialist ID: {specialist[0]}, Full name: {specialist[1]}, Qualification: {specialist[2]}, Work experience: {specialist[3]}, Contact info: {specialist[4]}")

    def show_specialist_record(self, specialist_record):
        print("\nSpecialist record:")
        for specialist in specialist_record:
            print(f"Specialist record ID: {specialist[0]}, Specialist ID: {specialist[1]}, Record ID: {specialist[2]}")

    def get_patient_input(self):
        while True:
            try:
                id = input("Enter patient ID: ")
                if id.strip():
                    id = int(id)
                    break
                else:
                    print("Patient ID cannot be empty.")
            except ValueError:
                print("It must be a number.")
        while True:
            try:
                full_name = input("Enter full name: ")
                if full_name.strip():
                    break
                else:
                    print("Full name cannot be empty.")
            except ValueError:
                print("It must be a string.")
        while True:
            try:
                age = input("Enter age: ")
                if age.strip():
                    age = int(age)
                    break
                else:
                    print("Age cannot be empty.")
            except ValueError:
                print("It must be a number.")
        while True:
            try:
                contact_info = input("Enter contact info: ")
                if contact_info.strip():
                    break
                else:
                    print("Contact info cannot be empty.")
            except ValueError:
                print("It must be a string.")
        return id, full_name, age, contact_info


    def get_medication_input(self):
        while True:
            try:
                id = input("Enter Medication ID: ")
                if id.strip():
                    id = int(id)
                    break
                else:
                    print("Medication ID cannot be empty.")
            except ValueError:
                print("It must be a number.")
        while True:
            try:
                id_patient = input("Enter id patient: ")
                if id_patient.strip():
                    id_patient = int(id_patient)
                    break
                else:
                    print("ID patient cannot be empty.")
            except ValueError:
                print("It must be a number.")
        while True:
            try:
                name = input("Enter name: ")
                if name.strip():
                    break
                else:
                    print("Name cannot be empty.")
            except ValueError:
                print("It must be a string.")
        while True:
            try:
                dosage_form = input("Enter dosage form: ")
                if dosage_form.strip():
                    break
                else:
                    print("Dosage form cannot be empty.")
            except ValueError:
                print("It must be a string.")
        while True:
            try:
                side_effect = input("Enter side effect: ")
                if side_effect.strip():
                    break
                else:
                    print("Side effect cannot be empty.")
            except ValueError:
                print("It must be a string.")
        return id, id_patient, name, dosage_form, side_effect


    def get_medical_record_input(self):
        while True:
            try:
                id = input("Enter medical record ID: ")
                if id.strip():
                    id = int(id)
                    break
                else:
                    print("Medical record ID cannot be empty.")
            except ValueError:
                print("It must be a number.")
        while True:
            try:
                id_patient = input("Enter Patient ID: ")
                if id_patient.strip():
                    id_patient = int(id_patient)
                    break
                else:
                    print("Patient ID cannot be empty.")
            except ValueError:
                print("It must be a number.")
        while True:
            try:
                visit_date = input("Enter state visit date (YYYY-MM-DD): ")
                if visit_date.strip():
                    datetime.strptime(visit_date, "%Y-%m-%d")
                    break
                else:
                    print("State visit date cannot be empty.")
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
        while True:
            try:
                diagnosis = input("Enter diagnosis: ")
                if diagnosis.strip():
                    break
                else:
                    print("Diagnosis cannot be empty.")
            except ValueError:
                print("It must be a string.")
        while True:
            try:
                symptoms = input("Enter symptoms: ")
                if symptoms.strip():
                    break
                else:
                    print("Symptoms cannot be empty.")
            except ValueError:
                print("It must be a string.")
        return id, id_patient, visit_date, diagnosis, symptoms

    def get_medical_specialist_input(self):
        while True:
            try:
                id = input("Enter medical specialist ID: ")
                if id.strip():
                    id = int(id)
                    break
                else:
                    print("Medical specialist ID cannot be empty.")
            except ValueError:
                print("It must be a number.")
        while True:
            try:
                full_name = input("Enter full name: ")
                if full_name.strip():
                    break
                else:
                    print("Full name cannot be empty.")
            except ValueError:
                print("It must be a string.")
        while True:
            try:
                qualification = input("Enter qualification: ")
                if qualification.strip():
                    break
                else:
                    print("Qualification cannot be empty.")
            except ValueError:
                print("It must be a string.")
        while True:
            try:
                work_experience = input("Enter work_experience: ")
                if work_experience.strip():
                    work_experience = int(work_experience)
                    break
                else:
                    print("Work_experience cannot be empty.")
            except ValueError:
                print("It must be a number.")
        while True:
            try:
                contact_info = input("Enter contact info: ")
                if contact_info.strip():
                    break
                else:
                    print("Contact info cannot be empty.")
            except ValueError:
                print("It must be a string.")
        return id, full_name, qualification, work_experience, contact_info

    def get_specialist_record_input(self):
        while True:
            try:
                id = input("Enter specialist record ID: ")
                if id.strip():
                    id = int(id)
                    break
                else:
                    print("Specialist record ID cannot be empty.")
            except ValueError:
                print("It must be a number.")
        while True:
            try:
                id_specialist = input("Enter specialist ID: ")
                if id_specialist.strip():
                    id_specialist = int(id_specialist)
                    break
                else:
                    print("Specialist ID cannot be empty.")
            except ValueError:
                print("It must be a number.")
        while True:
            try:
                id_record = input("Enter record ID: ")
                if id_record.strip():
                    id_record = int(id_record)
                    break
                else:
                    print("Record ID cannot be empty.")
            except ValueError:
                print("It must be a number.")
        return id, id_specialist, id_record

    def get_patient_id(self):
        while True:
            try:
                id = int(input("Enter patient ID: "))
                break
            except ValueError:
                print("It must be a number.")
        return id

    def get_medication_id(self):
        while True:
            try:
                id = int(input("Enter medication ID: "))
                break
            except ValueError:
                print("It must be a number.")
        return id

    def get_medical_record_id(self):
        while True:
            try:
                id = int(input("Enter medical record ID: "))
                break
            except ValueError:
                print("It must be a number.")
        return id

    def get_medical_specialist_id(self):
        while True:
            try:
                id = int(input("Enter medical specialist ID: "))
                break
            except ValueError:
                print("It must be a number.")
        return id

    def get_specialist_record_id(self):
        while True:
            try:
                id = int(input("Enter specialist record ID: "))
                break
            except ValueError:
                print("It must be a number.")
        return id

    def show_number_of_records_per_patient(self, rows):
        print("\nNumber of medical records for each patient:")
        for row in rows:
            print(f"Patient ID: {row[0]}, Full Name: {row[1]}, Total records: {row[2]}")

    def show_specialist_record_patient(self, rows):
        print("\nSpecialist's name, patient diagnosis, and corresponding patient's records:")
        for row in rows:
            print(f"Specialist name: {row[2]}, Patient diagnosis: {row[1]}, Patient's medical record ID: {row[0]}")

    def show_upcoming_patient_visits(self, rows):
        print("\nUpcoming patient visits:")
        for row in rows:
            print(f"Patient ID: {row[0]}, Full Name: {row[1]}, Visit Date: {row[2]}")

    def show_message(self, message):
        print(message)

    def get_number(self):
        while True:
            try:
                number = int(input("Enter the number: "))
                break
            except ValueError:
                print("It must be a number.")
        return number