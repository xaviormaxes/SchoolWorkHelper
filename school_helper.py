#!/usr/bin/env python3
"""
School Work Helper - Voice to Text Overlay Application
Helps students articulate their thoughts by converting speech to improved written text.
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import speech_recognition as sr
import pyperclip
import threading
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()


class SchoolWorkHelper:
    def __init__(self, root):
        self.root = root
        self.root.title("School Work Helper")
        self.root.geometry("450x600")

        # Make window always on top
        self.root.attributes('-topmost', True)

        # Set window opacity (optional - can be adjusted)
        self.root.attributes('-alpha', 0.95)

        # Initialize speech recognizer
        self.recognizer = sr.Recognizer()
        self.is_recording = False

        # Initialize OpenAI client
        api_key = os.getenv('OPENAI_API_KEY')
        self.use_ai = bool(api_key)
        if self.use_ai:
            self.client = OpenAI(api_key=api_key)

        # Setup UI
        self.setup_ui()

        # Add minimize to tray hint
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def setup_ui(self):
        """Create the user interface"""
        # Main frame with padding
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)

        # Title
        title_label = ttk.Label(
            main_frame,
            text="🎤 School Work Helper",
            font=("Arial", 16, "bold")
        )
        title_label.grid(row=0, column=0, pady=(0, 10))

        # Instructions
        instructions = ttk.Label(
            main_frame,
            text="Click 'Start Recording' and speak your answer.\nThe app will help rewrite it clearly!",
            justify=tk.CENTER,
            wraplength=400
        )
        instructions.grid(row=1, column=0, pady=(0, 10))

        # Status indicator
        self.status_label = ttk.Label(
            main_frame,
            text="Ready to record",
            font=("Arial", 10),
            foreground="green"
        )
        self.status_label.grid(row=2, column=0, pady=(0, 10))

        # Control buttons frame
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=3, column=0, pady=(0, 10))

        # Record button
        self.record_button = ttk.Button(
            button_frame,
            text="🎤 Start Recording",
            command=self.toggle_recording,
            width=20
        )
        self.record_button.grid(row=0, column=0, padx=5)

        # Clear button
        self.clear_button = ttk.Button(
            button_frame,
            text="🗑️ Clear",
            command=self.clear_text,
            width=15
        )
        self.clear_button.grid(row=0, column=1, padx=5)

        # What you said section
        original_label = ttk.Label(
            main_frame,
            text="What you said:",
            font=("Arial", 11, "bold")
        )
        original_label.grid(row=4, column=0, sticky=tk.W, pady=(10, 5))

        self.original_text = scrolledtext.ScrolledText(
            main_frame,
            height=6,
            wrap=tk.WORD,
            font=("Arial", 10),
            bg="#f0f0f0"
        )
        self.original_text.grid(row=5, column=0, sticky=(tk.W, tk.E), pady=(0, 10))

        # Improved version section
        improved_label = ttk.Label(
            main_frame,
            text="Improved version:",
            font=("Arial", 11, "bold")
        )
        improved_label.grid(row=6, column=0, sticky=tk.W, pady=(10, 5))

        self.improved_text = scrolledtext.ScrolledText(
            main_frame,
            height=8,
            wrap=tk.WORD,
            font=("Arial", 10),
            bg="#e8f5e9"
        )
        self.improved_text.grid(row=7, column=0, sticky=(tk.W, tk.E), pady=(0, 10))

        # Copy button
        self.copy_button = ttk.Button(
            main_frame,
            text="📋 Copy Improved Text",
            command=self.copy_improved_text,
            state=tk.DISABLED
        )
        self.copy_button.grid(row=8, column=0, pady=(0, 5))

        # AI status
        ai_status_text = "✓ AI Enhancement Active" if self.use_ai else "⚠️ AI Not Configured (Using basic mode)"
        ai_status_color = "green" if self.use_ai else "orange"
        ai_status = ttk.Label(
            main_frame,
            text=ai_status_text,
            font=("Arial", 9),
            foreground=ai_status_color
        )
        ai_status.grid(row=9, column=0, pady=(5, 0))

        # Configure row weights for resizing
        for i in range(5, 8):
            main_frame.rowconfigure(i, weight=1)

    def toggle_recording(self):
        """Start or stop recording"""
        if not self.is_recording:
            self.start_recording()
        else:
            self.stop_recording()

    def start_recording(self):
        """Start voice recording in a separate thread"""
        self.is_recording = True
        self.record_button.config(text="⏹️ Stop Recording")
        self.status_label.config(text="🔴 Recording... Speak now!", foreground="red")

        # Run recording in separate thread to avoid blocking UI
        threading.Thread(target=self.record_audio, daemon=True).start()

    def stop_recording(self):
        """Stop voice recording"""
        self.is_recording = False
        self.record_button.config(text="🎤 Start Recording")
        self.status_label.config(text="Processing...", foreground="orange")

    def record_audio(self):
        """Record audio and convert to text"""
        try:
            with sr.Microphone() as source:
                # Adjust for ambient noise
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)

                # Record audio
                audio = self.recognizer.listen(source, timeout=30, phrase_time_limit=30)

                # Convert to text
                self.root.after(0, lambda: self.status_label.config(
                    text="Converting speech to text...",
                    foreground="blue"
                ))

                text = self.recognizer.recognize_google(audio)

                # Update UI in main thread
                self.root.after(0, lambda: self.process_text(text))

        except sr.WaitTimeoutError:
            self.root.after(0, lambda: self.show_error("No speech detected. Please try again."))
        except sr.UnknownValueError:
            self.root.after(0, lambda: self.show_error("Could not understand audio. Please speak clearly and try again."))
        except sr.RequestError as e:
            self.root.after(0, lambda: self.show_error(f"Could not connect to speech service: {e}"))
        except Exception as e:
            self.root.after(0, lambda: self.show_error(f"An error occurred: {e}"))
        finally:
            self.is_recording = False
            self.root.after(0, lambda: self.record_button.config(text="🎤 Start Recording"))

    def process_text(self, original_text):
        """Process the recognized text and improve it"""
        # Display original text
        self.original_text.delete(1.0, tk.END)
        self.original_text.insert(1.0, original_text)

        # Improve text
        if self.use_ai:
            self.status_label.config(text="Improving your answer...", foreground="blue")
            threading.Thread(target=lambda: self.improve_with_ai(original_text), daemon=True).start()
        else:
            # Basic improvement without AI
            improved = self.basic_improvement(original_text)
            self.display_improved_text(improved)

    def improve_with_ai(self, text):
        """Use AI to improve the text"""
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": """You are a helpful writing assistant for students. Your job is to take what a student says out loud and rewrite it in a clear, well-structured way that's appropriate for school assignments.

