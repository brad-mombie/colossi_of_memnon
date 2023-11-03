import tkinter as tk
from ui_components import create_components

import json

def load_constants():
    with open("constants.json", "r") as file:
        constants = json.load(file)
    return constants

# Usage
constants = load_constants()
print(constants["PALM_FIBER_DENSITY"])


def main():
    root = tk.Tk()
    root.title("Colossi of Memon")
    
    create_components(root)
    
    root.mainloop()

if __name__ == "__main__":
    main()
