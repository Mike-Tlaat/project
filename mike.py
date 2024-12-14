import tkinter as tk
from tkinter import messagebox, ttk
import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty("voices")
default_voice = voices[0].id  
engine.setProperty("voice", default_voice)
engine.setProperty("rate", 150) 

def play_text():
    """Convert text to speech and play the audio."""
    text = text_entry.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Warning", "Please enter some text to convert.")
        return

    try:
        language = lang_var.get()
        if language == "English":
            engine.setProperty("voice", voices[0].id)  
        elif language == "Arabic":
            arabic_voice = next((v for v in voices if "Arabic" in v.name), None)
            if arabic_voice:
                engine.setProperty("voice", arabic_voice.id)
            else:
                messagebox.showerror("Error", "Arabic voice is not supported on your system.")
                return
        else:
            selected_voice = next((v for v in voices if language in v.name), None)
            if selected_voice:
                engine.setProperty("voice", selected_voice.id)
            else:
                messagebox.showerror("Error", f"Voice for '{language}' is not supported on your system.")
                return

        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")

def clear_text():
    """Clear the text entry."""
    text_entry.delete("1.0", tk.END)

def exit_app():
    """Exit the application."""
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Text-to-Speech App")
root.geometry("400x400")
root.resizable(False, False)

# Set background color
root.configure(bg="#eaf4f4")

# Define styles
style = ttk.Style()
style.theme_use("default")  # Use the default theme
style.configure(
    "TButton",
    font=("Arial", 12, "bold"),
    padding=5,
    background="#007ACC",
    foreground="white",
    borderwidth=2,
)
style.map(
    "TButton",
    background=[("active", "#005A9E")],
    foreground=[("active", "white")],
)
style.configure("TLabel", background="#eaf4f4", font=("Arial", 12, "bold"), foreground="#333333")
style.configure("TFrame", background="#eaf4f4")
style.configure("TOptionMenu", background="#eaf4f4", foreground="#333333", font=("Arial", 12))

# Language selection
lang_var = tk.StringVar(value="English")
languages = {"English": "en", "Arabic": "ar", "French": "fr", "Spanish": "es", "German": "de", "Chinese": "zh", "Hindi": "hi"}
ttk.Label(root, text="Select Language:").pack(pady=5)
lang_menu = ttk.OptionMenu(root, lang_var, "English", *languages.keys())
lang_menu.pack(pady=5)

# Create a text entry widget
text_entry = tk.Text(root, wrap=tk.WORD, height=10, width=40, font=("Arial", 12), bg="#ffffff", fg="#333333", bd=2, relief="solid")
text_entry.pack(pady=10)

# Create buttons
button_frame = ttk.Frame(root)
button_frame.pack(pady=10)

play_button = ttk.Button(button_frame, text="Play", command=play_text)
play_button.grid(row=0, column=0, padx=5)

clear_button = ttk.Button(button_frame, text="Clear", command=clear_text)
clear_button.grid(row=0, column=1, padx=5)

exit_button = ttk.Button(button_frame, text="Exit", command=exit_app)
exit_button.grid(row=0, column=2, padx=5)

# Run the application
root.mainloop()