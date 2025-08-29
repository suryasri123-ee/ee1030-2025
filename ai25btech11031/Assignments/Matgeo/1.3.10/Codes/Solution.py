def find_y_and_ratio():
    A = (1,2)
    B = (2,3)
    Px = 8

    # solve for ratio using x-coordinate
    k = (Px - A[0]) / (B[0] - Px)

    # solve for y-coordinate
    y = (k*B[1] + A[1]) / (k+1)

    print("Ratio = {:.2f} : 1".format(k))
    print("y =", y)

find_y_and_ratio()