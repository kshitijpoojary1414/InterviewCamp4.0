class RecursionAndMemoization :
    def fibonacci(self, n):
        if n == 1 or n == 2 :
            return 1

        return self.fibonacci(n - 1) + self.fibonacci(n - 2)

    def fibonacciWithMemoization(self, n):
        return self.helper(n, {})

    def helper(self, n, memo):
        if n == 1 or n == 2 :
            return 1

        if n in memo :
            return memo[n]

        result = self.fibonacci(n - 1) + self.fibonacci(n - 2)

        memo[n] = result

        return result

    def powPositive(self, n, pow):
        if pow == 1 :
            return n

        if n == 1 or pow == 0:
            return 1

        halfPower = self.powPositive(n, pow//2)

        if n % 2 == 0 :
            return halfPower * halfPower
        else :
            return halfPower * halfPower * n

    def pow(self, n, pow):
        positiveResult = self.powPositive(abs(n), abs(pow))
        if n < 0 and pow %2 != 0 :
            positiveResult =  -1* positiveResult

        if pow < 0 :
            positiveResult =  1/ positiveResult

        return positiveResult


