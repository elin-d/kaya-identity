def compute_kaya_identity(pop, gdp, enInt, carbInt, output_type="CO2"):
    """
    Equation that expresses yearly CO2 emissions.

    Extended description of function.

    Parameters:
    pop(numeric): Population size (in millions)
    gdp(numeric): GDP per capita (in 1000$/person)
    enInt(numeric): Energy Intensity (in Gigajoule/$1000GDP). Energy Intensity is the energy needed to produce a certain
    amount of economic value.
    carbInt(numeric) Carbon Intensity (in tonnes CO2/Gigajoule). Carbon Intensity is the CO2 emitted for produced energy
    output_type (String): "CO2" or "C", by default "CO2". If it was set to "C", the results will be given in
    tonnes C instead of tonnes CO2.

    Returns:
    float: CO2 or C emissions in million tonnes respectively
    :param output_type:

    """
    if pop < 0:
        raise ValueError("The population size should be positive.")
    if gdp < 0:
        raise ValueError("The GDP per capita should be positive.")

    co2 = pop * gdp * enInt * carbInt
    if output_type == "C":
        return co2 / 3.67
    elif output_type == "CO2":
        return co2
    else:
        ValueError("Output type should be CO2 or C")


def main():
    result = compute_kaya_identity(1, 1, 1, 1)
    print("%.2f" % result)


if __name__ == '__main__':
    main()
