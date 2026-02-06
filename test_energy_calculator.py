#!/usr/bin/env python3
"""
Unit tests for the Energy Calculator
"""

import unittest
from energy_calculator import EnergyCalculator


class TestKineticEnergy(unittest.TestCase):
    """Tests for kinetic energy calculations."""
    
    def test_kinetic_energy_basic(self):
        """Test basic kinetic energy calculation."""
        # KE = 0.5 * 2 * 3² = 0.5 * 2 * 9 = 9 J
        ke = EnergyCalculator.kinetic_energy(2, 3)
        self.assertAlmostEqual(ke, 9.0, places=2)
    
    def test_kinetic_energy_zero_velocity(self):
        """Test kinetic energy with zero velocity."""
        ke = EnergyCalculator.kinetic_energy(5, 0)
        self.assertEqual(ke, 0)
    
    def test_kinetic_energy_zero_mass(self):
        """Test kinetic energy with zero mass."""
        ke = EnergyCalculator.kinetic_energy(0, 10)
        self.assertEqual(ke, 0)
    
    def test_kinetic_energy_negative_mass(self):
        """Test kinetic energy with negative mass raises error."""
        with self.assertRaises(ValueError):
            EnergyCalculator.kinetic_energy(-1, 5)
    
    def test_kinetic_energy_negative_velocity(self):
        """Test kinetic energy with negative velocity raises error."""
        with self.assertRaises(ValueError):
            EnergyCalculator.kinetic_energy(5, -10)


class TestPotentialEnergy(unittest.TestCase):
    """Tests for potential energy calculations."""
    
    def test_potential_energy_basic(self):
        """Test basic potential energy calculation."""
        # PE = 10 * 9.81 * 2 = 196.2 J
        pe = EnergyCalculator.potential_energy(10, 2)
        self.assertAlmostEqual(pe, 196.2, places=1)
    
    def test_potential_energy_zero_height(self):
        """Test potential energy with zero height."""
        pe = EnergyCalculator.potential_energy(5, 0)
        self.assertEqual(pe, 0)
    
    def test_potential_energy_zero_mass(self):
        """Test potential energy with zero mass."""
        pe = EnergyCalculator.potential_energy(0, 10)
        self.assertEqual(pe, 0)
    
    def test_potential_energy_custom_gravity(self):
        """Test potential energy with custom gravitational acceleration."""
        # PE = 1 * 1.62 * 10 = 16.2 J (lunar gravity)
        pe = EnergyCalculator.potential_energy(1, 10, gravity=1.62)
        self.assertAlmostEqual(pe, 16.2, places=2)
    
    def test_potential_energy_negative_mass(self):
        """Test potential energy with negative mass raises error."""
        with self.assertRaises(ValueError):
            EnergyCalculator.potential_energy(-1, 5)
    
    def test_potential_energy_negative_height(self):
        """Test potential energy with negative height raises error."""
        with self.assertRaises(ValueError):
            EnergyCalculator.potential_energy(5, -10)
    
    def test_potential_energy_negative_gravity(self):
        """Test potential energy with negative gravity raises error."""
        with self.assertRaises(ValueError):
            EnergyCalculator.potential_energy(5, 10, gravity=-9.81)


class TestTotalMechanicalEnergy(unittest.TestCase):
    """Tests for total mechanical energy calculations."""
    
    def test_total_mechanical_energy(self):
        """Test total mechanical energy calculation."""
        # Mass = 2 kg, velocity = 3 m/s, height = 1 m
        # KE = 0.5 * 2 * 3² = 9 J
        # PE = 2 * 9.81 * 1 = 19.62 J
        # Total = 28.62 J
        total = EnergyCalculator.total_mechanical_energy(2, 3, 1)
        expected = 9 + (2 * 9.81 * 1)
        self.assertAlmostEqual(total, expected, places=2)
    
    def test_total_mechanical_energy_zero_velocity(self):
        """Test total mechanical energy with zero velocity (only PE)."""
        total = EnergyCalculator.total_mechanical_energy(5, 0, 3)
        expected = 5 * 9.81 * 3
        self.assertAlmostEqual(total, expected, places=2)
    
    def test_total_mechanical_energy_zero_height(self):
        """Test total mechanical energy with zero height (only KE)."""
        total = EnergyCalculator.total_mechanical_energy(4, 2, 0)
        expected = 0.5 * 4 * 2 ** 2
        self.assertAlmostEqual(total, expected, places=2)


class TestPhysicalExamples(unittest.TestCase):
    """Tests using real-world physics examples."""
    
    def test_falling_ball_example(self):
        """Test a ball falling from a height."""
        mass = 1  # kg
        initial_height = 10  # m
        
        # Initial mechanical energy (at rest at height)
        initial_pe = EnergyCalculator.potential_energy(mass, initial_height)
        initial_ke = EnergyCalculator.kinetic_energy(mass, 0)
        initial_total = initial_pe + initial_ke
        
        # Energy is conserved (ignoring air resistance)
        # At ground level: all potential energy converts to kinetic
        # PE = mgh = 1 * 9.81 * 10 = 98.1 J
        # KE at impact = 0.5 * m * v²
        # v = sqrt(2 * g * h) = sqrt(2 * 9.81 * 10) ≈ 14 m/s
        final_velocity = (2 * 9.81 * initial_height) ** 0.5
        final_ke = EnergyCalculator.kinetic_energy(mass, final_velocity)
        
        # Should be approximately equal
        self.assertAlmostEqual(initial_total, final_ke, places=1)


if __name__ == "__main__":
    unittest.main()
