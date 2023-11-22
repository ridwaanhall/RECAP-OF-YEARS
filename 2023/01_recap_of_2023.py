import time

def type_with_delay(text, delay=3.5):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)

text_to_type = "and with that the 2023 season"
type_with_delay(text_to_type)
