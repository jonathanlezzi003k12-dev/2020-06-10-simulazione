from dataclasses import dataclass
@dataclass
class Attori:
    id:int
    first_name:str
    last_name:str
    gender:chr


    def __hash__(self):
        return self.id

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"

    def __eq__(self, other):
        return self.id==other.id
