import pygame
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

# Initialize pygame
pygame.mixer.init()

# Create a tkinter window
root = tk.Tk()
root.title("Python Music Player")

# Create a function to load and play a song
def play_music():
    file_path = filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3")])
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play(loops=0)

# Create a function to pause the song
def pause_music():
    pygame.mixer.music.pause()

# Create a function to unpause the song
def unpause_music():
    pygame.mixer.music.unpause()

# Create buttons for controlling the music
play_button = ttk.Button(root, text="Play", command=play_music)
pause_button = ttk.Button(root, text="Pause", command=pause_music)
unpause_button = ttk.Button(root, text="Unpause", command=unpause_music)

play_button.pack()
pause_button.pack()
unpause_button.pack()

root.mainloop()
import pygame
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

# Initialize pygame
pygame.mixer.init()

# Create a tkinter window
root = tk.Tk()
root.title("Python Music Player")

# Create a function to load and play a song
def play_music():
    file_path = filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3")])
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play(loops=0)

# Create a function to pause the song
def pause_music():
    pygame.mixer.music.pause()

# Create a function to unpause the song
def unpause_music():
    pygame.mixer.music.unpause()

# Create buttons for controlling the music
play_button = ttk.Button(root, text="Play", command=play_music)
pause_button = ttk.Button(root, text="Pause", command=pause_music)
unpause_button = ttk.Button(root, text="Unpause", command=unpause_music)

play_button.pack()
pause_button.pack()
unpause_button.pack()

root.mainloop()
