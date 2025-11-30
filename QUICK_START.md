# Quick Start Guide

## First Time Setup (5 minutes)

### 1. Install Python
- Download from [python.org](https://www.python.org/downloads/)
- Install with "Add to PATH" checked

### 2. Install Dependencies
Open Command Prompt in this folder and run:
```
pip install -r requirements.txt
```

### 3. (Optional) Add OpenAI API Key
For AI-powered improvements:
1. Get API key from [platform.openai.com](https://platform.openai.com/api-keys)
2. Copy `.env.example` to `.env`
3. Edit `.env` and paste your API key

## Running the App

### Windows
Double-click `run.bat`

### Mac/Linux
```
./run.sh
```

## Using the App

### Basic Recording
1. **Select your subject** from the dropdown:
   - General (60 sec) - Quick answers
   - Math (90 sec) - Math problems
   - Science (2 min) - Science explanations
   - History (2.5 min) - Historical writing
   - Essay (3 min) - Long-form essays

2. Click "Start Recording" (or press **Spacebar**)
3. Speak your answer in YOUR OWN WORDS (time limit shown next to subject)
4. Click "Stop Recording" or wait for it to finish
5. Review the cleaned up text (grammar fixed, YOUR words kept!)
6. Watch the word count and get encouraging messages!
7. Click "Copy Cleaned Up Text"
8. Paste into your schoolwork (Ctrl+V or Cmd+V)

### NEW! For Long Essays
1. Record introduction
2. Click **"Add More"** button
3. Record body paragraph 1
4. Click **"Add More"** button
5. Keep adding sections!
6. Everything combines automatically
7. **Save Draft** (Ctrl+S) to continue later

### Keyboard Shortcuts (Faster!)
- **Space** = Start/Stop recording
- **Ctrl+S** = Save draft
- **Ctrl+O** = Load draft
- **Ctrl+Z** = Undo

## Tips

- **Use keyboard shortcuts** - Press Space to start recording (hands-free!)
- **Choose the right subject** for best results
- **Speak naturally** using YOUR words - the app keeps them!
- **For long assignments**: Use "Add More" to record in chunks
- **Save often**: Press Ctrl+S to save your work
- Position the window so it doesn't block your work
- The window stays on top - you can move it anywhere

## No AI Detection Worries!

This app only fixes grammar/punctuation while keeping YOUR exact words and natural voice. It won't make your writing sound AI-generated because it preserves your authentic student style!

## Troubleshooting

**PyAudio won't install on Windows?**
- Download the wheel file from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio)
- Install with: `pip install PyAudio-X.X.XX-cpXX-cpXX-win_amd64.whl`

**No microphone detected?**
- Check Windows Sound settings
- Grant microphone permissions when prompted

**App not improving text (just capitalizing)?**
- You need to add an OpenAI API key in the `.env` file
- See Step 3 above

## Need More Help?

See the full [README.md](README.md) for detailed instructions.
