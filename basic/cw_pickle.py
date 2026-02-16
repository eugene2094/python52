import pickle
import os
import string

numbers = [1, 2, 3, 4, 5]

serial_data = pickle.dumps(numbers)
print(f"Serial data: {serial_data}")
deserialized_data = pickle.loads(serial_data)
print(f"Deserialized data: {deserialized_data}")
print(numbers)


def create_path(file_name):
    script_dir = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(script_dir, file_name)


def serialize(file_name, data):
    with open(create_path(file_name), 'wb') as file:
        pickle.dump(data, file)


def deserialize(file_name):
    with open(create_path(file_name), 'rb') as file:
        data = pickle.load(file)
    return data


try:
    letters = [s for s in string.ascii_lowercase]
    file_name = 'letters.dat'
    print(f"original leters: {letters}")

    serialize(file_name, letters)
    letters_restored = deserialize(file_name)
    print(f"Deserialized letters: {letters_restored}")

except Exception as e:
    print(e)
