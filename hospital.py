import random
class patient:
    def parametrs(self, n, a, d):
      self.name = n
      self.age = a
      self.diseas = d
class docter:
    def parametrs(self, name, profil, schedule = []):
      self.name = name
      self.profil = profil
      self.schedule = schedule
    
class illness:
    def  parametrs(self, symptom, whos, who):
      self. symptom  =  symptom
      self.whos = whos 
      self.who = who 
doctors = [] # список с объектами типа доктор
patient1 = patient()
patient1.parametrs("bob", 26, 'hadeace')
print(patient1.name)
docotr1 = docter()
docotr1.parametrs("bill", 'head', [10, 12 ,13])
doctors.append(docotr1)
print(docotr1.profil)
def find_doctor(x):  #x - пациент
  promlem = x.d
  global doctors
  therapist = []
  for i in doctors:
    if promlem == i.profil:
      therapist.append(i)
  return random.therapist()
