import random
N_NUMBERS: int = 10
MIN_VALUE: int = 1
MAX_VALUE: int = 100
def random_number():
    print(f"see your random number")
    for _ in range(N_NUMBERS):
        print(random.randint(MIN_VALUE, MAX_VALUE), end=" ")
if __name__ == '__main__':
    random_number()