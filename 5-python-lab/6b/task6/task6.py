import pickle
import os

first_list = ["apple", "banana", "cherry"]
second_list = [10, 20, 30, 40]
third_list = ["Python", 3.13, True]

all_lists = [first_list, second_list, third_list]
file_name = "text.pkl"

try:
    with open(file_name, "wb") as file:
        pickle.dump(all_lists, file)
    print(f"Data has been saved in {file_name}")
except PermissionError:
    print(f"You cannot save data in this directory")
except Exception as e:
    print(f"Something went wrong: {e}")

del first_list, second_list, third_list, all_lists
print("Lists has been deleted from the memory!")


try:
    if os.path.exists(file_name):
        with open(file_name, "rb") as file:
            loaded_lists = pickle.load(file)
        print("Data has been loaded!")

    for i, list in enumerate(loaded_lists, 1):
        print(f"{i}: {list}")
except FileNotFoundError:
    print(f"File {file_name} not found!")
except pickle.UnpicklingError:
    print("Unpickling failed!")
except EOFError:
    print("File is empty!")
except Exception as e:
    print(f"Something went wrong: {e}.")
