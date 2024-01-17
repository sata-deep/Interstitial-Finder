# Interstitial-Finder
# **Interstitials App GUI Code**

This repository contains the **GUI code for the Interstitials App**, developed in Python using the **Tkinter library**. The app is designed to facilitate the identification and analysis of interstitial defects in crystal structures. It provides a user-friendly interface to input structural data and select parameters for defect generation.

## **Features**

- **File Input**: Users can input structural data files using a simple browse function (VASP format: *.vasp, POSCAR, CONTCAR)
- **Dynamic Parameter Selection**: Depending on the chosen method (InFiT or Voronoi), relevant parameters can be adjusted (at this moment only Voronoi is supported)
- **Progress Tracking**: A progress indicator shows the status of the defect generation process.
- **Result Display**: Upon completion, the results of the defect analysis are displayed.
- **Resizable Logo**: The app includes a resizable logo for enhanced user experience.

## **GUI Components**

- **Input Fields**: For specifying the structural data file and inter-element.
- **Combobox**: For selecting the method of defect generation (InFiT or Voronoi).
- **Parameter Adjustment**: Fields to adjust parameters specific to the Voronoi method.
- **Progress Bar**: To keep track of the ongoing process.
- **Submit Button**: To start the defect generation process.
    
    ## **Dependencies**

    Tkinter
    PIL (Python Imaging Library)
    Pymatgen

    ## **Installation**
The GUI is intuitively designed for ease of use while maintaining robust functionality for defect analysis.
Ensure you have **Python** installed on your machine. Clone the repository and install the required dependencies:
```bash
pip install -r requirements.txt
To run the code:
python New.py



