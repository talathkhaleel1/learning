from application_development.trial_test.zoo import Zoo


class Animals(Zoo):
    def __init__(self, name, territory_requirement =20):
        super().__init__(name)
        self.territory_requirement = territory_requirement

    def to_place(self):
        if self.territory_requirement > 20:
            len(self.name) += 1


    def to_sell(self):
        if self.territory_requirement < 20:
            len(self.name) -= 1