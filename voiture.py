class Voiture:

    def __init__(self, matricule, marque, annee, kilometrage):
        self.matricule = matricule
        self.marque = marque
        self.annee = annee
        self.kilometrage = kilometrage
        self.chauffeur = None

    def afficherInformations(self):

        print(f"Voiture: {self.marque} {self.annee} {self.kilometrage}km")

        if self.chauffeur:
            print("Chauffeur:", self.chauffeur.prenom)