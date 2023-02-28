from sql_lite.doc_app.doctors.doctor import Doctor


class Radiologist(Doctor):
    def __init__(self, name, phone_number, hospital, description):
        super().__init__(name, phone_number, hospital, description)

    def add_appointments(self, *args):
        for arg in args:
            self.appointments.append(arg)


R = Radiologist("Anita Petrova", "0876597555", "MediHope", "Doctors, also known as physicians, are licensed health\
 professionals who maintain and restore human health through the practice of medicine")

R.add_appointments("10:30 - Anita Petrova", "11:40 - Lilko Petkov", "12:50 - Ivan Petkov")
