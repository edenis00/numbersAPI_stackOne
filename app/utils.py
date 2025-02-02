from httpx import AsyncClient
client = AsyncClient()


def is_prime(number: int):
    if number < 2:
        return False
    sqrt_number = int(number ** 0.5)
    for i in range(2, sqrt_number + 1):
        if number % i == 0:
            return False
    return True


def is_perfect(number: int):
    if number < 2:
        return False
    sqrt_number = int(number ** 0.5)
    divisors_sum = 1 + sum(
        i + (number // i if i != number // i else 0)
        for i in range(2, sqrt_number + 1)
        if number % i == 0
    )
    return divisors_sum == number


def digit_sum(number: int):
    if number < 0:
        return False

    return sum(map(int, str(number)))


def is_armstrong(number: int):
    if number < 0:
        return False

    num_str = str(number)
    num_length = len(num_str)
    return sum(int(i) ** num_length for i in num_str) == number


def properties(number: int):
    n = ["even" if number % 2 == 0 else "odd"]
    if number >= 0 and is_armstrong(number):
        n.insert(0, "armstrong")
    return n


async def get_fun_fact(number: int):
    try:
        response = await client.get(f"http://numbersapi.com/{number}/math")
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"An error occured: {e}")
        return "No fun fact found"
