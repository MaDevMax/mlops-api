import pickle
from model import Model

# Создаём модель
model = Model()

# Сохраняем в файл
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Модель сохранена в model.pkl")
print(f"Коэффициент: {model.coef}")
print(f"Пересечение: {model.intercept}")