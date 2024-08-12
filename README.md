<div align="center" id="top"> 
  &#xa0;
</div>

<h1 align="center">SnapScrib</h1>

<p align="center">
  <img alt="Github top language" src="https://img.shields.io/github/languages/top/JAM-Solutionss/SnapScrib?color=56BEB8">

  <img alt="Github language count" src="https://img.shields.io/github/languages/count/JAM-Solutionss/SnapScrib?color=56BEB8">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/JAM-Solutionss/SnapScrib?color=56BEB8">
</p>

<p align="center">
  <a href="#dart-about">About</a> &#xa0; | &#xa0; 
  <a href="#rocket-technologies">Technologies</a> &#xa0; | &#xa0;
  <a href="#white_check_mark-requirements">Requirements</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-starting">Starting</a> &#xa0; | &#xa0;
  <a href="#memo-license">License</a>
</p>

## Contributors

<p align="center">
  <a href="https://github.com/cipher-shad0w" target="_blank">Cipher Shadow</a> &#xa0; | &#xa0;
  <a href="https://github.com/arvedb" target="_blank">Arved Bahde</a> &#xa0; | &#xa0;
  <a href="https://github.com/mirixy" target="_blank">Miriam</a>
</p>

<br>

## :dart: About ##

SnapScrib is a Python-based web application that retrieves subtitles from YouTube videos and summarizes them using the Groq API. Users can customize the language of the summary according to their preferences.


## Technologies ##
- **Programming Language:** Python
- **Main Libraries:**
  - `youtube_transcript_api`: For retrieving subtitles from YouTube videos.
  - `groq`: For summarizing the retrieved subtitles.
- **Web UI:** SnapScrib provides a user-friendly interface where users can input the YouTube URL and choose the language for the summary.

## :white_check_mark: Requirements ##

Before starting :checkered_flag:, you need to have [Git](https://git-scm.com) installed.


## Installation

1. **Clone the repository:**
   ```
   git clone https://github.com/JAM-Solutionss/SnapScrib.git
   cd SnapScrib
   ```

2. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

#### Configuration
Create a `.env` file in the project directory and add your Groq API key as follows:

```plaintext
GROQ_API_KEY="your_api_key_here"
```

## Usage

1. **Visit the Website:** Start the application and navigate to the web interface.
2. **Enter YouTube URL:** Provide the URL of the YouTube video you want to summarize.
3. **Select Language:** Choose the language in which the summary should be created.
4. **Receive Summary:** The subtitles will be retrieved, sent to the Groq API, and the summary will be provided in the selected language.

## Project Structure

- `requirements.txt`: List of Python dependencies.

## Technologies Used

- [Streamlit](https://streamlit.io/): Framework for creating interactive web applications.
- [Open Food Facts Python SDK](https://github.com/openfoodfacts/openfoodfacts-python): Python library for interacting with the Open Food Facts database.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

If you have any questions or need further assistance, please feel free to contact any of the contributors.

Happy coding!

---

Made with :heart: by:
- [Arved Bahde](https://github.com/arvedb)
- [Jannis Krija](https://github.com/cipher-shad0w)
- [Miriam](https://github.com/mirixy)

&#xa0;

<a href="#top">Back to top</a>