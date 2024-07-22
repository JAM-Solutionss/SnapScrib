import platform
from transcribe_mlx import transcribe as mlx
from transcribe_with_lightning_mlx import transcribe as lightning

def check_os():
    system = platform.system()
    if system == "Darwin":
        print("This system is running macOS.")
        choose = input("Choose 1: mlx or 2: lightning mlx: ")
        if choose == "1":
            mlx()
        else:
            lightning()

            
    elif system == "Windows":
        print("This system is running Windows.")
    elif system == "Linux":
        print("This system is running Linux.")
    else:
        print("Unknown operating system.")



if __name__ == "__main__":
    check_os()