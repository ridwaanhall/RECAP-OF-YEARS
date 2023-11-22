import time

def type_with_total_time(text, total_time=3.5):
    # Calculate the delay per character
    delay = total_time / len(text)

    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)

text_to_type = "and with that the 2023 season comes to an end, good night <3"
total_typing_time = 5.3

type_with_total_time(text_to_type, total_typing_time)

