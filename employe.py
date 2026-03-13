class Employe:
    def __init__(self, numeroPermis, nom, prenom):
        self.numeroPermis = numeroPermis
        self.nom = nom
        self.prenom = prenom
        self.voitureService = None

    def afficherInformations(self):
        print(f"Employe: {self.prenom} {self.nom}")

        if self.voitureService:
            print("Voiture:", self.voitureService.marque)

    def affecterVoiture(self, voiture):

        if self.voitureService is not None:
            print("Cet employe a deja une voiture")
            return

        if voiture.chauffeur is not None:
            print("Cette voiture est deja attribuee")
            return

        self.voitureService = voiture
        voiture.chauffeur = self

    def retirerVoiture(self):

        if self.voitureService:
            self.voitureService.chauffeur = None
            self.voitureService = None