---

# SnapScrib

### Project Description
SnapScrib is a Python-based web application that retrieves subtitles from YouTube videos and summarizes them using the Groq API. Users can customize the language of the summary according to their preferences.

### Technologies Used
- **Programming Language:** Python
- **Main Libraries:**
  - `youtube_transcript_api`: For retrieving subtitles from YouTube videos.
  - `groq`: For summarizing the retrieved subtitles.
- **Web UI:** SnapScrib provides a user-friendly interface where users can input the YouTube URL and choose the language for the summary.

### Installation and Setup

#### Dependencies
Ensure all necessary Python dependencies are installed by running the following command:

```bash
pip install -r requirements.txt
```

#### Configuration
Create a `.env` file in the project directory and add your Groq API key as follows:

```plaintext
GROQ_API_KEY="your_api_key_here"
```

### Usage

1. **Visit the Website:** Start the application and navigate to the web interface.
2. **Enter YouTube URL:** Provide the URL of the YouTube video you want to summarize.
3. **Select Language:** Choose the language in which the summary should be created.
4. **Receive Summary:** The subtitles will be retrieved, sent to the Groq API, and the summary will be provided in the selected language.

### Contributors
- [Arved Bahde](https://github.com/arvedb)
- [Jannis Krija](https://github.com/cipher-shad0w)
- [Miriam](https://github.com/mirixy)

### Contributing
To contribute to SnapScrib:

1. **Fork the repository** and create a new branch for your changes.
2. **Implement your changes** and test them.
3. **Submit a Pull Request** for review.

### License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---