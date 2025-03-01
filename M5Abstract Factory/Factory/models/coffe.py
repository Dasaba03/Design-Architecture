class coffe:
    def __init__(self,origin,weight,roast,base_cost):
        self._origin = origin
        self._weight = weight
        self._roast = roast
        self._base_cost = base_cost

    def calculate_total_cost(self, extraction_method):
        tax = extraction_method.calculate_cost()
        return self._base_cost + tax