# Interstitial-Finder
This repository contains the GUI code for the Interstitials App, developed in Python using the Tkinter library. The app is designed to facilitate the identification and analysis of interstitial defects in crystal structures. It provides a user-friendly interface to input structural data and select parameters for defect generation.
Features

    File Input: Users can input structural data files using a simple browse function (should be in VASP format: *.vasp, POSCAR, CONTCAR)
    Dynamic Parameter Selection: Depending on the chosen method (InFiT or Voronoi), relevant parameters can be adjusted. Please note at this moment only Voronoi is implemented.
    Progress Tracking: A progress indicator shows the status of the defect generation process.
    Result Display: Upon completion, the results of the defect analysis are displayed.
    Resizable Logo: The app includes a resizable logo for enhanced user experience.
    
    Dependencies

    Tkinter
    PIL (Python Imaging Library)
    Pymatgen

    ## **Installation**

Ensure you have **Python** installed on your machine. Clone the repository and install the required dependencies:
```bash
pip install -r requirements.txt
