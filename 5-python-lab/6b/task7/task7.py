import struct
import pickle
import os

file_name = "binary.pkl"
number = 123456789

try:
    binary_data = struct.pack('i', number)
    print(f"Data in binary code: {binary_data}")
    with open(file_name, "wb") as file:
        pickle.dump(binary_data, file)
    print("Data has been saved in file!")

    del binary_data

    if os.path.exists(file_name):
        with open(file_name, "rb") as file:
            binary_data = pickle.load(file)
        print("Data has been loaded from file!")

    data = struct.unpack('i', binary_data)[0]
    print(f"Data: {data}")

except Exception as e:
    print(f"Something went wrong! {e}")