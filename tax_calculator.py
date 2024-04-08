"""
Datum: 13-03-2024
Programmeur: Floris Barendsen
Opdracht: P3.6 Eindopdracht van Joost, Floris, Lucas, Wouter en Luca
"""

import tkinter as tk
from tkinter import ttk

class TaxScreen(tk.Frame):
    """
    A class representing the TaxScreen widget.
    """

    def __init__(self, parent) -> None:
        """
        Initializes the TaxScreen class.
        :param parent: The parent widget.
        :return: None
        """

        super().__init__(parent)
        
        # Create and configure the widgets
        self.label: ttk.Label = ttk.Label(self, text="BTW Rekentool")
        self.label.pack(pady=10)
        
        self.entry: ttk.Entry = ttk.Entry(self)
        self.entry.pack(pady=5)
        
        self.button: ttk.Button = ttk.Button(self, text="Bereken", command=self.calculate_btw)
        self.button.pack(pady=5)
        
        self.result_label: ttk.Label = ttk.Label(self, text="")
        self.result_label.pack(pady=10)
        
    def calculate_btw(self) -> None:
        """
        Calculates the VAT and total amount based on the entered amount.
        :return: None
        """

        try:
            amount: float = float(self.entry.get())
            btw_amount: float = amount * 0.21
            total_amount: float = amount + btw_amount
            self.result_label.configure(text=f"BTW: {btw_amount:.2f}, Totaal: {total_amount:.2f}")
        except ValueError:
            self.result_label.configure(text="Ongeldige invoer.")

if __name__ == "__main__":
    window: TaxScreen = TaxScreen()