#!/usr/bin/env python3
"""
Graphical User Interface for the Energy Calculator
Built with tkinter for cross-platform compatibility
"""

import tkinter as tk
from tkinter import ttk, messagebox
from energy_calculator import EnergyCalculator


class EnergyCalculatorGUI:
    """GUI for the Energy Calculator using tkinter."""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Energy Calculator - SI Units")
        self.root.geometry("600x700")
        self.root.resizable(False, False)
        
        # Set color scheme
        self.bg_color = "#f0f0f0"
        self.accent_color = "#2196F3"
        self.root.configure(bg=self.bg_color)
        
        # Create main notebook (tabbed interface)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Create tabs
        self.create_kinetic_tab()
        self.create_potential_tab()
        self.create_total_tab()
        self.create_info_tab()
    
    def create_kinetic_tab(self):
        """Create Kinetic Energy calculation tab."""
        frame = ttk.Frame(self.notebook, padding="20")
        self.notebook.add(frame, text="Kinetic Energy")
        
        # Title
        title = ttk.Label(frame, text="Kinetic Energy Calculator", 
                         font=("Arial", 14, "bold"))
        title.pack(pady=(0, 20))
        
        # Formula
        formula = ttk.Label(frame, text="KE = ½ × m × v²", 
                           font=("Arial", 12), foreground="gray")
        formula.pack(pady=(0, 15))
        
        # Mass input
        ttk.Label(frame, text="Mass (kg):", font=("Arial", 11)).pack(anchor=tk.W, pady=(10, 5))
        self.ke_mass = ttk.Entry(frame, width=30)
        self.ke_mass.pack(fill=tk.X, pady=(0, 15))
        self.ke_mass.insert(0, "5")
        
        # Velocity input
        ttk.Label(frame, text="Velocity (m/s):", font=("Arial", 11)).pack(anchor=tk.W, pady=(10, 5))
        self.ke_velocity = ttk.Entry(frame, width=30)
        self.ke_velocity.pack(fill=tk.X, pady=(0, 20))
        self.ke_velocity.insert(0, "10")
        
        # Calculate button
        btn = ttk.Button(frame, text="Calculate Kinetic Energy", 
                        command=self.calculate_kinetic)
        btn.pack(fill=tk.X, pady=10)
        
        # Result frame
        result_frame = ttk.LabelFrame(frame, text="Result", padding="15")
        result_frame.pack(fill=tk.X, pady=(20, 0))
        
        self.ke_result = tk.Text(result_frame, height=4, width=50, 
                                font=("Courier", 11), state=tk.DISABLED)
        self.ke_result.pack(fill=tk.BOTH, expand=True)
    
    def create_potential_tab(self):
        """Create Potential Energy calculation tab."""
        frame = ttk.Frame(self.notebook, padding="20")
        self.notebook.add(frame, text="Potential Energy")
        
        # Title
        title = ttk.Label(frame, text="Potential Energy Calculator", 
                         font=("Arial", 14, "bold"))
        title.pack(pady=(0, 20))
        
        # Formula
        formula = ttk.Label(frame, text="PE = m × g × h", 
                           font=("Arial", 12), foreground="gray")
        formula.pack(pady=(0, 15))
        
        # Mass input
        ttk.Label(frame, text="Mass (kg):", font=("Arial", 11)).pack(anchor=tk.W, pady=(10, 5))
        self.pe_mass = ttk.Entry(frame, width=30)
        self.pe_mass.pack(fill=tk.X, pady=(0, 15))
        self.pe_mass.insert(0, "10")
        
        # Height input
        ttk.Label(frame, text="Height (m):", font=("Arial", 11)).pack(anchor=tk.W, pady=(10, 5))
        self.pe_height = ttk.Entry(frame, width=30)
        self.pe_height.pack(fill=tk.X, pady=(0, 15))
        self.pe_height.insert(0, "20")
        
        # Gravity input
        ttk.Label(frame, text="Gravity (m/s²):", font=("Arial", 11)).pack(anchor=tk.W, pady=(10, 5))
        gravity_frame = ttk.Frame(frame)
        gravity_frame.pack(fill=tk.X, pady=(0, 15))
        
        self.pe_gravity = ttk.Entry(gravity_frame, width=20)
        self.pe_gravity.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.pe_gravity.insert(0, "9.81")
        
        # Quick gravity buttons
        ttk.Button(gravity_frame, text="Earth", width=8,
                  command=lambda: self.pe_gravity.delete(0, tk.END) or self.pe_gravity.insert(0, "9.81")).pack(side=tk.LEFT, padx=(5, 2))
        ttk.Button(gravity_frame, text="Moon", width=8,
                  command=lambda: self.pe_gravity.delete(0, tk.END) or self.pe_gravity.insert(0, "1.62")).pack(side=tk.LEFT, padx=2)
        ttk.Button(gravity_frame, text="Mars", width=8,
                  command=lambda: self.pe_gravity.delete(0, tk.END) or self.pe_gravity.insert(0, "3.71")).pack(side=tk.LEFT, padx=2)
        
        # Calculate button
        btn = ttk.Button(frame, text="Calculate Potential Energy", 
                        command=self.calculate_potential)
        btn.pack(fill=tk.X, pady=10)
        
        # Result frame
        result_frame = ttk.LabelFrame(frame, text="Result", padding="15")
        result_frame.pack(fill=tk.X, pady=(20, 0))
        
        self.pe_result = tk.Text(result_frame, height=4, width=50, 
                                font=("Courier", 11), state=tk.DISABLED)
        self.pe_result.pack(fill=tk.BOTH, expand=True)
    
    def create_total_tab(self):
        """Create Total Mechanical Energy calculation tab."""
        frame = ttk.Frame(self.notebook, padding="20")
        self.notebook.add(frame, text="Total Energy")
        
        # Title
        title = ttk.Label(frame, text="Total Mechanical Energy", 
                         font=("Arial", 14, "bold"))
        title.pack(pady=(0, 20))
        
        # Formula
        formula = ttk.Label(frame, text="E_total = KE + PE", 
                           font=("Arial", 12), foreground="gray")
        formula.pack(pady=(0, 15))
        
        # Mass input
        ttk.Label(frame, text="Mass (kg):", font=("Arial", 11)).pack(anchor=tk.W, pady=(10, 5))
        self.total_mass = ttk.Entry(frame, width=30)
        self.total_mass.pack(fill=tk.X, pady=(0, 15))
        self.total_mass.insert(0, "2")
        
        # Velocity input
        ttk.Label(frame, text="Velocity (m/s):", font=("Arial", 11)).pack(anchor=tk.W, pady=(10, 5))
        self.total_velocity = ttk.Entry(frame, width=30)
        self.total_velocity.pack(fill=tk.X, pady=(0, 15))
        self.total_velocity.insert(0, "8")
        
        # Height input
        ttk.Label(frame, text="Height (m):", font=("Arial", 11)).pack(anchor=tk.W, pady=(10, 5))
        self.total_height = ttk.Entry(frame, width=30)
        self.total_height.pack(fill=tk.X, pady=(0, 15))
        self.total_height.insert(0, "10")
        
        # Gravity input
        ttk.Label(frame, text="Gravity (m/s²):", font=("Arial", 11)).pack(anchor=tk.W, pady=(10, 5))
        gravity_frame = ttk.Frame(frame)
        gravity_frame.pack(fill=tk.X, pady=(0, 15))
        
        self.total_gravity = ttk.Entry(gravity_frame, width=20)
        self.total_gravity.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.total_gravity.insert(0, "9.81")
        
        # Quick gravity buttons
        ttk.Button(gravity_frame, text="Earth", width=8,
                  command=lambda: self.total_gravity.delete(0, tk.END) or self.total_gravity.insert(0, "9.81")).pack(side=tk.LEFT, padx=(5, 2))
        ttk.Button(gravity_frame, text="Moon", width=8,
                  command=lambda: self.total_gravity.delete(0, tk.END) or self.total_gravity.insert(0, "1.62")).pack(side=tk.LEFT, padx=2)
        ttk.Button(gravity_frame, text="Mars", width=8,
                  command=lambda: self.total_gravity.delete(0, tk.END) or self.total_gravity.insert(0, "3.71")).pack(side=tk.LEFT, padx=2)
        
        # Calculate button
        btn = ttk.Button(frame, text="Calculate Total Energy", 
                        command=self.calculate_total)
        btn.pack(fill=tk.X, pady=10)
        
        # Result frame
        result_frame = ttk.LabelFrame(frame, text="Result", padding="15")
        result_frame.pack(fill=tk.X, pady=(20, 0))
        
        self.total_result = tk.Text(result_frame, height=6, width=50, 
                                   font=("Courier", 11), state=tk.DISABLED)
        self.total_result.pack(fill=tk.BOTH, expand=True)
    
    def create_info_tab(self):
        """Create Information tab."""
        frame = ttk.Frame(self.notebook, padding="20")
        self.notebook.add(frame, text="Info")
        
        # Create scrollable text
        text_frame = ttk.Frame(frame)
        text_frame.pack(fill=tk.BOTH, expand=True)
        
        scrollbar = ttk.Scrollbar(text_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        info_text = tk.Text(text_frame, height=30, width=60, 
                           font=("Courier", 10), yscrollcommand=scrollbar.set)
        info_text.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=info_text.yview)
        
        info_content = """ENERGY CALCULATOR - SI UNITS
================================

FORMULAS:
--------
Kinetic Energy:     KE = ½ × m × v²
Potential Energy:   PE = m × g × h
Total Energy:       E_total = KE + PE

UNITS:
------
Mass (m):           kilograms (kg)
Velocity (v):       meters per second (m/s)
Height (h):         meters (m)
Gravity (g):        meters per second² (m/s²)
Energy:             joules (J)

GRAVITY CONSTANTS:
-----------------
Earth:              9.81 m/s²
Moon:               1.62 m/s²
Mars:               3.71 m/s²
Jupiter:            24.79 m/s²

EXAMPLES:
--------
1. A 5 kg object moving at 10 m/s
   KE = ½ × 5 × 10² = 250 J

2. A 10 kg object at 20 m height
   PE = 10 × 9.81 × 20 = 1,962 J

3. A 2 kg object moving at 8 m/s at 10 m height
   KE = ½ × 2 × 8² = 64 J
   PE = 2 × 9.81 × 10 = 196.2 J
   Total = 64 + 196.2 = 260.2 J

ENERGY CONSERVATION:
-------------------
When an object falls, potential energy
converts to kinetic energy. The total
mechanical energy remains constant (if
we ignore air resistance).

Example: 1 kg ball dropped from 20 m
Initial: PE = 196.2 J, KE = 0 J
Final:   PE = 0 J, KE = 196.2 J
Total energy is conserved!
"""
        
        info_text.insert(tk.END, info_content)
        info_text.config(state=tk.DISABLED)
    
    def calculate_kinetic(self):
        """Calculate and display kinetic energy."""
        try:
            mass = float(self.ke_mass.get())
            velocity = float(self.ke_velocity.get())
            
            result = EnergyCalculator.kinetic_energy(mass, velocity)
            
            # Display result
            self.ke_result.config(state=tk.NORMAL)
            self.ke_result.delete(1.0, tk.END)
            self.ke_result.insert(tk.END, 
                f"Mass: {mass} kg\n"
                f"Velocity: {velocity} m/s\n"
                f"\nKinetic Energy = {result:.2f} J\n"
                f"                = {result/1000:.3f} kJ"
            )
            self.ke_result.config(state=tk.DISABLED)
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers for mass and velocity.")
    
    def calculate_potential(self):
        """Calculate and display potential energy."""
        try:
            mass = float(self.pe_mass.get())
            height = float(self.pe_height.get())
            gravity = float(self.pe_gravity.get())
            
            result = EnergyCalculator.potential_energy(mass, height, gravity)
            
            # Display result
            self.pe_result.config(state=tk.NORMAL)
            self.pe_result.delete(1.0, tk.END)
            self.pe_result.insert(tk.END, 
                f"Mass: {mass} kg\n"
                f"Height: {height} m\n"
                f"Gravity: {gravity} m/s²\n"
                f"\nPotential Energy = {result:.2f} J\n"
                f"                 = {result/1000:.3f} kJ"
            )
            self.pe_result.config(state=tk.DISABLED)
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers for all fields.")
    
    def calculate_total(self):
        """Calculate and display total mechanical energy."""
        try:
            mass = float(self.total_mass.get())
            velocity = float(self.total_velocity.get())
            height = float(self.total_height.get())
            gravity = float(self.total_gravity.get())
            
            ke = EnergyCalculator.kinetic_energy(mass, velocity)
            pe = EnergyCalculator.potential_energy(mass, height, gravity)
            total = ke + pe
            
            # Display result
            self.total_result.config(state=tk.NORMAL)
            self.total_result.delete(1.0, tk.END)
            self.total_result.insert(tk.END, 
                f"Mass: {mass} kg\n"
                f"Velocity: {velocity} m/s\n"
                f"Height: {height} m\n"
                f"Gravity: {gravity} m/s²\n\n"
                f"Kinetic Energy  = {ke:.2f} J ({ke/1000:.3f} kJ)\n"
                f"Potential Energy = {pe:.2f} J ({pe/1000:.3f} kJ)\n"
                f"\nTotal Mechanical Energy = {total:.2f} J ({total/1000:.3f} kJ)"
            )
            self.total_result.config(state=tk.DISABLED)
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers for all fields.")


def main():
    """Main entry point for GUI application."""
    root = tk.Tk()
    gui = EnergyCalculatorGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
