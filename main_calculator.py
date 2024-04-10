"""
Datum: 06-03-2024
Programmeur: Joost van Assenbergh
Opdracht: P3.6 Eindopdracht van Joost, Floris, Lucas, Wouter en Luca
"""

import distance_calculator as distance
import tax_calculator as tax
import circle_calculator as circle
import square_calculator as square
import pythagoras_calculator as pythagoras

import tkinter as tk
from tkinter import ttk

# Start the main event loop
class CalculatorApp:
    """
    A class representing the CalculatorApp.
    """

    def __init__(self) -> None:
        """
        Initializes the CalculatorApp class.
        :return: None
        """

        self.window: tk.Tk = tk.Tk()  # Define the "window" variable
        self.window.title("Rekentool")
        self.window.geometry("300x200")

        # Create a notebook widget to hold the screens
        self.notebook: ttk.Notebook = ttk.Notebook(self.window)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Create the screens
        self.distance_screen: distance.DistanceScreen = distance.DistanceScreen(self.notebook)
        self.tax_screen: tax.TaxScreen = tax.TaxScreen(self.notebook)
        self.circle_screen: circle.CircleScreen = circle.CircleScreen(self.notebook)
        self.square_screen: square.SquareScreen = square.SquareScreen(self.notebook)
        self.pythagoras_screen: pythagoras.PythagorasScreen = pythagoras.PythagorasScreen(self.notebook)

        # Add the screens to the notebook
        self.notebook.add(self.distance_screen, text="Afstand")
        self.notebook.add(self.tax_screen, text="BTW")
        self.notebook.add(self.circle_screen, text="Cirkel")
        self.notebook.add(self.square_screen, text="Vierkant")
        self.notebook.add(self.pythagoras_screen, text="Pythagoras")

    def run(self) -> None:
        """
        Run the CalculatorApp.
        :return: None
        """
        
        # Start the main event loop
        self.window.mainloop()

# Main entry point of the program
def main() -> None:
    window: CalculatorApp = CalculatorApp()
    window.run()

# Run the main function
if __name__ == "__main__":
    main()