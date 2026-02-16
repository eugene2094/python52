import copy


class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def clone(self):
        return copy.copy(self)


p_car = Car("bmw", "black")
cloned_car = p_car.clone()

print(p_car)
print(cloned_car)