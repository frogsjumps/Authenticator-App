import time
import random

def authenticator(authentication_reset):
    elapsed_time = 0

    authentication_number = random.randint(100000, 999999)
    authentication_message = (f'Your authentication number is: {authentication_number}')
    print(authentication_message)

    while elapsed_time <= 10:
        start_time = time.time()
        time.sleep(10)
        current_time = time.time()
        elapsed_time = current_time - start_time

        print("\033[2J\033[H", end="", flush=True)

    authenticator(10)

authenticator(10)
