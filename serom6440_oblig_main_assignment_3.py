import math


class Expression:
    def eval(self):
        pass

    # collect all the numbers into a set
    def collect_numbers(self):
        pass


class Constant(Expression):
    def __init__(self, value):
        self.value = value

    def eval(self):
        return self.value

    def __str__(self):
        return str(self.value)

    def collect_numbers(self):
        # singleton set
        return {self.value}


class BinaryExpression(Expression):
    def __init__(self, operand1, operand2):
        self.operand1 = operand1
        self.operand2 = operand2

    def collect_numbers(self):
        set_ = self.operand1.collect_numbers() | self.operand2.collect_numbers()
        return set_


class PlusExpression(BinaryExpression):
    def __init__(self, operand1, operand2):
        super().__init__(operand1, operand2)

    def eval(self):
        return self.operand1.eval() + self.operand2.eval()

    def __str__(self):
        return f"({self.operand1}) + ({self.operand2})"


class MinusExpression(BinaryExpression):
    def __init__(self, operand1, operand2):
        super().__init__(operand1, operand2)

    def eval(self):
        return self.operand1.eval() - self.operand2.eval()

    def __str__(self):
        return f"({self.operand1}) - ({self.operand2})"


class MultiplyExpression(BinaryExpression):
    def __init__(self, operand1, operand2):
        super().__init__(operand1, operand2)

    def eval(self):
        return self.operand1.eval() * self.operand2.eval()

    def __str__(self):
        return f"({self.operand1}) * ({self.operand2})"


class DivideExpression(BinaryExpression):
    def __init__(self, operand1, operand2):
        super().__init__(operand1, operand2)

    def eval(self):
        return self.operand1.eval() / self.operand2.eval()

    def __str__(self):
        return f"({self.operand1}) / ({self.operand2})"


class NaryExpression(Expression):
    # operands is a list of expressions
    def __init__(self, *operands):
        self.operands = operands

    def collect_numbers(self):
        # singleton set
        empty_set = set()

        for n in self.operands:
            empty_set.update(n.collect_numbers())
        return empty_set


class MaxExpression(NaryExpression):

    def eval(self):

        empty_list = []
        for n in self.operands:
            empty_list.append(n.eval())

        return max(empty_list)

    def __str__(self):
        # string metode
        empty_string = ""
        
        for n in self.operands:
            empty_string += n.__str__()
            empty_string += ', '
        var = empty_string
       
        return f'max({empty_string})'
    
        """
        
        str_output = ", ".join([operand.__str__() for operand in self.operands])
    
        #return f"max({str_output})"
        """
  
            


class MinExpression(NaryExpression):

    def eval(self):

        empty_list = []
        for n in self.operands:
            empty_list.append(n.eval())
        return min(empty_list)

    def __str__(self):

        """
        empty_string = ""
        test_list = []

        for n in self.operands:
            #empty_string += n.__str__()
            test_list.append(n.__str__())
            #print(test_list)
        #return f'min({empty_string})'
        
        """

        #Sindre metode
        str_output = ", ".join([operand.__str__() for operand in self.operands])

        return f"min({str_output})"
        #return ', '.join(test_list)
        

if __name__ == '__main__':
    One = Constant(1)
    Two = Constant(2)
    Three = Constant(3)
    OneThousand = Constant(1000)
    Pi = Constant(round(math.pi, 2))

    expr1 = MultiplyExpression(MultiplyExpression(Three, Three), Pi)  # 3 * 3 * pi
    expr2 = DivideExpression(OneThousand, Three)  # 1000 * 3
    expr3 = MinusExpression(OneThousand, Two)  # 1000 - 2
    expr_min = MinExpression(expr1, expr2, expr3)
    expr_max = MaxExpression(expr1, expr2, expr3)

    for expr in [expr1, expr2, expr3, expr_min, expr_max]:
        print(f"{expr} = {expr.eval()}, with numbers {expr.collect_numbers()}")
        print()
