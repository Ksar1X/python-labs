import os

def create_directory(dir_name):
    try:
        os.makedirs(DIR_NAME, exist_ok=True)
        print(f"Directory {dir_name} created")
    except FileNotFoundError:
        print(f"❌ Error: Directory '{dir_name}' is not founded.")
    except Exception as e:
        print(f"❌ Error: {e}")


def rename_directory(current_dir, new_dir):
    try:
        os.rename(current_dir, new_dir)
        print(f"Directory {current_dir} renamed to {new_dir}")
    except FileNotFoundError:
        print(f"❌ Error: Directory '{current_dir}' is not founded.")
    except FileExistsError:
        print(f"❌ Error: Directory with name: '{new_dir}' is already exist.")
    except Exception as e:
        print(f"❌ Error: {e}")


DIR_NAME = str(input("Write name of directory: "))
create_directory(DIR_NAME)
new_directory_name = str(input("Write name of new directory: "))
rename_directory(DIR_NAME, new_directory_name)
