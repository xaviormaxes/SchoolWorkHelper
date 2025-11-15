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
        self.root.geometry("500x700")

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

        # Subject-specific settings
        self.subject_prompts = {
            "General": {
                "prompt": """You are helping a student clean up their spoken words for a school assignment. Your job is to make MINIMAL changes - just fix obvious errors while keeping their natural voice.

CRITICAL RULES to avoid AI detection:
- Use the student's EXACT words and phrasing whenever possible
- Only fix grammar mistakes, capitalization, and punctuation
- Keep the student's vocabulary - don't use fancier words
- Maintain their casual, natural student voice
- Add sentence breaks where they pause
- DO NOT make it sound formal or polished
- DO NOT add complex vocabulary or transitions
- The goal is to sound like THEY wrote it, just cleaned up
- Keep it simple and natural like a real student would write""",
                "max_tokens": 600,
                "time_limit": 60
            },
            "Essay": {
                "prompt": """You are helping a student clean up their spoken words for an essay. Make MINIMAL changes to preserve their authentic voice and avoid AI detection.

CRITICAL RULES to avoid AI detection:
- Use the student's EXACT words and phrasing as much as possible
- Only fix grammar, capitalization, and punctuation errors
- Break into paragraphs where they pause or change topics
- Keep their vocabulary - don't substitute "better" words
- Maintain their natural, age-appropriate writing voice
- DO NOT add fancy transitions or academic phrases
- DO NOT make it overly formal or structured
- Keep contractions if they use them (it's, don't, can't)
- The result should sound like a real student wrote it, not AI
- Simple and authentic is better than polished and formal""",
                "max_tokens": 1500,
                "time_limit": 180
            },
            "Math": {
                "prompt": """You are helping a student clean up their math explanation. Make MINIMAL changes to preserve their authentic voice and avoid AI detection.

CRITICAL RULES to avoid AI detection:
- Use the student's EXACT words and explanation
- Only fix grammar and add punctuation
- Keep their vocabulary - don't use formal math jargon unless they did
- Maintain their casual explanation style
- Add line breaks between steps if needed
- DO NOT add steps they didn't mention
- DO NOT make it sound textbook-formal
- Keep phrases like "so", "then", "because" if they used them
- The result should sound like a real student explaining, not a textbook
- Simple and natural is better than technically perfect""",
                "max_tokens": 800,
                "time_limit": 90
            },
            "History": {
                "prompt": """You are helping a student clean up their history answer. Make MINIMAL changes to preserve their authentic voice and avoid AI detection.

CRITICAL RULES to avoid AI detection:
- Use the student's EXACT words and interpretation
- Only fix grammar, capitalization, and punctuation
- Keep their vocabulary and phrasing
- Maintain their natural student writing voice
- Break into paragraphs only where they naturally pause
- DO NOT add formal historical language they didn't use
- DO NOT make it sound like a history textbook
- Keep their casual connections like "and then", "so", "because"
- The result should sound like a real student wrote it
- Authentic student voice is more important than formality""",
                "max_tokens": 1200,
                "time_limit": 150
            },
            "Science": {
                "prompt": """You are helping a student clean up their science explanation. Make MINIMAL changes to preserve their authentic voice and avoid AI detection.

CRITICAL RULES to avoid AI detection:
- Use the student's EXACT words and observations
- Only fix grammar and punctuation errors
- Keep their vocabulary - don't add scientific jargon they didn't use
- Maintain their natural explanation style
- Break into sentences/paragraphs only where natural
- DO NOT make it sound like a science textbook
- DO NOT add formal scientific language
- Keep their casual connectors like "so", "then", "because"
- The result should sound like a real student explaining
- Natural and authentic beats formal and polished""",
                "max_tokens": 1000,
                "time_limit": 120
            }
        }

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
            text="Select subject, click 'Start Recording' and speak your answer.\nWe'll clean up grammar while keeping YOUR voice!",
            justify=tk.CENTER,
            wraplength=450
        )
        instructions.grid(row=1, column=0, pady=(0, 10))

        # Subject selection frame
        subject_frame = ttk.Frame(main_frame)
        subject_frame.grid(row=2, column=0, pady=(0, 10))

        subject_label = ttk.Label(
            subject_frame,
            text="Subject:",
            font=("Arial", 10, "bold")
        )
        subject_label.grid(row=0, column=0, padx=(0, 10))

        self.subject_var = tk.StringVar(value="General")
        self.subject_dropdown = ttk.Combobox(
            subject_frame,
            textvariable=self.subject_var,
            values=list(self.subject_prompts.keys()),
            state="readonly",
            width=15
        )
        self.subject_dropdown.grid(row=0, column=1)
        self.subject_dropdown.bind("<<ComboboxSelected>>", self.on_subject_change)

        # Time limit display
        self.time_label = ttk.Label(
            subject_frame,
            text="(60 sec max)",
            font=("Arial", 9),
            foreground="gray"
        )
        self.time_label.grid(row=0, column=2, padx=(10, 0))

        # Status indicator
        self.status_label = ttk.Label(
            main_frame,
            text="Ready to record",
            font=("Arial", 10),
            foreground="green"
        )
        self.status_label.grid(row=3, column=0, pady=(0, 10))

        # Control buttons frame
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=4, column=0, pady=(0, 10))

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
        original_label.grid(row=5, column=0, sticky=tk.W, pady=(10, 5))

        self.original_text = scrolledtext.ScrolledText(
            main_frame,
            height=6,
            wrap=tk.WORD,
            font=("Arial", 10),
            bg="#f0f0f0"
        )
        self.original_text.grid(row=6, column=0, sticky=(tk.W, tk.E), pady=(0, 10))

        # Cleaned up version section
        improved_label = ttk.Label(
            main_frame,
            text="Cleaned up version:",
            font=("Arial", 11, "bold")
        )
        improved_label.grid(row=7, column=0, sticky=tk.W, pady=(10, 5))

        self.improved_text = scrolledtext.ScrolledText(
            main_frame,
            height=8,
            wrap=tk.WORD,
            font=("Arial", 10),
            bg="#e8f5e9"
        )
        self.improved_text.grid(row=8, column=0, sticky=(tk.W, tk.E), pady=(0, 10))

        # Copy button
        self.copy_button = ttk.Button(
            main_frame,
            text="📋 Copy Cleaned Up Text",
            command=self.copy_improved_text,
            state=tk.DISABLED
        )
        self.copy_button.grid(row=9, column=0, pady=(0, 5))

        # AI status
        ai_status_text = "✓ Grammar Cleanup Active (preserves your voice)" if self.use_ai else "⚠️ AI Not Configured (Using basic mode)"
        ai_status_color = "green" if self.use_ai else "orange"
        ai_status = ttk.Label(
            main_frame,
            text=ai_status_text,
            font=("Arial", 9),
            foreground=ai_status_color
        )
        ai_status.grid(row=10, column=0, pady=(5, 0))

        # Configure row weights for resizing
        for i in range(6, 9):
            main_frame.rowconfigure(i, weight=1)

    def on_subject_change(self, event=None):
        """Handle subject selection change"""
        subject = self.subject_var.get()
        time_limit = self.subject_prompts[subject]["time_limit"]
        self.time_label.config(text=f"({time_limit} sec max)")

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
            # Get time limit based on selected subject
            subject = self.subject_var.get()
            time_limit = self.subject_prompts[subject]["time_limit"]

            with sr.Microphone() as source:
                # Adjust for ambient noise
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)

                # Record audio with subject-specific time limit
                audio = self.recognizer.listen(source, timeout=time_limit, phrase_time_limit=time_limit)

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

        # Clean up text
        if self.use_ai:
            self.status_label.config(text="Cleaning up grammar and punctuation...", foreground="blue")
            threading.Thread(target=lambda: self.improve_with_ai(original_text), daemon=True).start()
        else:
            # Basic improvement without AI
            improved = self.basic_improvement(original_text)
            self.display_improved_text(improved)

    def improve_with_ai(self, text):
        """Use AI to improve the text"""
        try:
            # Get subject-specific settings
            subject = self.subject_var.get()
            subject_config = self.subject_prompts[subject]

            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": subject_config["prompt"]
                    },
                    {
                        "role": "user",
                        "content": f"Clean up this spoken text with MINIMAL changes. Only fix grammar/punctuation. Keep their exact words and natural voice:\n\n{text}"
                    }
                ],
                temperature=0.3,
                max_tokens=subject_config["max_tokens"]
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
