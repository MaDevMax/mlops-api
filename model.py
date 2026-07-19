class Model:
    def __init__(self):
        self.coef = 2.5
        self.intercept = 1.3

    def predict(self, x: float) -> float:
        return x * self.coef + self.intercept