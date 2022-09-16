import math


# Function that solves for the quadratic discriminate
def discriminate_solver(var_a, var_b, var_c):
    solutions = (var_b ** 2) - 4 * var_a * var_c
    return solutions


# Function that simplifies a radical if the equation has 2 imaginary solutions
def radical_simplifier():
    # Radicals cannot be negative so I must unnegative it.
    rad_discriminant = discriminant * -1
    duplicate_radical = rad_discriminant
    sqr_number = 1

    for i in range(2, rad_discriminant):
        exp = 1
        while i ** exp <= duplicate_radical:
            if duplicate_radical % i ** exp == 0:
                exp = exp + 1
            else:
                break
        if exp > 2:
            sqr_factor = i ** (int((exp - 1) / 2))
            sqr_number = sqr_number * sqr_factor
            duplicate_radical = duplicate_radical / (sqr_factor ** 2)

    coefficient = int(sqr_number)
    radicand = int(rad_discriminant / (sqr_number ** 2))
    # This finds what type of radical the finished product is and returns it (perfect square, simplified, unsimplified)
    if radicand == 1:
        return "perfect square", coefficient, radicand
    else:
        if coefficient == 1:
            return "unsimplified", coefficient, radicand
        else:
            return "simplified", coefficient, radicand


# Uses the quadratic formula to solve the quadratic equation
def quadratic_solver(var_a, var_b, var_c, quad_discriminant):
    quad_discriminant = int(quad_discriminant)
    # Solves equation if there is only one solution
    if quad_discriminant == 0:
        solutions = (-1 * var_b) / 2 * var_a
        return str(solutions)
    # Solves equation if there are two real solutions
    elif quad_discriminant > 0:
        solution1 = ((-1 * var_b) + math.sqrt(quad_discriminant)) / (2 * var_a)
        solution2 = ((-1 * var_b) - math.sqrt(quad_discriminant)) / (2 * var_a)
        return str(solution1) + " and " + str(solution2)
    # Solves equation if there are two imaginary solutions
    else:
        # Grabs three different variable from the radical_simplifier function
        statement, coefficient, radicand = radical_simplifier()
        # Solves the numerator and denominator of the quadratic equation separately
        quadratic_numerator = -1 * var_b
        quadratic_denominator = 2 * var_a
        # Returns the right string depending on what type of answer was returned from the radical_simplifier function
        if statement == "perfect square":
            string = "(" + str(quadratic_numerator) + " + " + str(coefficient) + "i) / " + str(
                quadratic_denominator) + " and " + "(" + str(quadratic_numerator) + " - " + str(
                coefficient) + "i) / " + str(quadratic_denominator)
            return string
        elif statement == "unsimplified":
            string = "(" + str(quadratic_numerator) + " + i√" + str(radicand) + ") / " + str(
                quadratic_denominator) + " and " + "(" + str(quadratic_numerator) + " - i√" + str(
                radicand) + ") / " + str(quadratic_denominator)
            return string
        else:
            string = "(" + str(quadratic_numerator) + " + " + str(coefficient) + "i√" + str(radicand) + ") / " + str(
                quadratic_denominator) + " and " + "(" + str(quadratic_numerator) + " - " + str(
                coefficient) + "i√" + str(radicand) + ") / " + str(quadratic_denominator)
            return string


# Error proofs the input for variables a, b, and c

while True:
    try:
        a = int(input("Input a: "))
        break
    except ValueError:
        print("That input is invalid! Try something else")

while True:
    try:
        b = int(input("Input b: "))
        break
    except ValueError:
        print("That input is invalid! Try something else")

while True:
    try:
        c = int(input("Input c: "))
        break
    except ValueError:
        print("That input is invalid! Try something else")

# finds the discriminant
discriminant = discriminate_solver(a, b, c)

# Converts the number discriminant into logical solution types
if discriminant > 0:
    solution_type = "2 real solutions"
elif discriminant == 0:
    solution_type = "one real solution"
else:
    solution_type = "2 imaginary solutions"

# Prints the answer
print("Your function was:")
if b < 0:
    if c < 0:
        print(str(a) + "x\u00b2" + str(b) + "x" + str(c))
    else:
        print(str(a) + "x\u00b2" + str(b) + "x+" + str(c))
else:
    if c < 0:
        print(str(a) + "x\u00b2+" + str(b) + "x" + str(c))
    else:
        print(str(a) + "x\u00b2+" + str(b) + "x+" + str(c))
print("This function has " + solution_type + ". The solutions are:")
print(quadratic_solver(a, b, c, discriminant))
