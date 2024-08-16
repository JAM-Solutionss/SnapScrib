from transcriber_factory import get_transcriber

if __name__ == "__main__":

    ### --- Testing transcriber factory --- ###
    transcriber = get_transcriber()
    print(transcriber)

    transcriber = get_transcriber("whisper")
    print(transcriber)

    transcriber = get_transcriber("lightning_mlx")
    print(transcriber)

    transcriber = get_transcriber("mlx")
    print(transcriber)

    transcriber = get_transcriber("youtube")
    print(transcriber)

    transcriber = get_transcriber("WhiSper")
    print(transcriber)

    transcriber = get_transcriber("lIghtning_mLx")
    print(transcriber)

    transcriber = get_transcriber("MLX")
    print(transcriber)

    transcriber = get_transcriber("YouTube")
    print(transcriber)

    transcriber = get_transcriber("irgendwas")
    print(transcriber)