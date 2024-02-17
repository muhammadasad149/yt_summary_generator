# YouTube Transcript to Detailed Notes Converter

This is a web application built using Streamlit that converts YouTube video transcripts into detailed notes. It utilizes Google's GenerativeAI (specifically the Gemini model) and the YouTube Transcript API to generate detailed summaries of videos.

## Features

- Extracts transcript details from YouTube videos.
- Generates detailed notes summarizing the video content.
- Allows customization of the summary length.
- Displays thumbnail of the YouTube video.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/muhammadasad149/yt_summary_generator.git

   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   - Create a `.env` file in the root directory.
   - Add your Google API key:
     ```dotenv
     GOOGLE_API_KEY=your_api_key_here
     ```

4. Run the application:
   ```bash
   streamlit run app.py
   ```

## Usage

1. Enter the YouTube video link in the provided text input.
2. Adjust the desired summary length using the slider.
3. Click on the "Get Detailed Notes" button.
4. The detailed notes will be displayed below.

## Dependencies

- Streamlit
- dotenv
- google (GenerativeAI)
- youtube_transcript_api

## Configuration

- The application requires a Google API key to access the GenerativeAI models.
- YouTubeTranscriptApi is used to fetch the transcript of YouTube videos.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.
