import tkinter as tk

def create_components(master):
    create_rope_frame(master)
    create_human_frame(master)
    create_stone_frame(master)

def create_rope_frame(master):
    rope_frame = tk.LabelFrame(master, text="Rope Parameters", padx=10, pady=10)
    rope_frame.pack(padx=20, pady=20, fill="x")
    
    # Label for Rope Diameter
    rope_diameter_label = tk.Label(rope_frame, text="Rope Diameter (mm):")
    rope_diameter_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
    
    # Entry for Rope Diameter
    rope_diameter_entry = tk.Entry(rope_frame)
    rope_diameter_entry.grid(row=1, column=1, padx=5, pady=5)

    # Dropdown menu for Rope Material
    rope_material_label = tk.Label(rope_frame, text="Rope Material:")
    rope_material_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

    rope_material_options = ["Palm fiber", "Hemp fiber"]
    rope_material_var = tk.StringVar()
    rope_material_var.set(rope_material_options[0])  # set the default value
    rope_material_dropdown = tk.OptionMenu(rope_frame, rope_material_var, *rope_material_options)
    rope_material_dropdown.grid(row=0, column=1, padx=5, pady=5)
    
    # Label for Tensile Strength
    tensile_strength_label = tk.Label(rope_frame, text="Tensile Strength (MPa):")
    tensile_strength_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
    
    # Entry for Tensile Strength
    tensile_strength_entry = tk.Entry(rope_frame)
    tensile_strength_entry.grid(row=2, column=1, padx=5, pady=5)
    
    # Label for Density
    density_label = tk.Label(rope_frame, text="Density (g/cm³):")
    density_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
    
    # Entry for Density
    density_entry = tk.Entry(rope_frame)
    density_entry.grid(row=3, column=1, padx=5, pady=5)

    # Label for Safety Margin
    safety_margin_label = tk.Label(rope_frame, text="Safety Margin: ")
    safety_margin_label.grid(row=4, column=0, padx=5, pady=5)

    # Entry for Safety Margin
    safety_margin_entry = tk.Entry(rope_frame)
    safety_margin_entry.grid(row=4, column=1, padx=5, pady=5)


def create_human_frame(master):
    human_frame = tk.LabelFrame(master, text="Human Exertion Limitations", padx=10, pady=10)
    human_frame.pack(padx=20, pady=20, fill="x")
    
    # Label for Daily human exertion
    human_exertion_label = tk.Label(human_frame, text="Daily human exertion (hours):")
    human_exertion_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    
    # Entry for Daily human exertion
    human_exertion_entry = tk.Entry(human_frame)
    human_exertion_entry.grid(row=0, column=1, padx=5, pady=5)

def create_stone_frame(master):
    stone_frame = tk.LabelFrame(master, text="Friction & Stone Block Mass", padx=10, pady=10)
    stone_frame.pack(padx=20, pady=20, fill="x")
    
    # Label for Block mass inside the stone_frame
    block_mass_label = tk.Label(stone_frame, text="Block mass (T):")
    block_mass_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    
    # Entry for Block mass inside the stone_frame
    block_mass_entry = tk.Entry(stone_frame)
    block_mass_entry.grid(row=0, column=1, padx=5, pady=5)

    # Label for co-efficent of friction
    friction_label = tk.Label(stone_frame,text="Coefficent of Friction: ")
    friction_label.grid(row=1, column=0, padx=5, pady=5)

    #Entry for Coefficient of friction
    friction_entry = tk.Entry(stone_frame)
    friction_entry.grid(row=1, column=1, padx=5, pady=5)
