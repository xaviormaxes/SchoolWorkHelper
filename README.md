# SchoolWorkHelper

A voice-to-text overlay application designed to help students who have difficulty articulating their thoughts in writing. This app listens to what your child says and cleans up grammar/punctuation while preserving THEIR authentic voice - perfect for online schoolwork!

## Features

### Core Functionality
- **Always-On-Top Overlay**: Window stays on top of Chrome and other applications
- **Voice Recognition**: Converts speech to text using Google's speech recognition
- **Subject-Specific Modes**: Optimized for Essays, Math, History, Science, and General work
- **Extended Recording Times**: Up to 3 minutes for essays, customized by subject
- **Minimal AI Cleanup**: Only fixes grammar/punctuation - keeps the student's EXACT words and natural voice
- **Avoids AI Detection**: Designed to preserve authentic student writing style

### NEW - Productivity Features
- **Word Count Display**: Live word count with progress tracking
- **Encouraging Messages**: Positive reinforcement as your son works ("Great start!", "Nice progress!")
- **Multiple Recordings**: Record in segments and combine them - perfect for long essays
- **Add More Button**: Keep adding to your work without losing previous parts
- **Undo Function**: Oops? Go back to the previous version
- **Save & Load Drafts**: Save work in progress and come back to it later
- **Keyboard Shortcuts**:
  - **Space** = Start/Stop recording (hands-free!)
  - **Ctrl+S** = Save draft
  - **Ctrl+O** = Load draft
  - **Ctrl+Z** = Undo last action

### Student-Friendly
- **Easy Copy-Paste**: One-click copy to clipboard for quick pasting into schoolwork
- **Privacy-Focused**: Works locally on your PC, no data stored
- **No Cheating**: Helps express the student's own thoughts clearly, doesn't rewrite or change meaning

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

2. **Select the subject**: Choose from Essay, Math, History, Science, or General
   - **General**: 60 seconds - Short answers and quick responses
   - **Math**: 90 seconds - Math problems and explanations
   - **Science**: 2 minutes - Scientific explanations and lab reports
   - **History**: 2.5 minutes - Historical analysis and narratives
   - **Essay**: 3 minutes - Long-form writing and multi-paragraph responses

3. **Click "Start Recording"**: The status will show "Recording... Speak now!"

4. **Speak the answer**: Have your son speak his thoughts naturally, as if explaining to a friend.

5. **Click "Stop Recording"** when finished (or it stops automatically at the time limit)

6. **Review the results**:
   - "What you said" shows the original transcription
   - "Cleaned up version" shows the text with grammar/punctuation fixed but YOUR words preserved

7. **Copy and paste**: Click "Copy Cleaned Up Text" and paste it into the schoolwork (Ctrl+V)

### NEW Features - How to Use

#### Word Count & Encouragement
- Watch the word count update in real-time as you work
- Get encouraging messages:
  - 50+ words: "Great start! Keep going! 💪"
  - 100+ words: "Nice progress! You're doing awesome! ⭐"
  - 200+ words: "Wow! That's a lot of great work! 🎉"

#### Multiple Recordings (Perfect for Essays!)
1. Record your first part (introduction)
2. Review the cleaned up text
3. Click **"Add More"** button
4. Record the next part (body paragraph)
5. Repeat for as many sections as needed
6. All sections combine automatically with proper spacing
7. Copy the complete essay when done!

#### Save & Load Drafts
- **Save**: Click "Save" button or press **Ctrl+S** to save your work
- **Load**: Click "Load" button or press **Ctrl+O** to continue where you left off
- Great for assignments that take multiple sessions!

#### Undo
- Made a mistake? Click "Undo" or press **Ctrl+Z**
- Goes back to the previous version
- Can undo multiple times

#### Keyboard Shortcuts (Hands-Free!)
- **Spacebar**: Start/Stop recording (no mouse needed!)
- **Ctrl+S**: Quick save
- **Ctrl+O**: Quick load
- **Ctrl+Z**: Undo
- Just press Space to toggle recording while your son thinks!

### Tips for Best Results

- **Choose the right subject mode**: This optimizes the cleanup for the type of work
- **Speak clearly** but naturally - use your own words!
- **Use complete thoughts**: Try to speak in full sentences
- **For essays**: Speak in logical chunks (introduction, body paragraphs, conclusion)
- **For math**: Explain each step of your reasoning in your own way
- **For history/science**: Organize your thoughts chronologically or by topic
- **Review before submitting**: The student should always read and understand what they're submitting
- **Take advantage of extended time**: Essays can be up to 3 minutes - no need to rush!

### About AI Detection

**This app is designed to AVOID AI detection flags:**

- ✓ **Preserves the student's authentic voice** - We keep their exact words and phrasing
- ✓ **Minimal changes only** - Just fixes grammar, capitalization, and punctuation
- ✓ **No AI rewriting** - We don't substitute fancy words or formal language
- ✓ **Keeps natural student style** - Maintains casual connectors like "so", "then", "because"
- ✓ **No textbook language** - The output sounds like a real student wrote it

**How it works:** The app acts like a helpful friend checking over the work - fixing typos and grammar mistakes while keeping the student's own voice and ideas completely intact. This is NOT the same as AI writing the content, which is why it shouldn't trigger AI detection tools.

**Important:** The student must speak their OWN thoughts and ideas. The app just helps them express those thoughts more clearly on paper.

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
