from abstracts.music.stringed_instruments import StringedInstrument



class ElectricGuitar(StringedInstrument):

    def __init__(self, numberOfStrings = 6):
        super().__init__(numberOfStrings)

    def sound(self, tune):# this shound give the sound "Twang"
        super().sound()
        self.tune = tune
        return tune
