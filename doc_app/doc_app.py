import os
from sql_lite.doc_app.doctors.doctor import Doctor
from sql_lite.doc_app.doctors.pediatrician import Pediatrician
from sql_lite.doc_app.doctors.psychiatrist import Psychiatrist
from sql_lite.doc_app.doctors.radiologist import Radiologist
import sqlite3


class DocApp:
    def __init__(self):
        self.doctors = []

    def add_doctor(self, doctor: Doctor):
        for doc in self.doctors:
            if doctor.name == doc.name and doctor.phone_number == doc.phone_number:
                raise Exception(f"Doctor {doctor.name} - {doctor.phone_number} already exists in our database.")

        if doctor.__class__.__name__ == "Pediatrician":
            self.doctors.append(doctor)
        elif doctor.__class__.__name__ == "Radiologist":
            self.doctors.append(doctor)
        elif doctor.__class__.__name__ == "Psychiatrist":
            self.doctors.append(doctor)

        return f"Doctor {doctor.name} was successfully added."

    def remove_doctor(self, name, phone_number):
        current_doc = None

        for d in self.doctors:
            if d.name == name and d.phone_number == phone_number:
                current_doc = d

        if not current_doc:
            raise Exception("Doctor does not exist in the database!")

        name = current_doc.name
        phone_number = current_doc.phone_number

        self.doctors.remove(current_doc)
        return f"Doctor {name} - {phone_number} was successfully removed."

    def add_to_db(self, name, phone_number):
        connection = sqlite3.connect("doctors.db")
        cursor = connection.cursor()

        try:
            cursor.execute("create table docs (doc_name VARCHAR(255), doc_phone text UNIQUE, doc_hospital text, doc_description "
                           "VARCHAR(255), doc_appointments text)")
            print("Table docs created")
        except sqlite3.OperationalError:
            pass

        doc_name, doc_phone, hospital, description, appointments = None, None, None, None, None

        for d in self.doctors:
            if name == d.name and phone_number == d.phone_number:
                doc_name = d.name
                doc_phone = d.phone_number
                hospital = d.hospital
                description = d.description
                appointments = ' '.join(d.appointments)

        if not doc_name:
            raise Exception("Doctor could not be added to the database, as it does not exist. \
Please do try to add it again")

        as_lst = [
            (doc_name, doc_phone, hospital, description, appointments)
        ]

        cursor.executemany("insert into docs values (?, ?, ?, ?, ?)", as_lst)

        result = []

        for row in cursor.execute("select * from docs"):
            result.append(row)  # -> Get everything from the database without specific filter

        connection.commit()
        connection.close()

        return result

    @staticmethod
    def database_status():
        connection = sqlite3.connect("doctors.db")
        cursor = connection.cursor()

        result = []

        for row in cursor.execute("select * from docs"):
            result.append(row)  # -> Get everything from the database without specific filter

        connection.close()

        return result


D = DocApp()

P = Pediatrician("E M", "1258158", "MH", "Doctors, also known as physicians, are licensed health\
 professionals who maintain and restore human health through the practice of medicine")

D.add_doctor(P)

connection = sqlite3.connect("doctors.db")
cursor = connection.cursor()

for row in cursor.execute("select * from docs"):
    print(row)


