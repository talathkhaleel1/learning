from application_development.OOP.Pokemon.pokemon import Pokemon


def initializePokemons():
    pokemon = []

    pokemon.append(Pokemon("Balbasaur", "leaf", "water"))
    pokemon.append(Pokemon("Pikatchu", "electric", "water"))
    pokemon.append(Pokemon("Charizard", "fire", "leaf"))
    pokemon.append(Pokemon("Balbasaur", "water", "fire"))
    pokemon.append(Pokemon("Kingler", "water", "fire"))

    return pokemon


pokemon = initializePokemons()

# Every pokemon has a name and a type.
# Certain types are effective against others, e.g. water is effective against fire.

# Ash has a few pokemon.
# A wild pokemon appeared!

wildPokemon = Pokemon("Oddish", "leaf", "water")

# Which pokemon should Ash use?

effective_pokemon = None
for p in pokemon:
    if p.isEffectiveAgainst(wildPokemon):
        effective_pokemon = p
        break

print("I choose you, ", effective_pokemon.name);
