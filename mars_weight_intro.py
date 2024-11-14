def planet_weight():   
    MERCURY_GRAVITY = 0.38
    VENUS_GRAVITY = 0.91
    MARS_GRAVITY = 0.378
    JUPITER_GRAVITY = 2.34
    SATURN_GRAVITY = 1.06
    URANUS_GRAVITY = 0.92
    NEPTUNE_GRAVITY = 1.19
    print("Hey buddy!!")
    earth_weight = float(input("Please enter your weight on Earth (in kg): "))
    planet = input("Which planet would you like to know your weight on? : ").strip().lower()
    if planet == "mercury":
        gravity_constant = MERCURY_GRAVITY
    elif planet == "venus":
        gravity_constant = VENUS_GRAVITY
    elif planet == "mars":
        gravity_constant = MARS_GRAVITY
    elif planet == "jupiter":
        gravity_constant = JUPITER_GRAVITY
    elif planet == "saturn":
        gravity_constant = SATURN_GRAVITY
    elif planet == "uranus":
        gravity_constant = URANUS_GRAVITY
    else:
        gravity_constant = NEPTUNE_GRAVITY
    planetary_weight = earth_weight * gravity_constant
    rounded_planetary_weight = round(planetary_weight, 3)
    print(f"Your weight on {planet.capitalize()} would be approximately {rounded_planetary_weight} kg.")

planet_weight()



