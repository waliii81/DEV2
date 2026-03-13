from employe import Employe
from voiture import Voiture

e1 = Employe("P001", "walid", "lahsaien")
e2 = Employe("P006", "taha", "amine")
e3 = Employe("P009", "sarah", "bikk")

v1 = Voiture("FR098", "Renault", 2022, 15000)
v2 = Voiture("MA7573", "Peugeot", 2023, 5000)
v3 = Voiture("MA346", "Citroen", 2021, 30000)

print("INITIAL")

e1.afficherInformations()
e2.afficherInformations()
e3.afficherInformations()

v1.afficherInformations()
v2.afficherInformations()
v3.afficherInformations()

print("ATTRIBUTION")

e1.affecterVoiture(v1)
e2.affecterVoiture(v2)

e1.afficherInformations()
e2.afficherInformations()
v1.afficherInformations()
v2.afficherInformations()

print("RETRAIT")

e1.retirerVoiture()

e1.afficherInformations()
v1.afficherInformations()

print("ATTRIBUTION IMPOSSIBLE")

e3.affecterVoiture(v2)

e2.afficherInformations()
e3.afficherInformations()
v2.afficherInformations()