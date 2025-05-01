from abc import ABC, abstractmethod
from dataclasses import dataclass

# Strategy Interface
class ShippingStrategy(ABC):
    @abstractmethod
    def calculate(self, package) -> float:
        pass

# Concrete Strategies
class StandardShipping(ShippingStrategy):
    def calculate(self, package) -> float:
        base_cost = 5.00
        return base_cost + (package.weight * 0.5) + (0.1 * package.distance)

class ExpressShipping(ShippingStrategy):
    def calculate(self, package) -> float:
        base_cost = 15.00
        return base_cost + (package.weight * 0.8) + (0.2 * package.distance)

class InternationalShipping(ShippingStrategy):
    def calculate(self, package) -> float:
        base_cost = 30.00
        return base_cost + (package.weight * 1.5) + (0.5 * package.distance) + (10 if package.size == 'large' else 0)

@dataclass
class Package:
    weight: float  # in kg
    distance: float  # in km
    size: str  # 'small', 'medium', 'large'
    destination: str  # 'domestic' or 'international'

# Context Class
class ShippingCostCalculator:
    def __init__(self, strategy: ShippingStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: ShippingStrategy):
        self._strategy = strategy

    def calculate_cost(self, package) -> float:
        return self._strategy.calculate(package)

# Usage
if __name__ == "__main__":
    package = Package(weight=2.5, distance=300, size='medium', destination='domestic')
    
    # Standard shipping
    calculator = ShippingCostCalculator(StandardShipping())
    print(f"Standard shipping cost: ${calculator.calculate_cost(package):.2f}")
    
    # Express shipping
    calculator.set_strategy(ExpressShipping())
    print(f"Express shipping cost: ${calculator.calculate_cost(package):.2f}")
    
    # International shipping (even though package is domestic in this case)
    calculator.set_strategy(InternationalShipping())
    print(f"International shipping cost: ${calculator.calculate_cost(package):.2f}")
