# Shipping Cost Calculator using Strategy Design Pattern

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Design Pattern](https://img.shields.io/badge/design%20pattern-strategy-brightgreen)

A Python implementation of the Strategy design pattern for calculating shipping costs based on different factors like location, delivery speed, and package size.

## 📦 Overview

This project demonstrates how to use the Strategy design pattern to implement different shipping cost calculation algorithms. The pattern allows you to define a family of algorithms (shipping methods), encapsulate each one, and make them interchangeable at runtime.

## 🚀 Usage
```python
from shipping import Package, ShippingCostCalculator, StandardShipping, ExpressShipping, InternationalShipping

# Create a package
package = Package(weight=2.5, distance=300, size='medium', destination='domestic')

# Calculate costs with different strategies
calculator = ShippingCostCalculator(StandardShipping())
print(f"Standard shipping: ${calculator.calculate_cost(package):.2f}")

calculator.set_strategy(ExpressShipping())
print(f"Express shipping: ${calculator.calculate_cost(package):.2f}")

calculator.set_strategy(InternationalShipping())
print(f"International shipping: ${calculator.calculate_cost(package):.2f}")
```

## 🧩 Key Components
1. ShippingStrategy (Interface)
- Defines the contract for all shipping algorithms
- Requires implementation of calculate() method
2. Concrete Strategies
- StandardShipping: Basic shipping with lowest cost
- ExpressShipping: Faster delivery at higher cost
- InternationalShipping: For overseas shipments with customs considerations
3. Package (Data Class)
- Contains package details: weight, distance, size, destination
4. ShippingCostCalculator (Context)
- Maintains reference to current strategy
- Delegates calculation to the strategy object
- Allows runtime strategy changes

## ✨ Design Pattern Benefits
- Flexibility: Easily add new shipping methods without modifying existing code
- Maintainability: Each algorithm is encapsulated in its own class
- Testability: Strategies can be tested in isolation
- Runtime Switching: Change shipping method dynamically
