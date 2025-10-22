from pathlib import Path
from colorama import Fore
import sys

def iterate_folder(path, prefix=""): 
    
    # Виведення переліку всіх файлів та піддиректорій
    for path in path.iterdir():
        space = "   "
        if path.is_dir():
            print(f"{prefix + space}{Fore.BLUE}{path.name}/")
        else:
            print(f"{prefix + space}{Fore.GREEN}{path.name}")
        
        if path.is_dir():   
            iterate_folder(path, prefix + space)

def main():
    try:
        file = sys.argv[1]
        path_file = Path(file)
        print(f"{Fore.BLUE}{path_file.name}/")
        iterate_folder(path_file)
        
    except FileNotFoundError:
        # Handle the case where the file is not found
        print("Error: The specified file was not found.")   
    except NotADirectoryError:
        print("Error: The path provided is not a directory.")

if __name__ == "__main__":
    main()
    
        