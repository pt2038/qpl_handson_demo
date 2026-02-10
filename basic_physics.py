"""
Basic Physics Formulas Calculator

This script demonstrates simple physics calculations.
It's designed for beginners to practice editing and running Python code.
"""

def calculate_velocity(distance, time):
    """
    Calculate velocity given distance and time.
    
    Args:
        distance: Distance traveled in meters
        time: Time taken in seconds
    
    Returns:
        Velocity in meters per second
    """
    velocity = distance / time
    return velocity


def calculate_acceleration(initial_velocity, final_velocity, time):
    """
    Calculate acceleration given initial and final velocities and time.
    
    Args:
        initial_velocity: Initial velocity in m/s
        final_velocity: Final velocity in m/s
        time: Time period in seconds
    
    Returns:
        Acceleration in m/s²
    """
    acceleration = (final_velocity - initial_velocity) / time
    return acceleration


def calculate_force(mass, acceleration):
    """
    Calculate force using Newton's second law: F = ma
    
    Args:
        mass: Mass in kilograms
        acceleration: Acceleration in m/s²
    
    Returns:
        Force in Newtons
    """
    force = mass * acceleration
    return force


def main():
    """Main function to demonstrate physics calculations."""
    print("=" * 50)
    print("Basic Physics Calculator")
    print("=" * 50)
    
    # Example 1: Calculate velocity
    distance = 100  # meters
    time = 5  # seconds
    velocity = calculate_velocity(distance, time)
    print(f"\n1. Velocity Calculation:")
    print(f"   Distance: {distance} m")
    print(f"   Time: {time} s")
    print(f"   Velocity: {velocity} m/s")
    
    # Example 2: Calculate acceleration
    v_initial = 0  # m/s
    v_final = 20  # m/s
    time_accel = 4  # seconds
    acceleration = calculate_acceleration(v_initial, v_final, time_accel)
    print(f"\n2. Acceleration Calculation:")
    print(f"   Initial velocity: {v_initial} m/s")
    print(f"   Final velocity: {v_final} m/s")
    print(f"   Time: {time_accel} s")
    print(f"   Acceleration: {acceleration} m/s²")
    
    # Example 3: Calculate force
    mass = 10  # kg
    force = calculate_force(mass, acceleration)
    print(f"\n3. Force Calculation:")
    print(f"   Mass: {mass} kg")
    print(f"   Acceleration: {acceleration} m/s²")
    print(f"   Force: {force} N")
    
    print("\n" + "=" * 50)


if __name__ == "__main__":
    main()
    # Test
