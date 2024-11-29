import time
from Model import Model
from View import View


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()

    def run(self):
        while True:
            choice = self.view.show_menu()

            if choice == '7':
                break
            if choice == '6':
                self.process_search_option()
            elif choice in ['1', '2', '3', '4', '5']:
                self.process_menu_choice(choice)
            else:
                self.view.show_message("Wrong choice. Try again.")

    def process_menu_choice(self, choice):
        while True:
            table = self.view.show_tables()

            if table == '6':
                break

            if choice == '1':
                self.process_add_option(table)
            elif choice == '2':
                self.process_add_random_option(table)
            elif choice == '3':
                self.process_view_option(table)
            elif choice == '4':
                self.process_update_option(table)
            elif choice == '5':
                self.process_delete_option(table)
            else:
                self.view.show_message("Wrong choice. Try again.")

    def process_add_option(self, table):
        if table == '1':
            self.view.show_message("\nAdding patient:")
            self.add_patient()
        elif table == '2':
            self.view.show_message("\nAdding medication:")
            self.add_medication()
        elif table == '3':
            self.view.show_message("\nAdding medical record:")
            self.add_medical_record()
        elif table == '4':
            self.view.show_message("\nAdding medical specialist task:")
            self.add_medical_specialist()
        elif table == '5':
            self.view.show_message("\nAdding specialist record task:")
            self.add_specialist_record()
        elif table == '6':
            self.view.show_menu()
        else:
            self.view.show_message("Wrong choice. Try again.")

    def process_add_random_option(self, table):
        if table == '1':
            self.view.show_message("\nAdding random patient:")
            self.add_random_fields()
        else:
            self.view.show_message("Wrong choice. Try again.")

    def process_view_option(self, table):
        if table == '1':
            self.show_patient()
        elif table == '2':
            self.show_medication()
        elif table == '3':
            self.show_medical_record()
        elif table == '4':
            self.show_medical_specialist()
        elif table == '5':
            self.show_specialist_record()
        elif table == '6':
            self.view.show_menu()
        else:
            self.view.show_message("Wrong choice. Try again.")

    def process_update_option(self, table):
        if table == '1':
            self.view.show_message("\nUpdating patient:")
            self.update_patient()
        elif table == '2':
            self.view.show_message("\nUpdating medication:")
            self.update_medication()
        elif table == '3':
            self.view.show_message("\nUpdating medical record:")
            self.update_medical_record()
        elif table == '4':
            self.view.show_message("\nUpdating medical specialist:")
            self.update_medical_specialist()
        elif table == '5':
            self.view.show_message("\nUpdating specialist record:")
            self.update_specialist_record()
        elif table == '6':
            self.view.show_menu()
        else:
            self.view.show_message("Wrong choice. Try again.")

    def process_delete_option(self, table):
        if table == '1':
            self.view.show_message("\nDeleting patient:")
            self.delete_patient()
        elif table == '2':
            self.view.show_message("\nDeleting medication:")
            self.delete_medication()
        elif table == '3':
            self.view.show_message("\nDeleting medical record:")
            self.delete_medical_record()
        elif table == '4':
            self.view.show_message("\nDeleting medical specialist:")
            self.delete_medical_specialist()
        elif table == '5':
            self.view.show_message("\nDeleting specialist record:")
            self.delete_specialist_record()
        else:
            self.view.show_message("Wrong choice. Try again.")

    import time

    def process_search_option(self):
        option = self.view.show_search()

        if option == '1':
            start_time = time.time()
            self.show_number_of_records_per_patient()
            end_time = time.time()
            elapsed_time = (end_time - start_time) * 1000
            print(f"Execution time: {elapsed_time:.2f} msec")
        elif option == '2':
            start_time = time.time()
            self.show_specialist_record_patient()
            end_time = time.time()
            elapsed_time = (end_time - start_time) * 1000
            print(f"Execution time: {elapsed_time:.2f} msec")
        elif option == '3':
            start_time = time.time()
            self.show_upcoming_patient_visits()
            end_time = time.time()
            elapsed_time = (end_time - start_time) * 1000
            print(f"Execution time: {elapsed_time:.2f} msec")
        else:
            self.view.show_menu()

    def add_patient(self):
        try:
            id, full_name, age, contact_info = self.view.get_patient_input()
            self.model.add_patient(id, full_name, age, contact_info)
            self.view.show_message("Patient added successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def add_medication(self):
        try:
            id, id_patient, name, dosage_form, side_effect = self.view.get_medication_input()
            self.model.add_medication(id, id_patient, name, dosage_form, side_effect)
            self.view.show_message("Medication added successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def add_medical_record(self):
        try:
            id, id_patient, visit_date, diagnosis, symptoms = self.view.get_medical_record_input()
            self.model.add_medical_record(id, id_patient, visit_date, diagnosis, symptoms)
            self.view.show_message("Medical record added successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def add_medical_specialist(self):
        try:
            id, full_name, qualification, work_experience, contact_info = self.view.get_medical_specialist_input()
            self.model.add_medical_specialist(id, full_name, qualification, work_experience, contact_info)
            self.view.show_message("Medical specialist added successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def add_specialist_record(self):
        try:
            id, id_specialist, id_record = self.view.get_specialist_record_input()
            self.model.add_specialist_record(id, id_specialist, id_record)
            self.view.show_message("Specialist record added successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def show_patient(self):
        try:
            patient = self.model.get_patient()
            self.view.show_patient(patient)
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def show_medication(self):
        try:
            medication = self.model.get_medication()
            self.view.show_medication(medication)
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def show_medical_record(self):
        try:
            medical_record = self.model.get_medical_record()
            self.view.show_medical_record(medical_record)
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def show_medical_specialist(self):
        try:
            medical_specialist = self.model.get_medical_specialist()
            self.view.show_medical_specialist(medical_specialist)
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def show_specialist_record(self):
        try:
            specialist_record = self.model.get_specialist_record()
            self.view.show_specialist_record(specialist_record)
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def update_patient(self):
        try:
            id_new = self.view.get_patient_id()
            id, full_name, age, contact_info = self.view.get_patient_input()
            self.model.update_patient(id, full_name, age, contact_info, id_new)
            self.view.show_message("Patient updated successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def update_medication(self):
        try:
            id_new = self.view.get_medication_id()
            id, id_patient, name, dosage_form, side_effect = self.view.get_medication_input()
            self.model.update_medication(id, id_patient, name, dosage_form, side_effect, id_new)
            self.view.show_message("Medication updated successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def update_medical_record(self):
        try:
            id_new = self.view.get_medical_record_id()
            id, id_patient, visit_date, diagnosis, symptoms = self.view.get_medical_record_input()
            self.model.update_medical_record(id, id_patient, visit_date, diagnosis, symptoms, id_new)
            self.view.show_message("Medical record updated successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def update_medical_specialist(self):
        try:
            id_new = self.view.get_medical_specialist_id()
            id, full_name, qualification, work_experience, contact_info = self.view.get_medical_specialist_input()
            self.model.update_medical_specialist(id, full_name, qualification, work_experience, contact_info, id_new)
            self.view.show_message("Medical specialist updated successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def update_specialist_record(self):
        try:
            id_new = self.view.get_specialist_record_id()
            id, id_specialist, id_record = self.view.get_specialist_record_input()
            self.model.update_specialist_record(id, id_specialist, id_record, id_new)
            self.view.show_message("Specialist record updated successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def delete_patient(self):
        try:
            id = self.view.get_patient_id()
            self.model.delete_patient(id)
            self.view.show_message("Patient deleted successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def delete_medication(self):
        try:
            id = self.view.get_medication_id()
            self.model.delete_medication(id)
            self.view.show_message("Medication deleted successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def delete_medical_record(self):
        try:
            id = self.view.get_medical_record_id()
            self.model.delete_medical_record(id)
            self.view.show_message("Medical record deleted successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def delete_medical_specialist(self):
        try:
            id = self.view.get_medical_specialist_id()
            self.model.delete_medical_specialist(id)
            self.view.show_message("Medical specialist deleted successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def delete_specialist_record(self):
        try:
            id = self.view.get_specialist_record_id()
            self.model.delete_specialist_record(id)
            self.view.show_message("Specialist record deleted successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def show_number_of_records_per_patient(self):
        try:
            records_per_patient = self.model.get_number_of_records_per_patient()
            self.view.show_number_of_records_per_patient(records_per_patient)
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def show_specialist_record_patient(self):
        try:
            specialist_record_patient = self.model.get_specialist_record_patient()
            self.view.show_specialist_record_patient(specialist_record_patient)
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def show_upcoming_patient_visits(self):
        try:
            upcoming_patient_visits = self.model.get_upcoming_patient_visits()
            self.view.show_upcoming_patient_visits(upcoming_patient_visits)
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")

    def add_random_fields(self):
        try:
            number = self.view.get_number()
            self.model.add_random_fields(number)
            self.view.show_message("Random fields added successfully!")
        except Exception as e:
            self.view.show_message(f"Something went wrong: {e}")