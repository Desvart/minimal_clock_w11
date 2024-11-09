import tkinter as tk
from datetime import datetime
import keyboard
import json
import os
from pathlib import Path

class MinimalClock:
    def __init__(self):
        self.root = tk.Tk()
        self.root.overrideredirect(True)  # Remove window decorations
        self.root.attributes('-alpha', 0.8)  # Set transparency
        self.root.attributes('-topmost', True)  # Keep window on top
        
        # Set initial position (load from config if exists)
        self.config_path = Path.home() / 'minimal_clock_config.json'
        self.load_position()
        
        # Create clock label
        self.label = tk.Label(
            self.root,
            font=('Segoe UI', 10),
            bg='black',
            fg='white',
            padx=10,
            pady=5
        )
        self.label.pack()
        
        # Bind mouse events for dragging
        self.label.bind('<Button-1>', self.start_move)
        self.label.bind('<B1-Motion>', self.on_move)
        
        # Bind right-click for context menu
        self.label.bind('<Button-3>', self.show_menu)
        
        # Create context menu
        self.menu = tk.Menu(self.root, tearoff=0)
        self.menu.add_command(label="Exit", command=self.root.quit)
        
        # Register global hotkey to toggle transparency
        keyboard.on_press_key('scroll lock', self.toggle_transparency)
        
        self.transparent = False
        self.update_clock()
    
    def start_move(self, event):
        self.x = event.x
        self.y = event.y
    
    def on_move(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.root.winfo_x() + deltax
        y = self.root.winfo_y() + deltay
        self.root.geometry(f"+{x}+{y}")
        self.save_position()
    
    def show_menu(self, event):
        self.menu.post(event.x_root, event.y_root)
    
    def toggle_transparency(self, _):
        if self.transparent:
            self.root.attributes('-alpha', 0.8)
            self.transparent = False
        else:
            self.root.attributes('-alpha', 0.2)
            self.transparent = True
    
    def save_position(self):
        config = {
            'x': self.root.winfo_x(),
            'y': self.root.winfo_y()
        }
        with open(self.config_path, 'w') as f:
            json.dump(config, f)
    
    def load_position(self):
        if self.config_path.exists():
            with open(self.config_path) as f:
                config = json.load(f)
            self.root.geometry(f"+{config['x']}+{config['y']}")
        else:
            # Default position (bottom right)
            screen_width = self.root.winfo_screenwidth()
            screen_height = self.root.winfo_screenheight()
            self.root.geometry(f"+{screen_width-100}+{screen_height-50}")
    
    def update_clock(self):
        current_time = datetime.now().strftime("%H:%M")
        self.label.config(text=current_time)
        self.root.after(1000, self.update_clock)  # Update every second
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    clock = MinimalClock()
    clock.run()
