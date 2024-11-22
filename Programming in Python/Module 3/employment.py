class Employees:
    def __init__(self,name,last) -> None:
        self.name = name 
        self.last = last
        
class Supervisors(Employees):
    def __init__(self, name, last, password) -> None:
        super().__init__(name, last)
        self.password = password
        
class Chefs(Supervisors):
    def leave_request(self, days):
        return "i'll take leave for "+ str(days) +  " days"
    
geralda = Employees("Geralda","G" )
gertrude = Supervisors("Gertrude","G","123")
filo = Chefs("Filo","F","here")

print(filo.leave_request(45))