"""
Projectile Motion Calculator

This script calculates and displays projectile motion parameters.
Students can modify launch angles and velocities to see different results.
"""

import math


def calculate_projectile_motion(initial_velocity, angle_degrees, gravity=9.81):
    """
    Calculate projectile motion parameters.
    
    Args:
        initial_velocity: Initial velocity in m/s
        angle_degrees: Launch angle in degrees
        gravity: Gravitational acceleration (default: 9.81 m/s²)
    
    Returns:
        Dictionary containing motion parameters
    """
    # Convert angle to radians
    angle_rad = math.radians(angle_degrees)
    
    # Calculate velocity components
    v_x = initial_velocity * math.cos(angle_rad)
    v_y = initial_velocity * math.sin(angle_rad)
    
    # Calculate time of flight
    time_of_flight = (2 * v_y) / gravity
    
    # Calculate maximum height
    max_height = (v_y ** 2) / (2 * gravity)
    
    # Calculate range
    range_distance = v_x * time_of_flight
    
    return {
        'v_x': v_x,
        'v_y': v_y,
        'time_of_flight': time_of_flight,
        'max_height': max_height,
        'range': range_distance
    }


def main():
    """Main function to demonstrate projectile motion."""
    print("=" * 50)
    print("Projectile Motion Calculator")
    print("=" * 50)
    
    # Example calculations with different angles
    initial_velocity = 20  # m/s
    angles = [30, 45, 60]  # degrees
    
    for angle in angles:
        print(f"\nLaunch Angle: {angle}°")
        print("-" * 50)
        
        results = calculate_projectile_motion(initial_velocity, angle)
        
        print(f"   Initial velocity: {initial_velocity} m/s")
        print(f"   Horizontal velocity: {results['v_x']:.2f} m/s")
        print(f"   Vertical velocity: {results['v_y']:.2f} m/s")
        print(f"   Time of flight: {results['time_of_flight']:.2f} s")
        print(f"   Maximum height: {results['max_height']:.2f} m")
        print(f"   Range: {results['range']:.2f} m")
    
    print("\n" + "=" * 50)
    print("Try changing the initial_velocity or angles values!")
    print("=" * 50)


if __name__ == "__main__":
    main()
