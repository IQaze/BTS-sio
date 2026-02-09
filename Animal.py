class Animal:
  def __init__(self, nom,taille):
    self.nom = nom
    self.taille = taille

  def nomAnimal(self):
      return self.nom

  def __str__(self):
    return self.nom

  def __repr__(self):
    return self.__str__()