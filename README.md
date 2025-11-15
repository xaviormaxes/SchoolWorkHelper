# SchoolWorkHelper

A voice-to-text overlay application designed to help students who have difficulty articulating their thoughts in writing. This app listens to what your child says and rewrites it clearly while keeping their original meaning - perfect for online schoolwork!

## Features

- **Always-On-Top Overlay**: Window stays on top of Chrome and other applications
- **Voice Recognition**: Converts speech to text using Google's speech recognition
- **AI-Powered Rewriting**: Uses OpenAI to improve grammar and clarity while preserving meaning
- **Easy Copy-Paste**: One-click copy to clipboard for quick pasting into schoolwork
- **Privacy-Focused**: Works locally on your PC, no data stored
- **No Cheating**: Helps articulate the student's own thoughts, doesn't answer questions

## System Requirements

- **Windows 10/11** (or Linux/Mac with minor adjustments)
- **Python 3.7 or higher**
- **Microphone**
- **Internet connection** (for speech recognition and AI features)

## Installation

### Step 1: Install Python

If you don't have Python installed:

1. Download Python from [python.org](https://www.python.org/downloads/)
2. Run the installer
3. **Important**: Check "Add Python to PATH" during installation

### Step 2: Install Dependencies

1. Open Command Prompt (Windows) or Terminal (Mac/Linux)
2. Navigate to the SchoolWorkHelper folder:
   ```
   cd path\to\SchoolWorkHelper
   ```
3. Install required packages:
   ```
   pip install -r requirements.txt
   ```

**Note for Windows users**: If PyAudio installation fails, download the appropriate wheel file from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) and install it with:
```
pip install PyAudio-0.2.11-cp3xx-cp3xx-win_amd64.whl
```
(Replace `cp3xx` with your Python version, e.g., `cp312` for Python 3.12)

### Step 3: Configure OpenAI API (Optional but Recommended)

The app works in basic mode without AI, but for best results:

1. Get an OpenAI API key from [platform.openai.com/api-keys](https://platform.openai.com/api-keys)
2. Copy `.env.example` to `.env`:
   ```
   copy .env.example .env
   ```
3. Edit `.env` and add your API key:
   ```
   OPENAI_API_KEY=sk-your-actual-api-key-here
   ```

**Cost**: OpenAI API usage is very affordable - typically less than $0.01 per rewrite using GPT-3.5-turbo

## Usage

### Starting the App

**Windows:**
- Double-click `run.bat`, or
- Run `python school_helper.py` in Command Prompt

**Mac/Linux:**
- Run `chmod +x run.sh` (first time only)
- Run `./run.sh`, or
- Run `python3 school_helper.py` in Terminal

### How to Use

1. **Position the window**: The app window will stay on top of other windows. Position it where it won't block important parts of the schoolwork screen.

2. **Click "Start Recording"**: The status will show "Recording... Speak now!"

3. **Speak the answer**: Have your son speak his thoughts naturally, as if explaining to a friend.

4. **Click "Stop Recording"** (or it stops automatically after 30 seconds)

5. **Review the results**:
   - "What you said" shows the original transcription
   - "Improved version" shows the rewritten, clearer text

6. **Copy and paste**: Click "Copy Improved Text" and paste it into the schoolwork (Ctrl+V)

### Tips for Best Results

- **Speak clearly** but naturally
- **Use complete thoughts**: Try to speak in full sentences
- **Keep it under 30 seconds** per recording for best results
- **Review before submitting**: The student should always read and understand what they're submitting
- **Multiple recordings**: For longer answers, break them into chunks

## Troubleshooting

### "No module named 'pyaudio'" error
- On Windows: Download and install the PyAudio wheel file (see Installation Step 2)
- On Mac: Run `brew install portaudio && pip install pyaudio`
- On Linux: Run `sudo apt-get install python3-pyaudio`

### "Could not find microphone" error
- Check that your microphone is connected and enabled
- Give the app microphone permissions if prompted
- Try selecting a different microphone in Windows Sound settings

### "AI Not Configured" warning
- The app will work in basic mode (just fixes capitalization and punctuation)
- For full AI rewriting, add an OpenAI API key to the `.env` file

### Voice recognition not working well
- Reduce background noise
- Speak clearly and at a moderate pace
- Check your microphone levels in Windows Sound settings
- Move closer to the microphone

## Privacy & Security

- Voice data is sent to Google for speech-to-text conversion (industry standard)
- Text is sent to OpenAI for improvement if API key is configured
- No data is stored or logged by this application
- All processing happens in real-time; nothing is saved

## Educational Use

This tool is designed to help students with:
- Learning differences
- Speech-to-writing challenges
- Articulation difficulties
- Confidence in expressing ideas

**Important**: This tool helps students express their *own* thoughts more clearly. It should not be used to:
- Generate answers the student doesn't understand
- Complete work the student hasn't thought about
- Replace learning and understanding

## License

This project is provided as-is for educational purposes.

## Support

For issues or questions, please open an issue on GitHub or contact the developer
