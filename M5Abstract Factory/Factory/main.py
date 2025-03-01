from models.coffe import coffe
from factory.extraction_factory import ExtractionFactory

coffees = [
    coffe("Colombia", 250, "Medium", 50),
    coffe("Ethiopia", 300, "Dark", 65),
    coffe("Brazil", 200, "Light", 40)
]

methods = ["espresso", "french_press", "filter"]

for i in range(len(coffees)):
    extraction_method = ExtractionFactory.create_extraction(methods[i], coffees[i])
    extraction_method.extract()
    print(f"Total cost for {coffees[i]._origin} coffee: {coffees[i].calculate_total_cost(extraction_method)}")
    print("-" * 50)
