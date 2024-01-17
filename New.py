# GUI Code for the Interstitials App
import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
import time

##     Satadeep Bhattacharjee ##
##          IKST Bangalore    ##
###   ================================================= #

class InterstitialsApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("I-finder-Satadeep")
        self.geometry("800x600")
        # Labels and Input fields
        ttk.Label(self, text="Input Structure File:").grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        self.input_structure_var = tk.StringVar()
        self.file_entry = ttk.Entry(self, textvariable=self.input_structure_var, width=30)
        self.file_entry.grid(row=0, column=1, padx=10, pady=5)
        self.browse_btn = ttk.Button(self, text="Browse", command=self.browse_file)
        self.browse_btn.grid(row=0, column=2, padx=10, pady=5)
        
#        self.logo_image = tk.PhotoImage(file="./image/logo.png")
        image = Image.open("./image/logo.png")
        width, height = image.size
        image = image.resize((int(width/2), int(height/2)), Image.Resampling.LANCZOS)
        self.logo_image = ImageTk.PhotoImage(image)

        logo_label = ttk.Label(self, image=self.logo_image)
        logo_label.grid(row=0, column=3, rowspan=2)

        
        ttk.Label(self, text="Inter-element:").grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        self.inter_element_var = tk.StringVar()
        self.inter_element_entry = ttk.Entry(self, textvariable=self.inter_element_var)
        self.inter_element_entry.grid(row=1, column=1, padx=10, pady=5)
        
        ttk.Label(self, text="Method:").grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
        self.method_var = tk.StringVar()
        self.method_combobox = ttk.Combobox(self, textvariable=self.method_var, values=["InFiT", "Voronoi"], state="readonly")
        self.method_combobox.grid(row=2, column=1, padx=10, pady=5)
        self.method_combobox.bind("<<ComboboxSelected>>", self.toggle_voronoi_inputs)
        
        # Voronoi method parameters
        self.voronoi_params_frame = ttk.LabelFrame(self, text="Voronoi Parameters", padding=(10, 5))
        self.voronoi_params_frame.grid(row=3, column=0, columnspan=3, padx=10, pady=5, sticky=tk.W+tk.E)
        
        self.voronoi_params_vars = {
            "clustering_tol": tk.DoubleVar(value=0.05),
            "min_dist": tk.DoubleVar(value=0.1),
            "ltol": tk.DoubleVar(value=0.1),
            "stol": tk.DoubleVar(value=0.1),
            "angle_tol": tk.DoubleVar(value=1)
        }
        for i, (param, var) in enumerate(self.voronoi_params_vars.items()):
            ttk.Label(self.voronoi_params_frame, text=f"{param}:").grid(row=i, column=0, padx=10, pady=5, sticky=tk.W)
            ttk.Entry(self.voronoi_params_frame, textvariable=var).grid(row=i, column=1, padx=10, pady=5)
        
        # Progress Text Box
        self.progress_var = tk.StringVar()
        self.progress_entry = ttk.Entry(self, textvariable=self.progress_var, state="readonly", width=30)
        self.progress_entry.grid(row=4, column=0, columnspan=3, padx=10, pady=5)
        
        # Submit Button
        self.submit_btn = ttk.Button(self, text="Submit", command=self.submit)
        self.submit_btn.grid(row=5, column=0, columnspan=3, pady=20)

        self.Label_frame = ttk.LabelFrame(self, text="Credits", padding=(10, 5))
        ttk.Label(self, text="Written by Satadeep Bhattacharjee", font=("Arial", 16, "bold")).grid(row=6, column=1, columnspan=2)  # Adjust as necessary
        ttk.Label(self, text="Version 1", font=("Arial", 16)).grid(row=7, column=0, columnspan=2)  # Adjust as necessary

        # Initially disable Voronoi parameters
        self.toggle_voronoi_inputs()

    def toggle_voronoi_inputs(self, event=None):
        "Enable or Disable Voronoi parameters based on method selection"
        if self.method_var.get() == "Voronoi":
            for widget in self.voronoi_params_frame.winfo_children():
                widget["state"] = "normal"
        else:
            for widget in self.voronoi_params_frame.winfo_children():
                widget["state"] = "disabled"

    def browse_file(self):
        "Open file dialog and set the selected file path to input_structure_var"
        file_path = filedialog.askopenfilename()
        self.input_structure_var.set(file_path)

    def submit(self):
        "Handle submission and print values (for now)"
        self.progress_var.set("Processing...")
        self.update_idletasks()  # Update the GUI
        time.sleep(2)  # Simulate some processing time
        self.process_and_display_results()
        self.progress_var.set("Job done")

    def process_and_display_results(self):
        method_num = 1 if self.method_var.get() == "InFiT" else 2
        
        voronoi_params = {
            "clustering_tol": self.voronoi_params_vars["clustering_tol"].get(),
            "min_dist": self.voronoi_params_vars["min_dist"].get(),
            "ltol": self.voronoi_params_vars["ltol"].get(),
            "stol": self.voronoi_params_vars["stol"].get(),
            "angle_tol": self.voronoi_params_vars["angle_tol"].get()
        }
        results = generate_defects(self.input_structure_var.get(), self.inter_element_var.get(), method_num, **voronoi_params)
        print(results)



def generate_defects(input_file, inter_elem, method_num, clustering_tol=0.05, min_dist=0.1, ltol=0.1, stol=0.1, angle_tol=1):
    from ast import Str
    import os, sys, subprocess
    from pymatgen.core import Structure
    from pymatgen.core.periodic_table import Element
    from pymatgen.analysis.defects.generators import (
        DefectGenerator,
        InterstitialGenerator,
        VoronoiInterstitialGenerator,
    )
    input_structure = Structure.from_file(input_file)
    try:
        inter_element = Element(inter_elem)
    except ValueError:
        print("Invalid element! ", inter_elem)
        sys.exit()
    if int(method_num) == 1:
        method_name = "InFiT"
    else:
        method_name = "Voronoi"
    if int(method_num) == 1:
        defects_generator = InterstitialGenerator(min_dist=0.5) 
    elif int(method_num) == 2:
        defects_generator = VoronoiInterstitialGenerator(clustering_tol=clustering_tol, min_dist=min_dist, ltol=ltol, stol=stol, angle_tol=angle_tol)
    defects = defects_generator.generate(input_structure, {str(inter_element)})
    out_dir = "./" 
    import numpy as np
    def convert_to_diagonal_matrix(scell_size_1d):
        return np.diag(scell_size_1d)

    scell = '1 1 1'
    scell_size = [int(x) for x in scell.split()]
    scell_size_matrix = convert_to_diagonal_matrix(scell_size)

    for i, x in enumerate(defects):
        defect_structure = x.get_supercell_structure(scell_size_matrix)  # Adjusted this line
        defect_structure.to(
        fmt="POSCAR",
        filename=f"{out_dir}/{method_name}_defect_{i + 1}.vasp"
    )
 
def main():    
    app = InterstitialsApp()
    app.mainloop()
if __name__ == '__main__':
    main()
