<div align="center" id="top"> 
  &#xa0;
</div>

<h1 align="center">SnapScrib</h1>

<p align="center">
  <img alt="Github top language" src="https://img.shields.io/github/languages/top/JAM-Solutionss/SnapScrib?color=56BEB8">

  <img alt="Github language count" src="https://img.shields.io/github/languages/count/JAM-Solutionss/SnapScrib?color=56BEB8">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/JAM-Solutionss/SnapScrib?color=56BEB8">
</p>

<div align="center">

  [About](#dart-about) &#xa0; | &#xa0; 
  [Technologies](#rocket-technologies) &#xa0; | &#xa0; 
  [Requirements](#white_check_mark-requirements) &#xa0; | &#xa0; 
  [Starting](#checkered_flag-starting) &#xa0; | &#xa0; 
  [Project structure](#file_folder-project-structure) &#xa0; | &#xa0; 
  [License](#license)

</div>

<br>

## Contributors

<div align="center">

  [Arved Bahde](https://github.com/arvedb) &#xa0; | &#xa0;
  [Jannis Krija](https://github.com/cipher-shad0w) &#xa0; | &#xa0;
  [Miriam](https://github.com/mirixy) &#xa0; | &#xa0;
  [Tobias](https://github.com/Tatoffel)

</div>

<br>

## :dart: About ##

SnapScrib is a Python-based application that extract the audio from the given file, transcribe the audio and summarizes the transcription using the Groq API. Users can customize the transcriber and the summarizer for the summary according to their preferences.

<br>

## :rocket: Technologies ##
- **Programming Language:** Python
- **Main Libraries:**
  - `PyQt6`: To build the frontend (the UI).
  - `yt_dlp`: To extract the audio from the file.
  - `youtube_transcript_api`: For retrieving subtitles from YouTube videos.
  - `whisper`: To transcribe the extracted audiofile.
  - `groq`: For summarizing the retrieved subtitles.

- **UI:** SnapScrib provides a user-friendly interface where users can input the YouTube URL or a audio/video file and choose the transcriber and the summarizer for the summary.

<br>

## :white_check_mark: Requirements ##

Before starting :checkered_flag:, you need to have [Git](https://git-scm.com) installed.

<br>

## :checkered_flag: Starting

1. **Clone the repository:**
   ```
   git clone https://github.com/JAM-Solutionss/SnapScrib.git
   cd SnapScrib
   ```

2. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

<br>
#### Configuration
Create a `.env` file in the project directory and add your Groq API key as follows:

```plaintext
GROQ_API_KEY="your_api_key_here"
```

<br>

## Usage

1. **Open the application:** Start the application and navigate to the web interface.
2. **Enter a YouTube URL or paste an audio/video file:** Provide the URL of the YouTube video or the audio/video file you want to summarize.
3. **Select a transcriber and a summarizer:** Choose the appropriate transcriber and summarizer from the available options.
4. **Start -> summarize:** Press the button to summarize the video/audio.
5. **Receive Summary:** You can see the summary on the right.

<br>

## :file_folder: Project Structure ##

- `LICENSE`: License file for the project.
- `README.md`: Project documentation.
- `docs/`: Documentation directory.
  - `CONTRIBUTION.md`: Guidelines for contributing to the project.
- `requirements.txt`: All packages you need to run this app.
- `src/`: Contains the source code of the project.
  - `app.py`: Main application component.
  - `backend/`: Backend logic directory.
    - `modules/`: Modules directory.
      - `app/`: Application-specific modules.
        - `app_data.py`: Application data handling module.
      - `audio/`: Audio processing modules.
        - `audio_data.py`: Audio data handling module.
        - `audio_extractor_factory.py`: Factory for creating audio extractors.
        - `audio_extractor_interface.py`: Interface for audio extractors.
        - `download/`: Directory for downloaded audio files.
        - `file_extractor.py`: Module for extracting audio from files.
        - `testing_extraction.py`: Tests for audio extraction.
        - `youtube_extractor.py`: Module for extracting audio from YouTube.
      - `summary/`: Summary generation modules.
        - `dummy_text.py`: Dummy text for testing.
        - `summarizer_factory.py`: Factory for creating summarizers.
        - `summarizer_interface.py`: Interface for summarizers.
        - `summarizer_llama.py`: Summarizer implementation using LLaMA.
        - `summary_data.py`: Summary data handling module.
        - `testing_summarizer.py`: Tests for summarizers.
      - `transcription/`: Transcription modules.
        - `lightning_mlx_transcriber.py`: Transcriber using Lightning MLX.
        - `mlx_transcriber.py`: MLX transcriber implementation.
        - `testing_transcriber.py`: Tests for transcribers.
        - `transcribe.py`: Main transcription module.
        - `transcribe_mlx.py`: Transcription using MLX.
        - `transcribe_whisper.py`: Transcription using Whisper.
        - `transcriber_factory.py`: Factory for creating transcribers.
        - `transcriber_interface.py`: Interface for transcribers.
        - `transcription_data.py`: Transcription data handling module.
        - `whisper_transcriber.py`: Whisper transcriber implementation.
        - `youtube_transcriber.py`: YouTube transcriber implementation.
      - `youtube_audio/`: YouTube audio extraction modules.
        - `extract_audio.py`: Module for extracting audio from YouTube.
    - `utils/`: Utility modules.
      - `logger_config.py`: Logger configuration module.
      - `status_tracker.py`: Status tracking module.
- `tests/`: Contains unit and integration tests.
  - `test_youtube_extractor.py`: Tests for the YouTube extractor module.

<br>

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

<br>

## Collaborate
If you have any questions or need further assistance, please feel free to contact any of the contributors.
Happy coding!

<br>
---

Made with :heart: by:

<div align="center">

  [Arved Bahde](https://github.com/arvedb) &#xa0; | &#xa0;
  [Jannis Krija](https://github.com/cipher-shad0w) &#xa0; | &#xa0;
  [Miriam](https://github.com/mirixy) &#xa0; | &#xa0;
  [Tobias](https://github.com/Tatoffel)

</div>

&#xa0;

<a href="#top">Back to top</a>