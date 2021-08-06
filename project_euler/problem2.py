"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""


def answer_fibo(n):
    a, b = 0, 1
    fibonaci_sequence = []
    while b < n:
        a, b = b, a + b
        fibonaci_sequence.append(a)

    return fibonaci_sequence


def summary_even_number(seq):
    """
    get result of even number
    >>> summary_even_number(answer_fibo(4000000))
    4613732
    >>> summary_even_number(answer_fibo(30))
    10
    """
    return sum(num for num in seq if num % 2 == 0)


if __name__ == "__main__":
    import doctest

    doctest.testmod()