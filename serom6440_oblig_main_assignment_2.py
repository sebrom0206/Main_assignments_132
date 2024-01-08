# main assignment 2

# 1. TheSquareMatrix class

class SquareMatrix:

    def __init__(self, order):
        self.order = order
        self.rows = [
            [0 for j in range(order)]
            for i in range(order)
        ]

    def __str__(self):
        return ("\n".join(
            [
                " ".join([str(e) for e in row])
                for row in self.rows
            ]
        ))

    def set_value(self, i, j, value):
        self.rows[i][j] = value

    def get_value(self, i, j):
        return self.rows[i][j]

    def max(self):
        li1 = []
        for row in self.rows:
            for n in row:
                li1.append(n)
        return max(li1)

    def min(self):
        li2 = []
        for row in self.rows:
            for n in row:
                li2.append(n)
        return min(li2)

    def trace(self):

        return sum(self.rows[i][i] for i in range(self.order))

    def summary(self):
        return {'order': self.order, 'max': self.max(), 'min': self.min(), 'trace': self.trace()}

    def save(self, filename):
        var = self.__str__()
        f = open(filename, 'w')
        f.write(var)
        f.close()

    @classmethod
    def parse(cls, text):

        lines = [line for line in text.split('\n')]
        first_line = lines[0]
        first_line = first_line.replace(' ', '')
        # print(lines)
        order = len(first_line)
        matrix = SquareMatrix(order)

        for i, line in enumerate(lines):
            print(line)

            matrix.rows[i] = [int(i) for i in line.split()]

        return matrix

    @classmethod
    def load(cls, filename):

        # f = open(filename)
        return SquareMatrix.parse(open(filename).read())


# Test m1 | m2 | m3

m1 = SquareMatrix(3)
m1.set_value(0, 0, 1)
m1.set_value(1, 1, 1)
m1.set_value(2, 2, 1)
print('--m1--')
print(m1)
print(m1.summary())
print()

m2_text = '''\
1 2 3
4 5 6
7 8 9'''

print('--m2--')
m2 = SquareMatrix.parse(m2_text)

print(m2.summary())
m2.save('m3.txt')
print()

print('--m3--')
m3 = SquareMatrix.load('m3.txt')
# print(m3)
print(m3.summary())
print()

m4 = SquareMatrix(3)
m4.set_value(0, 0, 3)
m4.set_value(0, 1, 6)
m4.set_value(0, 2, 3)
m4.set_value(1, 0, 6)
m4.set_value(1, 1, 3)
m4.set_value(1, 2, 6)
m4.set_value(2, 0, 3)
m4.set_value(2, 1, 6)
m4.set_value(2, 2, 3)
print('--m4--')
print(m4)
print(m4.summary())
m4.save('m4.txt')
print()
