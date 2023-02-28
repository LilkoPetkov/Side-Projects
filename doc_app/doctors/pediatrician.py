from sql_lite.doc_app.doctors.doctor import Doctor


class Pediatrician(Doctor):
    def __init__(self, name, phone_number, hospital, description):
        super().__init__(name, phone_number, hospital, description)

    def add_appointments(self, *args):
        for arg in args:
            self.appointments.append(arg)


P = Pediatrician("Emil Mihailov", "0876597885", "MediHope", "Doctors, also known as physicians, are licensed health\
 professionals who maintain and restore human health through the practice of medicine")

P.add_appointments("10:30 - Anita Petrova", "11:40 - Lilko Petkov", "12:50 - Ivan Petkov")
