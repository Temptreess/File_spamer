import os
import random
import string


def generate_random_filename(length=20):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def generate_random_text():
    text_length = random.randint(100000, 100000000)
    letters = string.ascii_letters + string.digits + string.punctuation + string.whitespace
    return ''.join(random.choices(letters, k=text_length))


def create_random_file(file_count):
    for _ in range(file_count):
        filename = generate_random_filename()
        text = generate_random_text()
        with open(filename + ".txt", 'w') as file:
            file.write(text)
        print("Created:" + filename + ".txt")


current_directory = os.getcwd()


file_count = int(input("How many files do you want to do? "))


create_random_file(file_count)
