# Kinetic and Potential Energy Calculator

A Python-based and web-based calculator for computing kinetic and potential energy in SI units.

## Features

- **Kinetic Energy**: Calculates KE = ½mv² (in Joules)
- **Potential Energy**: Calculates PE = mgh (in Joules, with standard g = 9.81 m/s²)
- **Total Mechanical Energy**: Combines kinetic and potential energy
- **Custom Gravity**: Support for different gravitational accelerations (e.g., lunar gravity)
- **Input Validation**: Prevents invalid negative values
- **Multiple Interfaces**: 
  - 🌐 **Web Interface** (HTML/CSS/JavaScript) - Works in any browser
  - 🖥️ **Desktop GUI** (Tkinter) - Modern graphical application
  - 💻 **Command-Line** - Interactive terminal interface
  - 📚 **Python Library** - Use as a module in your code
- **Comprehensive Unit Tests**: Test coverage for all calculations

## Installation

No external dependencies required. Works with Python 3.6+

```bash
# Clone the repository
cd Kinetic-energy-calculator

# Make scripts executable (optional)
chmod +x launch_web.py
chmod +x gui_calculator.py
chmod +x energy_calculator.py
```

## Quick Start

### 🚀 Launch Pad (Share-Friendly!)

A beautiful animated landing page perfect for sharing on social media:

```bash
python3 launch_web.py
```

Or open [rocket.html](rocket.html) directly - features:
- 🎨 Animated launching rocket
- 👥 Built-in social share buttons
- 🔗 Shareable link with one-click copy
- 📱 Mobile-responsive design
- ✨ Stunning space theme

### 🌐 Web Interface (Easiest - Recommended!)

**Option 1: One-Click Launcher**
```bash
python3 launch_web.py
```
This will automatically start a local server and open the calculator in your default browser.

**Option 2: Direct File**
Simply open `index.html` directly in any web browser (no server needed)

**Option 3: Manual Server**
```bash
python3 -m http.server 8000
# Then open http://localhost:8000 in your browser
```

**Features:**
- 🎨 Modern, responsive design (works on desktop, tablet, mobile)
- ⚡ Instant calculations with smooth animations
- 🌍 Quick planet gravity buttons (Earth 🌍, Moon 🌙, Mars 🔴, Jupiter 🪐)
- 📱 Works completely offline - no internet required
- 🎯 Beautiful tabbed interface with formula reference
- 4 tabs: Kinetic Energy, Potential Energy, Total Energy, Info

## Usage

### 🖥️ Desktop GUI Application

Modern graphical calculator with tabbed interface:

```bash
python3 gui_calculator.py
```

**Features:**
- **Kinetic Energy Tab** - Calculate KE with mass and velocity
- **Potential Energy Tab** - Calculate PE with mass, height, and gravity
- **Total Energy Tab** - Calculate both KE and PE simultaneously
- **Info Tab** - Reference formulas, units, and examples
- Quick planet gravity preset buttons
- Clean, professional design

### 💻 Command-Line Interface

Terminal-based interactive calculator:

```bash
python3 energy_calculator.py
```

**Menu options:**
1. **Kinetic Energy** - Input mass (kg) and velocity (m/s)
2. **Potential Energy** - Input mass (kg), height (m), and optional gravity
3. **Total Mechanical Energy** - Calculate both KE and PE
4. **Exit** - Quit the calculator

### Using as a Library

```python
from energy_calculator import EnergyCalculator

# Kinetic Energy: KE = 0.5 * m * v²
ke = EnergyCalculator.kinetic_energy(mass=5, velocity=10)  # 5 kg, 10 m/s
print(f"Kinetic Energy: {ke} J")  # Output: 250.0 J

# Potential Energy: PE = m * g * h
pe = EnergyCalculator.potential_energy(mass=5, height=20)  # Earth gravity
print(f"Potential Energy: {pe} J")  # Output: 981.0 J

# Custom gravity (e.g., Moon: 1.62 m/s²)
pe_moon = EnergyCalculator.potential_energy(mass=5, height=20, gravity=1.62)
print(f"Potential Energy (Moon): {pe_moon} J")  # Output: 162.0 J

# Total Mechanical Energy
total = EnergyCalculator.total_mechanical_energy(
    mass=5, 
    velocity=10, 
    height=20
)
print(f"Total Mechanical Energy: {total} J")  # Output: 1231.0 J
```

## Running Tests

Run the comprehensive unit test suite:

```bash
python3 -m unittest test_energy_calculator.py -v
```

Or run a specific test class:

```bash
python3 -m unittest test_energy_calculator.TestKineticEnergy -v
```

## Physics Equations

### Kinetic Energy
$$KE = \frac{1}{2}mv^2$$

Where:
- *KE* = Kinetic Energy (Joules)
- *m* = Mass (kilograms)
- *v* = Velocity (meters per second)

### Potential Energy
$$PE = mgh$$

Where:
- *PE* = Potential Energy (Joules)
- *m* = Mass (kilograms)
- *g* = Gravitational acceleration (m/s², default: 9.81 m/s² on Earth)
- *h* = Height (meters)

### Total Mechanical Energy
$$E_{total} = KE + PE$$

## SI Units Reference

| Quantity | Unit | Symbol |
|----------|------|--------|
| Mass | kilogram | kg |
| Velocity | meter per second | m/s |
| Height/Distance | meter | m |
| Acceleration | meter per second squared | m/s² |
| Energy | joule | J |

### Gravity Constants

- **Earth**: 9.81 m/s²
- **Moon**: 1.62 m/s²
- **Mars**: 3.71 m/s²
- **Jupiter**: 24.79 m/s²

## Examples

### Example 1: Falling Object
A 2 kg ball is dropped from a height of 10 meters.

```python
from energy_calculator import EnergyCalculator

mass = 2  # kg
height = 10  # m
velocity = 0  # m/s (at rest initially)

pe = EnergyCalculator.potential_energy(mass, height)
ke = EnergyCalculator.kinetic_energy(mass, velocity)
total = pe + ke

print(f"Initial PE: {pe:.2f} J")  # 196.2 J
print(f"Initial KE: {ke:.2f} J")  # 0 J
print(f"Total Energy: {total:.2f} J")  # 196.2 J
```

### Example 2: Moving Car
A 1000 kg car moving at 20 m/s on a bridge 5 meters high.

```python
from energy_calculator import EnergyCalculator

mass = 1000  # kg
velocity = 20  # m/s
height = 5  # m

ke = EnergyCalculator.kinetic_energy(mass, velocity)
pe = EnergyCalculator.potential_energy(mass, height)
total = EnergyCalculator.total_mechanical_energy(mass, velocity, height)

print(f"Kinetic Energy: {ke:.0f} J")  # 200,000 J
print(f"Potential Energy: {pe:.0f} J")  # 49,050 J
print(f"Total Mechanical Energy: {total:.0f} J")  # 249,050 J
```

## Input Validation

The calculator validates all inputs and raises `ValueError` for:
- Negative mass
- Negative velocity
- Negative height
- Negative gravitational acceleration

## License

Open source project
