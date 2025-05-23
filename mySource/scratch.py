from dataclasses import dataclass

@dataclass
class Customer:
    name: str
    city: str = "Florence"
    bonus_points: int = 100
    total_spent: float = 0.00

c1 = Customer("Robert")
print(repr(c1))