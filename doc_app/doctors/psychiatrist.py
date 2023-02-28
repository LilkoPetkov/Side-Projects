from sql_lite.doc_app.doctors.doctor import Doctor


class Psychiatrist(Doctor):
    def __init__(self, name, phone_number, hospital, description):
        super().__init__(name, phone_number, hospital, description)

    def add_appointments(self, *args):
        for arg in args:
            self.appointments.append(arg)


P = Psychiatrist("Emily Stefanova", "0876578885", "MediHope", "A psychiatrist is a physician who specializes in\
 psychiatry, the branch of medicine devoted to the diagnosis, prevention, study, and treatment of mental disorders.")

P.add_appointments("10:30 - Anita Petrova", "11:40 - Lilko Petkov", "12:50 - Ivan Petkov")
