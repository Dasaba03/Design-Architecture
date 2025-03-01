from extractions.espresso import EspressoExtraction
from extractions.french_press import FrenchPressExtraction
from extractions.filter import FilterExtraction

class ExtractionFactory:
    @staticmethod
    def create_extraction(method, coffee):
        if method == "espresso":
            return EspressoExtraction(coffee)
        if method == "french_press":
            return FrenchPressExtraction(coffee)
        if method == "filter":
            return FilterExtraction(coffee)
       