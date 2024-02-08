import os
import sys
from colorama import Fore, Back, Style
def structure(path_to_file, count = -1):
    count+=1
    new_path = str()
    for i in os.listdir(path_to_file):
        if os.path.isdir(path_to_file + '\\' + i):
            new_path = (path_to_file + "\\" + i)
            print(f'{" "*count}{Fore.RED}{i}{Style.RESET_ALL}')
            count += 1
            structure(new_path, count)
            count-=1
        else:
            print(f'{" "*count}{Fore.BLUE}{i}{Style.RESET_ALL}')
            pass


if __name__ == "__main__":
    print(sys.argv)
    path_to_file = str(sys.argv[1])
    try:
        os.path.exists(path_to_file)
        structure(path_to_file)
    except Exception as e:
        print(str(e)+'\nTry again!')