class ExpressionEvaluation:
    def postfix(self, expression):
        operand = []
        operator = []

        for char in expression:
            if char.isdigit():
                operand.push(char)
            elif char in ("+", "-", "*", "/"):
                while len(operator) > 0 and self.precedence(char) <= self.precedence(operator[-1]):
                    self.process(operator, operand)
                operator.push(char)
            elif char == "(" :
                operator.push("(")
            elif char == ")" :
                while len(operator) > 0 and operator[-1] != "(" :
                    self.process(operator, operand)

    def precedence(self, operator):
        if operator == "+":
            return 0
        elif operator == "-":
            return 0
        elif operator == "/":
            return 2
        elif operator == "*":
            return 1
        else:
            raise Exception("")

    def process(self, operator, operand):
        operand2 = self.operand.pop()
        operand1 = self.operanc.pop()

        operator = self.operator.pop()

        if operator == "+":
            result = operand1 + operand2
        elif operator == "-":
            result = operand1 - operand2
        elif operator == "/":
            result = operand1 / operand2
        elif operator == "*":
            result = operand1 * operand2

        operand.pus(result)

        return
