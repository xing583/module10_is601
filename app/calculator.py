from enum import Enum

class CalculationType(str, Enum):
    ADD = "Add"
    SUBTRACT = "Subtract"
    MULTIPLY = "Multiply"
    DIVIDE = "Divide"

class AddOperation:
    def calculate(self, a: float, b: float) -> float:
        return a + b

class SubtractOperation:
    def calculate(self, a: float, b: float) -> float:
        return a - b

class MultiplyOperation:
    def calculate(self, a: float, b: float) -> float:
        return a * b

class DivideOperation:
    def calculate(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

class CalculationFactory:
    @staticmethod
    def create(operation_type: CalculationType):
        operations = {
            CalculationType.ADD: AddOperation(),
            CalculationType.SUBTRACT: SubtractOperation(),
            CalculationType.MULTIPLY: MultiplyOperation(),
            CalculationType.DIVIDE: DivideOperation(),
        }
        if operation_type not in operations:
            raise ValueError(f"Unknown operation: {operation_type}")
        return operations[operation_type]
