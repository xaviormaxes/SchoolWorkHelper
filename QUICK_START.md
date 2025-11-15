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

1. Click "Start Recording"
2. Speak your answer (up to 30 seconds)
3. Click "Stop Recording" or wait for it to finish
4. Review the improved text
5. Click "Copy Improved Text"
6. Paste into your schoolwork (Ctrl+V or Cmd+V)

## Tips

- Speak naturally and clearly
- Use complete sentences when possible
- Position the window so it doesn't block your work
- The window stays on top - you can move it anywhere
- Break long answers into multiple recordings

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
