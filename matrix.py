'''
Matt Bonnell
420 LCU Computer Programming (Python) Section 01
April 10, 2017
R. Vincent, instructor
Epreuve synthese
'''


class Matrix(list):
    """A class for representing matrices."""

    def __init__(self, *rows):
        self.__precision = 0
        for row in rows:
            self.append(row)
            if len(self[0]) != len(row):
                raise ValueError("All rows must have the same number of entries.")
        self.__rows = self.get_rows()  # Stores the number of rows
        self.__columns = self.get_columns()  # Stores the number of columns

    def add_rows(self, *rows):
        """Appends a variable number of rows to the matrix."""
        if self.__rows:
            for row in rows:
                if len(row) == self.__columns:
                    self.append(row)
                else:
                    raise ValueError("One or more of the new rows doesn't have the right number " +
                                     "of columns for this matrix.")
        else:
            for row in rows:
                if len(row) == len(rows[0]):
                    self.append(row)
                else:
                    raise ValueError("All rows must have the same number of entries.")
            self.__columns = self.get_columns()
        self.__rows = self.get_rows()

    def add_columns(self, *columns):
        """Appends a variable number of columns to the matrix."""
        if self.__columns:
            for column in columns:
                if len(column) == self.__rows:
                    for i in range(self.__rows):
                        self[i].append(column[i])
                else:
                    raise ValueError("One or more of the new columns doesn't have the right number " +
                                     "of rows for this matrix.")
        else:
            for column in columns:
                if len(column) == len(columns[0]):
                    for value in column:
                        self.add_rows([value])
                else:
                    raise ValueError("All columns must have the same number of entries.")
            self.__rows = self.get_rows()
        self.__columns = self.get_columns()

    def get_rows(self):
        """Returns the number of rows."""
        return len(self)

    def get_columns(self):
        """Returns the number of columns."""
        return len(self[0]) if len(self) else 0

    def is_square(self):
        """Returns true if the matrix has the same number of rows and columns."""
        return self.__rows == self.__columns

    def is_invertible(self):
        """Returns true if the matrix is invertible."""
        if self.is_square():
            return bool(self.determinant())
        else:
            return False

    def is_symmetric(self):
        """Returns true if the matrix is symmetric."""
        if self.is_square():
            return self == self.transpose()
        else:
            return False

    def is_skew_symmetric(self):
        """Returns true if the matrix is skew-symmetric."""
        if self.is_square():
            return self == self.transpose() * -1
        else:
            return False

    def is_upper_triangular(self):
        """Returns true if the matrix is upper triangular."""
        if self.is_square():
            for i in range(self.__rows):
                for j in range(self.__columns):
                    if i == j:
                        break
                    else:
                        if self[i][j]:
                            return False
            return True
        else:
            return False

    def is_lower_triangular(self):
        """Returns true if the matrix is lower triangular."""
        if self.is_square():
            for i in range(self.__rows):
                for j in range(self.__columns):
                    if j <= i:
                        continue
                    else:
                        if self[i][j]:
                            return False
            return True
        else:
            return False

    def is_triangular(self):
        """Returns true if the matrix is upper or lower triangular."""
        if self.is_square():
            return self.is_upper_triangular() or self.is_lower_triangular()
        else:
            return False

    def determinant(self):
        """Returns the determinant of the matrix."""
        if self.is_square():
            if self.__rows == 2 and self.__columns == 2:
                return (self[0][0] * self[1][1]) - (self[0][1] * self[1][0])
            else:
                answer = 0
                # Following block expands the 0th row of the matrix.
                for j in range(self.__columns):
                    sub_matrix = Matrix()
                    for k in range(self.__rows):
                        new_row = []
                        for l in range(self.__columns):
                            if k != 0 and l != j:
                                new_row.append(self[k][l])
                        if new_row:
                            sub_matrix.add_rows(new_row)
                    answer += ((-1) ** j) * self[0][j] * sub_matrix.determinant()
                return answer
        else:
            raise ValueError("Determinants only exist for square matrices.")

    def transpose(self):
        """Returns the transpose of the matrix."""
        answer = Matrix()
        for row in self:
            answer.add_columns(row)
        return answer

    def is_the_same_size_as(self, other):
        """Returns true if the matrices are of the same dimensions."""
        return self.__rows == other.__rows and self.__columns == other.__columns

    def can_be_multiplied_by(self, other):
        """Returns true if the matrix can be multiplied by the other matrix."""
        return self.__columns == other.__rows

    #  Implicits
    def __repr__(self):
        """Specifies how the matrix should be represented."""
        to_print = ""
        for row in self:
            for entry in row:
                to_print += f"{entry:^ {10}.{1}f}"
            to_print += "\n"
        return to_print

    def __add__(self, other):
        """Specifies how the addition operation should be performed on
        matrix objects."""
        if isinstance(other, Matrix):  # Checks if other is a matrix object.
            if self.is_the_same_size_as(other):  # Checks if the matrices are compatible for addition.
                answer = Matrix()
                for i in range(self.__rows):
                    new_row = []
                    for j in range(self.__columns):
                        new_entry = self[i][j] + other[i][j]  # Adds the matrix entries together.
                        new_row.append(new_entry)
                    answer.add_rows(new_row)
                return answer
            else:
                raise ValueError("Matrices must have the same dimensions for addition.")
        else:
            raise TypeError("Objects of type \"" + type(other).__name__ + "\" cannot be added to matrices.")

    def __sub__(self, other):
        """Specifies how the subtraction operation should be performed on
        matrix objects."""
        if isinstance(other, Matrix):  # Checks if other is a matrix object.
            if self.is_the_same_size_as(other):  # Checks if the matrices are compatible for subtraction.
                answer = Matrix()
                for i in range(self.__rows):
                    new_row = []
                    for j in range(self.__columns):
                        new_entry = self[i][j] - other[i][j]
                        new_row.append(new_entry)
                    answer.add_rows(new_row)
                return answer
            else:
                raise ValueError("Matrices must have the same dimensions for subtraction.")
        else:
            raise TypeError("Objects of type \"" + type(other).__name__ + "\" cannot be added to matrices.")

    def __mul__(self, other):
        """Specifies how the multiplication operation should be performed on
        matrix objects."""
        if isinstance(other, Matrix):  # Checks if other is a matrix object.
            if self.can_be_multiplied_by(other):  # Checks if the matrices are compatible for multiplication.
                answer = Matrix()
                for i in range(self.__rows):
                    new_row = []
                    for j in range(other.__columns):
                        new_entry = 0
                        for k in range(self.__columns):
                            new_entry += self[i][k] * other[k][j]
                        new_row.append(new_entry)
                    answer.add_rows(new_row)
                return answer
            else:
                raise ValueError("Matrices are not compatible for multiplication.")
        else:
            answer = Matrix()
            for i in range(self.__rows):
                new_row = []
                for j in range(self.__columns):
                    new_row.append(self[i][j] * other)
                answer.add_rows(new_row)
            return answer


