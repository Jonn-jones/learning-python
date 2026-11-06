import tkinter as tk
import itertools

# Create window
root = tk.Tk()
root.title("Shiny Love Sign")
root.configure(bg="black")
root.geometry("800x400")

# Colors for glow effect
colors = [

    "#ff0000",
    "#ff1493",
    "#ff69b4",
    "#ff4500",
    "#ff00ff",
    "#ff6347"
]

color_cycle = itertools.cycle(colors)

# Label
love_label = tk.Label(
    root,
    text="❤️ LOVE ❤️",
    font=("Arial", 50, "bold"),
    bg="black",
    fg="red"
)
love_label.pack(expand=True)

# Animation
def shine():
    color = next(color_cycle)

    love_label.config(
        fg=color
    )

    # Simulate glow by changing border/highlight
    love_label.config(
        highlightthickness=10,
        highlightbackground=color
    )

    root.after(200, shine)

shine()

root.mainloop()