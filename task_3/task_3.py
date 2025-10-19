from pathlib import Path
from colorama import Fore

def iterate_folder(path, prefix=""): 
    # Виведення переліку всіх файлів та піддиректорій
    for path in path.iterdir():
        space = "   "
        if path.is_dir():
            print(f"{prefix + space}{Fore.BLUE}{path.name}/")
        else:
            print(f"{prefix + space}{Fore.GREEN}{path.name}")
        
        if path.is_dir():   
            # print(f"\t{Fore.BLUE}{path.name}")
            iterate_folder(path, prefix + space)

try:
    file = Path("pictures") 
    print(f"{Fore.BLUE}{file.name}/")
    iterate_folder(file)
except FileNotFoundError:
    # Handle the case where the file is not found
    print("Error: The specified file was not found.")   
except NotADirectoryError:
    print("Error: The path provided is not a directory.")