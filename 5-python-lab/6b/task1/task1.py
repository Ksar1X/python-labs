import os

def change_and_show_catalog(string):
    try:
        os.chdir(string)
        print(f"✅ The directory has been successfully changed to: {os.getcwd()}")

        value = os.listdir()

        print("\nContents of the directory:")
        if not value:
            print("Directory is empty!")
        else:
            for element in value:
                print(f" ├── {element}")

    except FileNotFoundError:
        print(f"❌ Error: Directory '{string}' is not founded.")
    except PermissionError:
        print(f"❌ Error: No access permissions to the directory '{string}'.")
    except NotADirectoryError:
        print(f"❌ Error: '{string}' this is file not directory.")
    except Exception as e:
        print(f"❌ Error: {e}")

change_and_show_catalog("D:\\")