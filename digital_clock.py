"""
Digital Clock with Multiple Time Zones
Displays current time in different time zones with a clean, modern UI.
"""

import tkinter as tk
from tkinter import font
from datetime import datetime
import pytz

class DigitalClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Clock - Multiple Time Zones")
        self.root.geometry("900x600")
        self.root.configure(bg="#1a1a1a")
        
        # Define time zones to display
        self.time_zones = [
            ("New York", "America/New_York"),
            ("London", "Europe/London"),
            ("Tokyo", "Asia/Tokyo"),
            ("Sydney", "Australia/Sydney"),
            ("Dubai", "Asia/Dubai"),
            ("Singapore", "Asia/Singapore"),
            ("Los Angeles", "America/Los_Angeles"),
            ("Mumbai", "Asia/Kolkata"),
        ]
        
        # Create main frame
        self.main_frame = tk.Frame(root, bg="#1a1a1a")
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Title
        title_font = font.Font(family="Helvetica", size=24, weight="bold")
        title_label = tk.Label(
            self.main_frame,
            text="⏰ World Time Zones",
            font=title_font,
            bg="#1a1a1a",
            fg="#00ff88"
        )
        title_label.pack(pady=(0, 20))
        
        # Create clock displays
        self.clock_frames = {}
        self.time_labels = {}
        self.date_labels = {}
        
        # Create a grid layout for clocks
        grid_frame = tk.Frame(self.main_frame, bg="#1a1a1a")
        grid_frame.pack(fill=tk.BOTH, expand=True)
        
        for idx, (city, tz) in enumerate(self.time_zones):
            row = idx // 4
            col = idx % 4
            
            # Clock container
            clock_frame = tk.Frame(
                grid_frame,
                bg="#2d2d2d",
                relief=tk.RAISED,
                bd=2,
                highlightbackground="#00ff88",
                highlightthickness=1
            )
            clock_frame.grid(row=row, column=col, padx=10, pady=10, sticky="nsew", ipadx=10, ipady=10)
            
            # Configure grid weights
            grid_frame.grid_rowconfigure(row, weight=1)
            grid_frame.grid_columnconfigure(col, weight=1)
            
            # City name
            city_font = font.Font(family="Helvetica", size=12, weight="bold")
            city_label = tk.Label(
                clock_frame,
                text=city,
                font=city_font,
                bg="#2d2d2d",
                fg="#00ff88"
            )
            city_label.pack(pady=(0, 10))
            
            # Time display
            time_font = font.Font(family="Courier", size=28, weight="bold")
            time_label = tk.Label(
                clock_frame,
                text="00:00:00",
                font=time_font,
                bg="#2d2d2d",
                fg="#00ffff"
            )
            time_label.pack()
            
            # Date display
            date_font = font.Font(family="Helvetica", size=10)
            date_label = tk.Label(
                clock_frame,
                text="Jan 01, 2024",
                font=date_font,
                bg="#2d2d2d",
                fg="#aaaaaa"
            )
            date_label.pack(pady=(5, 0))
            
            # Store references
            self.clock_frames[tz] = clock_frame
            self.time_labels[tz] = time_label
            self.date_labels[tz] = date_label
        
        # Create control panel
        control_frame = tk.Frame(self.main_frame, bg="#1a1a1a")
        control_frame.pack(fill=tk.X, pady=(20, 0))
        
        # 12/24 hour toggle
        self.hour_format = tk.StringVar(value="24")
        format_font = font.Font(family="Helvetica", size=10)
        
        format_label = tk.Label(
            control_frame,
            text="Time Format:",
            font=format_font,
            bg="#1a1a1a",
            fg="#ffffff"
        )
        format_label.pack(side=tk.LEFT, padx=(0, 10))
        
        radio_24 = tk.Radiobutton(
            control_frame,
            text="24-Hour",
            variable=self.hour_format,
            value="24",
            bg="#1a1a1a",
            fg="#ffffff",
            selectcolor="#00ff88"
        )
        radio_24.pack(side=tk.LEFT, padx=5)
        
        radio_12 = tk.Radiobutton(
            control_frame,
            text="12-Hour",
            variable=self.hour_format,
            value="12",
            bg="#1a1a1a",
            fg="#ffffff",
            selectcolor="#00ff88"
        )
        radio_12.pack(side=tk.LEFT, padx=5)
        
        # Start the clock update
        self.update_clock()
    
    def update_clock(self):
        """Update all clock displays"""
        for city, tz_name in self.time_zones:
            tz = pytz.timezone(tz_name)
            current_time = datetime.now(tz)
            
            # Format time based on user selection
            if self.hour_format.get() == "24":
                time_str = current_time.strftime("%H:%M:%S")
            else:
                time_str = current_time.strftime("%I:%M:%S %p")
            
            # Format date
            date_str = current_time.strftime("%b %d, %Y")
            
            # Update labels
            self.time_labels[tz_name].config(text=time_str)
            self.date_labels[tz_name].config(text=date_str)
            
            # Change color based on time of day (optional visual feedback)
            hour = current_time.hour
            if 6 <= hour < 12:
                color = "#ffff00"  # Morning - yellow
            elif 12 <= hour < 18:
                color = "#ff9900"  # Afternoon - orange
            elif 18 <= hour < 21:
                color = "#ff6666"  # Evening - red
            else:
                color = "#00ffff"  # Night - cyan
            
            self.time_labels[tz_name].config(fg=color)
        
        # Schedule next update (every 1000ms = 1 second)
        self.root.after(1000, self.update_clock)

def main():
    root = tk.Tk()
    app = DigitalClockApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
