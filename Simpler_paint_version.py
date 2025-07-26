import tkinter as tk
from tkinter import ttk, filedialog
from PIL import ImageGrab  # Required to save canvas as image

# -------------------------------
# Main Window Setup
# -------------------------------
window = tk.Tk()
window.title("🖌️ Simpler Paint - Tkinter Drawing App")
window.geometry("1100x700")
window.config(bg="white")

# -------------------------------
# Variables
# -------------------------------
color_var = tk.StringVar(value="Black")
size_var = tk.IntVar(value=2)
tool_var = tk.StringVar(value="Freehand")  # Default tool is Freehand
start_x, start_y = None, None  # Used for freehand drawing

# -------------------------------
# UI Elements - Color & Size
# -------------------------------
top_frame = ttk.Frame(window)
top_frame.pack(pady=10)

ttk.Label(top_frame, text="🎨 Color:").grid(row=0, column=0, padx=5)
color_picker = ttk.Combobox(
    top_frame, textvariable=color_var,
    values=["Black", "Red", "Blue", "Green", "Yellow", "White"], width=10
)
color_picker.grid(row=0, column=1, padx=5)

ttk.Label(top_frame, text="✏️ Size:").grid(row=0, column=2, padx=5)
size_picker = tk.Spinbox(top_frame, from_=1, to=20, textvariable=size_var, width=5)
size_picker.grid(row=0, column=3, padx=5)

# -------------------------------
# Create Canvas
# -------------------------------
canvas = tk.Canvas(window, bg="white", width=1000, height=500, bd=2, relief="groove")
canvas.pack(pady=10)

# -------------------------------
# Drawing Tools
# -------------------------------

def set_tool(tool_name):
    """Switches between Freehand, Eraser, or Shape Tools"""
    tool_var.set(tool_name)

def on_mouse_press(event):
    """Records starting point and handles shape placement"""
    global start_x, start_y
    start_x, start_y = event.x, event.y

    if tool_var.get() == "Circle":
        r = size_var.get() * 5
        canvas.create_oval(event.x - r, event.y - r, event.x + r, event.y + r,
                           fill=color_var.get(), outline=color_var.get())

    elif tool_var.get() == "Rectangle":
        s = size_var.get() * 6
        canvas.create_rectangle(event.x, event.y, event.x + s, event.y + s,
                                fill=color_var.get(), outline=color_var.get())

    elif tool_var.get() == "Line":
        canvas.create_line(event.x, event.y, event.x + 100, event.y, fill=color_var.get(), width=size_var.get())

    elif tool_var.get() == "Text":
        canvas.create_text(event.x, event.y, text="Hello!", fill=color_var.get(), font=("Arial", 20))

def on_mouse_drag(event):
    """Handles freehand drawing and erasing"""
    if tool_var.get() in ["Freehand", "Eraser"]:
        color = "white" if tool_var.get() == "Eraser" else color_var.get()
        size = size_var.get()
        canvas.create_line(event.x, event.y, event.x + 1, event.y + 1, fill=color, width=size, capstyle=tk.ROUND)

# -------------------------------
# Save Canvas as Image
# -------------------------------
def save_canvas():
    file_path = filedialog.asksaveasfilename(defaultextension=".png",
        filetypes=[("PNG Image", "*.png")])
    if file_path:
        x = window.winfo_rootx() + canvas.winfo_x()
        y = window.winfo_rooty() + canvas.winfo_y()
        x1 = x + canvas.winfo_width()
        y1 = y + canvas.winfo_height()
        ImageGrab.grab().crop((x, y, x1, y1)).save(file_path)

# -------------------------------
# Clear Canvas
# -------------------------------
def clear_canvas():
    canvas.delete("all")

# -------------------------------
# Tool Buttons
# -------------------------------
button_frame = ttk.Frame(window)
button_frame.pack(pady=10)

tools = [
    ("✏️ Freehand", "Freehand"),
    ("🧼 Eraser", "Eraser"),
    ("⭕ Circle", "Circle"),
    ("▭ Rectangle", "Rectangle"),
    ("📏 Line", "Line"),
    ("🔤 Text", "Text"),
]

for i, (label, toolname) in enumerate(tools):
    ttk.Button(button_frame, text=label, command=lambda t=toolname: set_tool(t)).grid(row=0, column=i, padx=5)

# Save and Clear Buttons
ttk.Button(button_frame, text="💾 Save", command=save_canvas).grid(row=0, column=6, padx=10)
ttk.Button(button_frame, text="🧹 Clear", command=clear_canvas).grid(row=0, column=7, padx=10)

# -------------------------------
# Bind Mouse Events
# -------------------------------
canvas.bind("<Button-1>", on_mouse_press)
canvas.bind("<B1-Motion>", on_mouse_drag)

# -------------------------------
# Run Application
# -------------------------------
window.mainloop()
