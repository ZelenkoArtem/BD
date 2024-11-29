import psycopg2


class Model:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname='postgres',
            user='postgres',
            password='qwerty',
            host='localhost',
            port=5432
        )

    def add_patient(self, id, full_name, age, contact_info):
        c = self.conn.cursor()
        c.execute('INSERT INTO patient(id, full_name, age, contact_info) VALUES(%s, %s, %s, %s);',
                  (id, full_name, age, contact_info))
        self.conn.commit()

    def add_medication(self, id, id_patient, name, dosage_form, side_effect):
        c = self.conn.cursor()
        c.execute('INSERT INTO medication(id, id_patient, name, dosage_form, side_effect) VALUES(%s, %s, %s, %s, %s);',
                  (id, id_patient, name, dosage_form, side_effect))
        self.conn.commit()

    def add_medical_record(self, id, id_patient, visit_date, diagnosis, symptoms):
        c = self.conn.cursor()
        c.execute('INSERT INTO medical_record(id, id_patient, visit_date, diagnosis, symptoms) VALUES(%s, %s, %s, %s, %s);',
                  (id, id_patient, visit_date, diagnosis, symptoms))
        self.conn.commit()

    def add_medical_specialist(self, id, full_name, qualification, work_experience, contact_info):
        c = self.conn.cursor()
        c.execute('INSERT INTO medical_specialist(id, full_name, qualification, work_experience, contact_info) VALUES(%s, %s, %s, %s, %s);',
                  (id, full_name, qualification, work_experience, contact_info))
        self.conn.commit()

    def add_specialist_record(self, id, id_specialist, id_record):
        c = self.conn.cursor()
        c.execute('INSERT INTO specialist_record(id, id_specialist, id_record) VALUES(%s, %s, %s);',
                  (id, id_specialist, id_record))
        self.conn.commit()

    def get_patient(self):
        c = self.conn.cursor()
        c.execute('SELECT * FROM patient;')
        return c.fetchall()

    def get_medication(self):
        c = self.conn.cursor()
        c.execute('SELECT * FROM medication;')
        return c.fetchall()

    def get_medical_record(self):
        c = self.conn.cursor()
        c.execute('SELECT * FROM medical_record;')
        return c.fetchall()

    def get_medical_specialist(self):
        c = self.conn.cursor()
        c.execute('SELECT * FROM medical_specialist;')
        return c.fetchall()

    def get_specialist_record(self):
        c = self.conn.cursor()
        c.execute('SELECT * FROM specialist_record;')
        return c.fetchall()

    def update_patient(self, id, full_name, age, contact_info, id_new):
        c = self.conn.cursor()
        c.execute('UPDATE patient SET id=%s, full_name=%s, age=%s, contact_info=%s WHERE id=%s',
                  (id, full_name, age, contact_info, id_new))
        self.conn.commit()

    def update_medication(self, id, id_patient, name, dosage_form, side_effect, id_new):
        c = self.conn.cursor()
        c.execute('UPDATE medication SET id=%s, id_patient=%s, name=%s, dosage_form=%s, side_effect=%s WHERE id=%s',
                  (id, id_patient, name, dosage_form, side_effect, id_new))
        self.conn.commit()

    def update_medical_record(self, id, id_patient, visit_date, diagnosis, symptoms, id_new):
        c = self.conn.cursor()
        c.execute('UPDATE medical_record SET id=%s, id_patient=%s, visit_date=%s, diagnosis=%s, symptoms=%s WHERE id=%s',
                  (id, id_patient, visit_date, diagnosis, symptoms, id_new))
        self.conn.commit()

    def update_medical_specialist(self, id, full_name, qualification, work_experience, contact_info, id_new):
        c = self.conn.cursor()
        c.execute('UPDATE medical_specialist SET id=%s, full_name=%s, qualification=%s, work_experience=%s, contact_info=%s WHERE id=%s',
                  (id, full_name, qualification, work_experience, contact_info, id_new))
        self.conn.commit()

    def update_specialist_record(self, id, id_specialist, id_record, id_new):
        c = self.conn.cursor()
        c.execute('UPDATE specialist_record SET id=%s, id_specialist=%s, id_record=%s WHERE id=%s',
                  (id, id_specialist, id_record, id_new))
        self.conn.commit()

    def delete_patient(self, id):
        c = self.conn.cursor()
        c.execute('DELETE FROM patient WHERE "id"=%s', (id,))
        self.conn.commit()

    def delete_medication(self, id):
        c = self.conn.cursor()
        c.execute('DELETE FROM medication WHERE "id"=%s', (id,))
        self.conn.commit()

    def delete_medical_record(self, id):
        c = self.conn.cursor()
        c.execute('DELETE FROM medical_record WHERE "id"=%s', (id,))
        self.conn.commit()

    def delete_medical_specialist(self, id):
        c = self.conn.cursor()
        c.execute('DELETE FROM medical_specialist WHERE "id"=%s', (id,))
        self.conn.commit()

    def delete_specialist_record(self, id):
        c = self.conn.cursor()
        c.execute('DELETE FROM specialist_record WHERE "id"=%s', (id,))
        self.conn.commit()

    def get_number_of_records_per_patient(self):
        c = self.conn.cursor()
        c.execute('SELECT p.id AS patient_id, p.full_name, COUNT(mr.id) AS total_records '
                  'FROM patient p '
                  'LEFT JOIN medical_record mr ON p.id = mr.id_patient '
                  'GROUP BY p.id, p.full_name;')
        return c.fetchall()

    def get_specialist_record_patient(self):
        c = self.conn.cursor()
        c.execute(
            'SELECT DISTINCT mr.id AS record_id, mr.diagnosis, ms.full_name AS specialist_name, p.full_name AS patient_name '
            'FROM medical_record mr '
            'JOIN specialist_record sr ON mr.id = sr.id_record '
            'JOIN medical_specialist ms ON sr.id_specialist = ms.id '
            'JOIN patient p ON mr.id_patient = p.id;')
        return c.fetchall()

    def get_upcoming_patient_visits(self):
        c = self.conn.cursor()
        c.execute('SELECT p.full_name AS patient_name, mr.visit_date, mr.diagnosis '
                  'FROM medical_record mr '
                  'JOIN patient p ON mr.id_patient = p.id '
                  'WHERE mr.visit_date >= CURRENT_DATE '
                  'ORDER BY mr.visit_date LIMIT 5;')
        return c.fetchall()

    def add_random_fields(self, number):
        c = self.conn.cursor()
        c.execute("""
            INSERT INTO patient (id, full_name, age, contact_info)
            SELECT 
                row_number() OVER () + COALESCE((SELECT MAX(id) FROM patient), 0), 
                chr(trunc(65 + random() * 26)::int) || chr(trunc(65 + random() * 26)::int) || ' ' || 
                chr(trunc(65 + random() * 26)::int) || chr(trunc(65 + random() * 26)::int), 
                trunc(18 + random() * 62)::int, 
                'contact' || trunc(random() * 1000)::int || '@example.com'
            FROM generate_series(1, %s);
        """, (number,))
        self.conn.commit()
