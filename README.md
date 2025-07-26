# 🖌️ Simpler Paint - Tkinter Drawing App
Simpler Paint is a lightweight desktop drawing application built using Python’s Tkinter library. It mimics the basic functionality of Microsoft Paint and is ideal for learning GUI development and event handling in Python. This project allows users to draw freely, use different tools like shapes and erasers, and even save their creations as image files.

## Features
-Freehand Drawing — Click and drag your mouse to draw.<br>
-Eraser Tool — Erase parts of your drawing with adjustable thickness.<br>
-Shape Tools — Quickly draw: Circles, Rectangles, Straight lines <br>
-Text Tool — Place predefined text (“Hello!”) on the canvas.<br>
-Save Canvas — Export your drawing as a .png image.<br>
-Clear Canvas — Instantly remove all drawings to start fresh.<br>

## Customizable Options:
-Select stroke color (e.g., Black, Red, Green, etc.)<br>
-Set brush size using a spinbox.<br>
-Decide where to draw shapes <br>

## Tech Stack
-Tool	Purpose <br>
-Tkinter	GUI framework for Python<br>
-Pillow	To grab and save the canvas as image<br>
-ttk	For themed widgets like buttons and labels<br>
-ImageGrab	Captures and crops canvas region for saving<br>

## Preview
<img width="1101" height="689" alt="image" src="https://github.com/user-attachments/assets/ba990681-fdd2-4354-b253-8b1f7bd5797f" />



## How to Run
1. Clone the repository: `git clone https://github.com/yourusername/simpler-paint.git`<br>
2. Install dependencies: Only one external library is needed: `pip install pillow` <br>
tkinter comes pre-installed with most Python distributions. If not, install via: <br>
-`sudo apt-get install python3-tk`     # For Linux  <br>
- `brew install python-tk`               # For Mac  <br>
3. Run the Application `python simpler_paint.py`

## Code Highlights
Canvas-based Drawing: Uses tk.Canvas for all visual elements.<br>
Tool Switching Logic: tool_var variable controls which drawing behavior is active.<br>
Event Binding: Handles user interaction through mouse events like <Button-1> and <B1-Motion>.<br>
Save as PNG: Uses ImageGrab to capture and crop canvas for saving.<br>

## Ideal For
Beginners exploring GUI development with Python<br>
Learning event-driven programming<br>
Creating fun mini-projects to build your portfolio<br>
Understanding canvas manipulation and saving user drawings<br>

## File Structure
Simpler_Ms_paint_with_Python_Thinkter/ <br>
│
├── simpler_paint.py     # Main Python GUI application <br>
└── README.md            # Project documentation <br>
 
## Future Ideas (Optional Additions)
1. Color picker widget<br>
2. Custom text input feature<br>
3. Shape resizing or drag handles<br>
4. Undo/Redo functionality<br>
5. Layer-based drawing<br>

## Author
Rida Fatima – Computational Finance Student | Python & Fintech Enthusiast
🔗 LinkedIn: https://www.linkedin.com/in/rida-fatima-ned
