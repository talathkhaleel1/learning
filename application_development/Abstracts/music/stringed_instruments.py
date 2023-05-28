from abstracts.music.instrument import Instrument


class StringedInstrument(Instrument):

    def __init__(self, name, numberOfStrings):
        super().__init__(name)
        self.numberOfStrings = numberOfStrings

    def sound(self, tune):# use play function
        super().play()
        self.tune = tune
        return tune

    def __str__(self):
        print(self.name + ", a " + self.numberOfStrings + " stringed instrument that goes"\
              + self.sound()