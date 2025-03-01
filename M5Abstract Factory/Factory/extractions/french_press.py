from .base_extraction import BaseExtraction

class FrenchPressExtraction(BaseExtraction):
    def extract(self):
        print (f"Preparando cafe en prensa francesa de cafe de {self.coffee._origin}")
        print (f"Weight: {self.coffee._weight} kg. Roast: {self.coffee._roast}")
        print(f"Tax: {self.calculate_cost()}")
    
    def calculate_cost(self):
        return self.coffee._base_cost * 0.15  
