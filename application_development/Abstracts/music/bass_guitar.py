from abstracts.music.stringed_instruments import StringedInstrument



class BassGuitar(StringedInstrument):

    def __init__(self, numberOfStrings = 4):
        super().__init__(numberOfStrings)

    def sound(self):# this shound give the sound "Duum-duum-duum"
        super().sound()