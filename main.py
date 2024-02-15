class Cooking:
    def __init__(self):
        self.type = None
        self.sauce = None
        self.topping = None
        self.dressing = None

    def add_pasta(self, pasta_type):
        self.type = pasta_type

    def add_sauce(self, sauce):
        self.sauce = sauce

    def add_topping(self, topping):
        self.topping = topping

    def add_dressing(self, dressing):
        self.dressing = dressing


class Cooker:
    def __init__(self):
        self.cooking = Cooking()

    def add_pasta(self, pasta_type):
        self.cooking.add_pasta(pasta_type)
        return self

    def add_topping(self, topping):
        self.cooking.add_topping(topping)
        return self

    def add_sauce(self, sauce):
        self.cooking.add_sauce(sauce)
        return self

    def add_dressing(self, dressing):
        self.cooking.add_dressing(dressing)
        return self

    def build(self):
        return self.cooking


cooker_1 = Cooker()
process_1 = (
    cooker_1.add_pasta("Mafaldine")
    .add_sauce("Arabesse")
    .add_topping("Olives")
    .add_dressing("Chilli flakes")
    .build()
)
print("First meal:", process_1.type, process_1.sauce, process_1.topping, process_1.dressing)

cooker_2 = Cooker()
process_2 = (
    cooker_2.add_pasta("Orecchini")
    .add_sauce("Ricotta")
    .add_topping("Shroom")
    .add_dressing("Parsley")
    .build()
)
print("Second meal:", process_2.type, process_2.sauce, process_2.topping, process_2.dressing)

cooker_3 = Cooker()
process_3 = (
    cooker_3.add_pasta("Paccheri")
    .add_sauce("Pesto")
    .add_topping("Garlic")
    .add_dressing("Olive oil")
    .build()
)
print("Third meal:", process_3.type, process_3.sauce, process_3.topping, process_3.dressing)
