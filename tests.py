'''
Matt Bonnell
420 LCU Computer Programming (Python) Section 01
May 19, 2017
R. Vincent, instructor
Epreuve synthese
'''

from matrix import Matrix
from random import randint


def test_properties(name, matrix):
    print("-----------------------------------------------------------------------")
    print("Properties test: {}\n".format(name))
    print("{} =\n{}".format(name, matrix))
    print("Number of rows:", matrix.get_rows())
    print("Number of columns:", matrix.get_columns())
    print("Square:", matrix.is_square())
    print("Invertible:", matrix.is_invertible())
    print("Symmetric:", matrix.is_symmetric())
    print("Skew-symmetric:", matrix.is_skew_symmetric())
    print("Triangular:", matrix.is_triangular())
    print("Upper triangular:", matrix.is_upper_triangular())
    print("Lower triangular:", matrix.is_lower_triangular())

    try:
        print("Determinant = {}".format(matrix.determinant()))
    except ValueError as e:
        print("Determinant = N/A", "({})".format(e))

    print("Transpose = ", "\n" + str(matrix.transpose()))


def test_operations(name1, matrix1, name2, matrix2):

    m1 = matrix1
    m2 = matrix2

    print("-----------------------------------------------------------------------")
    print("Comparison and operations test: {}, {}\n".format(name1, name2))
    print("{} =\n{}".format(name1, m1))
    print("{} =\n{}".format(name2, m2))

    print("{} is the same size as {}: {}".format(name1, name2, m1.is_the_same_size_as(m2)))

    print("\n--Addition--\n")
    try:
        print("{} + {} =\n{}".format(name1, name2, str(m1 + m2)))
    except ValueError as e:
        print("{} + {} = N/A ({})".format(name1, name2, e))

    print("\n--Subtraction--\n")
    try:
        print("{} - {} =\n{}".format(name1, name2, str(m1 - m2)))
    except ValueError as e:
        print("{} - {} = N/A ({})".format(name1, name2, e))

    print("\n--Scalar multiplication--\n")

    scalar = randint(-9, 9)
    print("{} * {} =\n{}".format(name1, scalar, str(m1 * scalar)))

    scalar = randint(-9, 9)
    print("{} * {} =\n{}".format(name2, scalar, str(m2 * scalar)))

    print("\n--Matrix multiplication--\n")
    print("{} can be multiplied by {}: {}".format(name1, name2, m1.can_be_multiplied_by(m2)))

    try:
        print("{} * {} =\n{}".format(name1, name2, m1 * m2))
    except ValueError as e:
        print("{} * {} = N/A ({})".format(name1, name2, e))

    print("{} can be multiplied by {}: {}".format(name2, name1, m2.can_be_multiplied_by(m1)))

    try:
        print("{} * {} =\n{}".format(name2, name1, m2 * m1))
    except ValueError as e:
        print("{} * {} = N/A ({})".format(name2, name1, e))

A = Matrix([2, 0, 0], [3, 4, 0], [1, 5, 2])
B = Matrix([2, 4, 3, 4], [0, 2, 1, 3], [0, 0, 4, 5], [0, 0, 0, 3])
C = Matrix([4, 8], [3, 2], [6, 2])
D = Matrix([1, 2, 3], [2, 5, 1], [3, 1, 4])
E = Matrix([0, -1, 5], [1, 0, -3], [-5, 3, 0])


test_properties("A", A)
test_properties("B", B)
test_properties("C", C)
test_properties("D", D)
test_properties("E", E)
test_operations("A", A, "B", B)
test_operations("A", A, "C", C)
test_operations("A", A, "D", D)
test_operations("A", A, "E", E)
test_operations("B", B, "C", C)
test_operations("B", B, "D", D)
test_operations("B", B, "E", E)
test_operations("C", C, "D", D)
test_operations("C", C, "E", E)
test_operations("D", D, "E", E)
print("\nTesting complete")
