# Necessary Imports
from numpy import matmul, array
from numpy.linalg import eig

# Parameters

p1 = 400  # Initial population in Downtown

p2 = 400  # Initial population in Capital Hill

p3 = 400  # Initial population in Ballard

p4 = 400  # Initial population in U District

p5 = 400  # Initial population in Fremont

t1 = 1  # In months

t2 = 12

# Variables

x1 = array([[p1, p2, p3, p4, p5]]).T  # Column vector built from initial conditions

A = array(([0.8, 0.1, 0, 0, 0], [0.1, 0.6, 0, 0.1, 0], [0.1, 0.2, 0.5, 0.1, 0], [0, 0.1, 0.2, 0.8, 0],
           [0, 0, 0.3, 0, 1]))  # Matrix for moving


# Main function

def main():
    # Run ratestep function and print to find people at each location after 1 month
    y1 = ratestep(x1, A, t1)

    # Check to make sure we have the right total number of people at the end after 1 month

    print("Calculated total after 1 month: ", sum(ratestep(x1, A, t1)))

    print("Check ", 400 * 5 + 400 - 200 - (0.5 + 0.2) * 400)

    # Look at change in people by directly comparing initial condition with step

    dy1 = x1 - y1

    print("Total change in population after 1 month: \n", dy1)

    # Run ratestep function and print to find people at each location after 12 months

    y2 = ratestep(x1, A, t2)

    print("Number of people at each location after 12 months: \n ", y2)


# Rate function
def ratestep(x, M, t):
    # Run equation number of times equal to the number of months
    for k in range(t):
        # Declare b here(since it depends on x as x changes). Kind of clunky, but I don't want to take the time to
        # optimize it

        b = array([[400, -100, -100, -0.2 * float(x[3]), -0.5 * float(x[4])]]).T  # Vector b

        # Calculate new x based on old x multiplied by our matrix + b
        x = matmul(M, x) + b
    return x


main()
