#!/usr/bin/env python3
"""
Energy Calculator - Kinetic and Potential Energy Calculator in SI Units
"""

import sys
from typing import Union


class EnergyCalculator:
    """Calculator for kinetic and potential energy in SI units."""
    
    # Standard gravitational acceleration in SI units (m/s²)
    GRAVITY = 9.81
    
    @staticmethod
    def kinetic_energy(mass: float, velocity: float) -> float:
        """
        Calculate kinetic energy in Joules.
        
        KE = (1/2) * m * v²
        
        Args:
            mass: Mass in kilograms (kg)
            velocity: Velocity in meters per second (m/s)
            
        Returns:
            Kinetic energy in Joules (J)
            
        Raises:
            ValueError: If mass or velocity is negative
        """
        if mass < 0:
            raise ValueError("Mass cannot be negative")
        if velocity < 0:
            raise ValueError("Velocity cannot be negative")
        
        return 0.5 * mass * velocity ** 2
    
    @staticmethod
    def potential_energy(mass: float, height: float, gravity: float = GRAVITY) -> float:
        """
        Calculate gravitational potential energy in Joules.
        
        PE = m * g * h
        
        Args:
            mass: Mass in kilograms (kg)
            height: Height in meters (m)
            gravity: Gravitational acceleration in m/s² (default: 9.81 m/s²)
            
        Returns:
            Potential energy in Joules (J)
            
        Raises:
            ValueError: If mass, height, or gravity is negative
        """
        if mass < 0:
            raise ValueError("Mass cannot be negative")
        if height < 0:
            raise ValueError("Height cannot be negative")
        if gravity < 0:
            raise ValueError("Gravitational acceleration cannot be negative")
        
        return mass * gravity * height
    
    @staticmethod
    def total_mechanical_energy(
        mass: float, velocity: float, height: float, gravity: float = GRAVITY
    ) -> float:
        """
        Calculate total mechanical energy (kinetic + potential).
        
        Total Energy = KE + PE
        
        Args:
            mass: Mass in kilograms (kg)
            velocity: Velocity in meters per second (m/s)
            height: Height in meters (m)
            gravity: Gravitational acceleration in m/s² (default: 9.81 m/s²)
            
        Returns:
            Total mechanical energy in Joules (J)
        """
        ke = EnergyCalculator.kinetic_energy(mass, velocity)
        pe = EnergyCalculator.potential_energy(mass, height, gravity)
        return ke + pe


def interactive_mode():
    """Run the calculator in interactive mode."""
    print("\n" + "=" * 50)
    print("Energy Calculator - SI Units")
    print("=" * 50)
    
    while True:
        print("\nSelect calculation:")
        print("1. Kinetic Energy (KE = 0.5 * m * v²)")
        print("2. Potential Energy (PE = m * g * h)")
        print("3. Total Mechanical Energy (KE + PE)")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == "1":
            try:
                mass = float(input("Enter mass (kg): "))
                velocity = float(input("Enter velocity (m/s): "))
                ke = EnergyCalculator.kinetic_energy(mass, velocity)
                print(f"\nKinetic Energy = {ke:.2f} J")
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == "2":
            try:
                mass = float(input("Enter mass (kg): "))
                height = float(input("Enter height (m): "))
                gravity_input = input("Enter gravitational acceleration (m/s²) [default: 9.81]: ").strip()
                gravity = float(gravity_input) if gravity_input else EnergyCalculator.GRAVITY
                pe = EnergyCalculator.potential_energy(mass, height, gravity)
                print(f"\nPotential Energy = {pe:.2f} J")
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == "3":
            try:
                mass = float(input("Enter mass (kg): "))
                velocity = float(input("Enter velocity (m/s): "))
                height = float(input("Enter height (m): "))
                gravity_input = input("Enter gravitational acceleration (m/s²) [default: 9.81]: ").strip()
                gravity = float(gravity_input) if gravity_input else EnergyCalculator.GRAVITY
                
                ke = EnergyCalculator.kinetic_energy(mass, velocity)
                pe = EnergyCalculator.potential_energy(mass, height, gravity)
                total = ke + pe
                
                print(f"\nKinetic Energy = {ke:.2f} J")
                print(f"Potential Energy = {pe:.2f} J")
                print(f"Total Mechanical Energy = {total:.2f} J")
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == "4":
            print("\nGoodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")


def main():
    """Main entry point."""
    if len(sys.argv) == 1:
        interactive_mode()
    else:
        print("Command-line mode:")
        print("Usage: python energy_calculator.py")
        print("  Run without arguments to use interactive mode.")


if __name__ == "__main__":
    main()
