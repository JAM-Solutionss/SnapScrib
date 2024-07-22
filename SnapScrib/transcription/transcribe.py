import platform
from .transcribe_mlx import transcribe as mlx
from .transcribe_with_lightning_mlx import transcribe as lightning
from .transcribe_whisper import transcribe_audio as whisper

def check_os(path, filename):
    system = platform.system()
    if system == "Darwin":
        print("This system is running macOS.")
        choose = input("Choose 1: mlx or 2: lightning mlx: ")
        if choose == "1":
            mlx(path, filename)
        else:
            lightning(path, filename)

            
    elif system == "Windows":
        print("This system is running Windows.")
        whisper(path, filename)

    elif system == "Linux":
        print("This system is running Linux.")
        whisper(path, filename)

    else:
        print("Unknown operating system.")



if __name__ == "__main__":
    check_os()