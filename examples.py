#!/usr/bin/env python3
"""
Example usage of the Energy Calculator
"""

from energy_calculator import EnergyCalculator

print("=" * 60)
print("KINETIC AND POTENTIAL ENERGY CALCULATOR - EXAMPLES")
print("=" * 60)

# Example 1: Kinetic Energy
print("\n1. KINETIC ENERGY EXAMPLE")
print("-" * 60)
mass = 5  # kg
velocity = 10  # m/s
ke = EnergyCalculator.kinetic_energy(mass, velocity)
print(f"   Mass: {mass} kg")
print(f"   Velocity: {velocity} m/s")
print(f"   Kinetic Energy = 0.5 × {mass} × {velocity}²")
print(f"   Kinetic Energy = {ke} J")

# Example 2: Potential Energy
print("\n2. POTENTIAL ENERGY EXAMPLE (Earth)")
print("-" * 60)
mass = 10  # kg
height = 50  # m
pe = EnergyCalculator.potential_energy(mass, height)
print(f"   Mass: {mass} kg")
print(f"   Height: {height} m")
print(f"   Gravity: 9.81 m/s² (Earth)")
print(f"   Potential Energy = {mass} × 9.81 × {height}")
print(f"   Potential Energy = {pe:.2f} J")

# Example 3: Potential Energy on Moon
print("\n3. POTENTIAL ENERGY EXAMPLE (Moon)")
print("-" * 60)
mass = 10  # kg
height = 50  # m
gravity_moon = 1.62  # m/s²
pe_moon = EnergyCalculator.potential_energy(mass, height, gravity_moon)
print(f"   Mass: {mass} kg")
print(f"   Height: {height} m")
print(f"   Gravity: {gravity_moon} m/s² (Moon)")
print(f"   Potential Energy = {mass} × {gravity_moon} × {height}")
print(f"   Potential Energy = {pe_moon:.2f} J")
print(f"   (Note: Moon has 1/6 of Earth's gravity)")

# Example 4: Total Mechanical Energy
print("\n4. TOTAL MECHANICAL ENERGY EXAMPLE")
print("-" * 60)
mass = 2  # kg
velocity = 8  # m/s
height = 10  # m
ke = EnergyCalculator.kinetic_energy(mass, velocity)
pe = EnergyCalculator.potential_energy(mass, height)
total = EnergyCalculator.total_mechanical_energy(mass, velocity, height)
print(f"   Mass: {mass} kg")
print(f"   Velocity: {velocity} m/s")
print(f"   Height: {height} m")
print(f"   ")
print(f"   Kinetic Energy = {ke} J")
print(f"   Potential Energy = {pe:.2f} J")
print(f"   Total Mechanical Energy = {total:.2f} J")

# Example 5: Falling Ball (Energy Conservation)
print("\n5. FALLING BALL - ENERGY CONSERVATION")
print("-" * 60)
mass = 1  # kg
initial_height = 20  # m

# At the top (initial state)
initial_pe = EnergyCalculator.potential_energy(mass, initial_height)
initial_ke = EnergyCalculator.kinetic_energy(mass, 0)
initial_total = initial_pe + initial_ke

print(f"   Initial State (at height {initial_height}m):")
print(f"      Potential Energy = {initial_pe:.2f} J")
print(f"      Kinetic Energy = {initial_ke:.2f} J")
print(f"      Total Energy = {initial_total:.2f} J")

# At ground level, all PE converts to KE
# v = √(2gh)
final_velocity = (2 * 9.81 * initial_height) ** 0.5
final_ke = EnergyCalculator.kinetic_energy(mass, final_velocity)
final_pe = EnergyCalculator.potential_energy(mass, 0)
final_total = final_ke + final_pe

print(f"\n   Final State (at ground level):")
print(f"      Final Velocity = {final_velocity:.2f} m/s")
print(f"      Potential Energy = {final_pe:.2f} J")
print(f"      Kinetic Energy = {final_ke:.2f} J")
print(f"      Total Energy = {final_total:.2f} J")

print(f"\n   Energy Conservation Check:")
print(f"      Initial Total = {initial_total:.2f} J")
print(f"      Final Total = {final_total:.2f} J")
print(f"      ✓ Energy is conserved (within rounding error)")

# Example 6: Moving Vehicle
print("\n6. MOVING VEHICLE EXAMPLE")
print("-" * 60)
mass = 1500  # kg (car)
velocity = 25  # m/s (about 90 km/h)
height = 100  # m (on a bridge)

ke = EnergyCalculator.kinetic_energy(mass, velocity)
pe = EnergyCalculator.potential_energy(mass, height)
total = EnergyCalculator.total_mechanical_energy(mass, velocity, height)

print(f"   Vehicle: Car (mass = {mass} kg)")
print(f"   Velocity: {velocity} m/s ({velocity * 3.6:.0f} km/h)")
print(f"   Height: {height} m")
print(f"   ")
print(f"   Kinetic Energy = {ke:,.0f} J ({ke/1000:.1f} kJ)")
print(f"   Potential Energy = {pe:,.0f} J ({pe/1000:.1f} kJ)")
print(f"   Total Mechanical Energy = {total:,.0f} J ({total/1000:.1f} kJ)")

print("\n" + "=" * 60)
print("All calculations use SI units (kg, m/s, m, J)")
print("=" * 60)
