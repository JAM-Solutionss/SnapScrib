from file_extractor import FileExtractor

if __name__ == "__main__":
    test_path = r"youtube_audio\output\audio.mp3"
    audio_extractor = FileExtractor()
    audio = audio_extractor.extract(test_path)
    print(audio)