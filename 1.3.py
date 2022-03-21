class Worker():

   def __init__(self, name_1, surname_1, position_1, wage, bonus):
       self.name = name_1
       self.surname = surname_1
       self.position = position_1
       self._income = {"wage": wage , "bonus": bonus}



class Position(Worker):
    def get_full_name(self):
        return self.name, self.surname
    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')

Worker_1 = Position('Alex' , 'Lesstor', 'director', 200, 5)
print(Worker_1.name, ' ', Worker_1.surname, ' ', Worker_1.position, ' ', Worker_1.position, ' ', Worker_1._income.get('wage'), Worker_1._income.get('bonus'))
print(Worker_1.get_full_name(), ' ', Worker_1.get_total_income())