Important rules:
- Keep the student's original meaning and ideas
- Make the language more formal and clear
- Fix grammar and sentence structure
- Don't add new information or answer questions for them
- Keep it at an appropriate level for a student
- Make it concise and easy to understand"""
                    },
                    {
                        "role": "user",
                        "content": f"Please rewrite this in a clear, well-structured way for a school assignment:\n\n{text}"
                    }
                ],
                temperature=0.7,
                max_tokens=500
            )

            improved_text = response.choices[0].message.content.strip()
            self.root.after(0, lambda: self.display_improved_text(improved_text))

        except Exception as e:
            self.root.after(0, lambda: self.show_error(f"AI improvement failed: {e}"))
            # Fallback to basic improvement
            improved = self.basic_improvement(text)
            self.root.after(0, lambda: self.display_improved_text(improved))

    def basic_improvement(self, text):
        """Basic text improvement without AI"""
        # Capitalize first letter
        if text:
            text = text[0].upper() + text[1:]

        # Ensure it ends with proper punctuation
        if text and text[-1] not in '.!?':
            text += '.'

        return text

    def display_improved_text(self, improved_text):
        """Display the improved text"""
        self.improved_text.delete(1.0, tk.END)
        self.improved_text.insert(1.0, improved_text)

        self.copy_button.config(state=tk.NORMAL)
        self.status_label.config(text="✓ Ready! Copy and paste into your work.", foreground="green")

    def copy_improved_text(self):
        """Copy improved text to clipboard"""
        text = self.improved_text.get(1.0, tk.END).strip()
        if text:
            pyperclip.copy(text)
            self.status_label.config(text="✓ Copied to clipboard! Paste it into your work.", foreground="green")

            # Show a brief confirmation
            original_text = self.copy_button.config('text')[-1]
            self.copy_button.config(text="✓ Copied!")
            self.root.after(2000, lambda: self.copy_button.config(text=original_text))

    def clear_text(self):
        """Clear all text fields"""
        self.original_text.delete(1.0, tk.END)
        self.improved_text.delete(1.0, tk.END)
        self.copy_button.config(state=tk.DISABLED)
        self.status_label.config(text="Ready to record", foreground="green")

    def show_error(self, message):
        """Show error message"""
        self.status_label.config(text="Error - Ready to try again", foreground="red")
        messagebox.showerror("Error", message)

    def on_closing(self):
        """Handle window closing"""
        self.root.destroy()


def main():
    """Main application entry point"""
    root = tk.Tk()
    app = SchoolWorkHelper(root)
    root.mainloop()


if __name__ == "__main__":
    main()
