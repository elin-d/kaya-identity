def compute_kaya_identity(pop, gdp, enInt, carbInt):
    """
    Equation that expresses yearly CO2 emissions.

    Extended description of function.

    Parameters:
    pop(numeric): Population size (in millions)
    gdp(numeric): GDP per capita (in 1000$/person)
    enInt(numeric): Energy Intensity (in Gigajoule/$1000GDP). Energy Intensity is the energy needed to produce a certain
    amount of economic value.
    carbInt(numeric) Carbon Intensity (in tonnes CO2/Gigajoule). Carbon Intensity is the CO2 emitted for produced energy


    Returns:
    float: CO2 emissions in million tonnes of CO2

    """
    co2 = pop * gdp * enInt * carbInt
    return co2


def main():
    result = compute_kaya_identity(82.4, 44, 5, 0.05)
    print("%.2f" % result)


if __name__ == '__main__':
    main()