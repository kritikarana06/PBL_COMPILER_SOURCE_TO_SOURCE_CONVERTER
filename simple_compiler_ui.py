import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox
import subprocess
import os

class SimpleCompilerUI:
    def __init__(self, root):
        self.root = root
        self.root.title("C2Py Compiler")
        self.root.geometry("800x400")

        # Main frame to split the window into two sides
        self.main_frame = tk.Frame(root)
        self.main_frame.pack(fill="both", expand=True, padx=5, pady=5)

        # Left side: C Code
        self.c_frame = tk.Frame(self.main_frame)
        self.c_frame.pack(side="left", fill="both", expand=True, padx=5)

        self.c_label = tk.Label(self.c_frame, text="C Code")
        self.c_label.pack(anchor="w")

        self.c_text = scrolledtext.ScrolledText(self.c_frame, height=15, wrap=tk.WORD)
        self.c_text.pack(fill="both", expand=True)

        # Buttons below C code
        self.button_frame = tk.Frame(self.c_frame)
        self.button_frame.pack(fill="x", pady=5)

        self.load_button = tk.Button(self.button_frame, text="Load C File", command=self.load_c_file)
        self.load_button.pack(side="left", padx=5)

        # Right side: Python Code
        self.py_frame = tk.Frame(self.main_frame)
        self.py_frame.pack(side="right", fill="both", expand=True, padx=5)

        self.py_label = tk.Label(self.py_frame, text="Python Code")
        self.py_label.pack(anchor="w")

        self.py_text = scrolledtext.ScrolledText(self.py_frame, height=15, wrap=tk.WORD)
        self.py_text.pack(fill="both", expand=True)

        # Save Button
        self.save_button = tk.Button(self.py_frame, text="Save Python Code", command=self.save_py_file)
        self.save_button.pack(pady=5)

        # Compile button at the bottom
        self.compile_button = tk.Button(root, text="Compile", command=self.compile_c_code)
        self.compile_button.pack(pady=5)

    def load_c_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("C Files", "*.c")])
        if file_path:
            with open(file_path, "r") as f:
                self.c_text.delete(1.0, tk.END)
                self.c_text.insert(tk.END, f.read())

    def compile_c_code(self):
        self.py_text.delete(1.0, tk.END)
        c_code = self.c_text.get(1.0, tk.END).strip()

        if not c_code:
            self.py_text.insert(tk.END, "Error: No C code to compile!")
            return

        # Save to temp.c
        with open("temp.c", "w") as f:
            f.write(c_code)

        try:
            # Call the external parser silently
            result = subprocess.run(["./parser", "temp.c"], capture_output=True, text=True)

            # Handle errors
          
            if os.path.exists("out.py"):
                with open("out.py", "r") as f:
                    py_code = f.read()
                    self.py_text.insert(tk.END, py_code)
            else:
                self.py_text.insert(tk.END, "Error: out.py not generated.")
        except FileNotFoundError:
            self.py_text.insert(tk.END, "Error: Compiler (./parser) not found.")
        finally:
            # Optional cleanup
            if os.path.exists("temp.c"):
                os.remove("temp.c")

    def save_py_file(self):
        py_code = self.py_text.get(1.0, tk.END).strip()
        if not py_code:
            messagebox.showwarning("Save Error", "No Python code to save.")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".py", filetypes=[("Python Files", "*.py")])
        if file_path:
            with open(file_path, "w") as f:
                f.write(py_code)
            messagebox.showinfo("Success", f"Python code saved to:\n{file_path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleCompilerUI(root)
    root.mainloop()
