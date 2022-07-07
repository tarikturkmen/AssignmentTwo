def auto(merk, health, damage):
    print("ik rij in een " + merk)

    if damage > health:
        print("Door de " + merk + ': boooooom!')


auto('audi', 100, 50)
auto('bmw', 50, 100)
