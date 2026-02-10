"""
Data Analysis and Visualization

This script demonstrates reading data from a file and creating simple plots.
It's perfect for practicing data analysis basics.
"""

import numpy as np
import matplotlib.pyplot as plt


def load_data(filename):
    """
    Load data from a CSV file.
    
    Args:
        filename: Path to the data file
    
    Returns:
        Tuple of (time, position) arrays
    """
    try:
        data = np.loadtxt(filename, delimiter=',', skiprows=1)
        time = data[:, 0]
        position = data[:, 1]
        return time, position
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
        print("Generating sample data instead...")
        time = np.linspace(0, 10, 50)
        position = 5 * time + 0.5 * 9.81 * time**2
        return time, position


def calculate_velocity(time, position):
    """
    Calculate velocity from position data using numerical differentiation.
    
    Args:
        time: Time array
        position: Position array
    
    Returns:
        Velocity array
    """
    velocity = np.gradient(position, time)
    return velocity


def plot_motion(time, position, velocity):
    """
    Create plots for position and velocity vs time.
    
    Args:
        time: Time array
        position: Position array
        velocity: Velocity array
    """
    plt.figure(figsize=(12, 5))
    
    # Plot position vs time
    plt.subplot(1, 2, 1)
    plt.plot(time, position, 'b-', linewidth=2, label='Position')
    plt.xlabel('Time (s)', fontsize=12)
    plt.ylabel('Position (m)', fontsize=12)
    plt.title('Position vs Time', fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    # Plot velocity vs time
    plt.subplot(1, 2, 2)
    plt.plot(time, velocity, 'r-', linewidth=2, label='Velocity')
    plt.xlabel('Time (s)', fontsize=12)
    plt.ylabel('Velocity (m/s)', fontsize=12)
    plt.title('Velocity vs Time', fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.legend()
    
    plt.tight_layout()
    plt.savefig('motion_analysis.png', dpi=150)
    print("\nPlot saved as 'motion_analysis.png'")
    plt.show()


def calculate_statistics(data):
    """
    Calculate basic statistics for the data.
    
    Args:
        data: Data array
    
    Returns:
        Dictionary of statistics
    """
    return {
        'mean': np.mean(data),
        'std': np.std(data),
        'min': np.min(data),
        'max': np.max(data)
    }


def main():
    """Main function for data analysis."""
    print("=" * 50)
    print("Data Analysis and Visualization")
    print("=" * 50)
    
    # Load data
    filename = 'motion_data.csv'
    time, position = load_data(filename)
    
    # Calculate velocity
    velocity = calculate_velocity(time, position)
    
    # Display statistics
    print("\nPosition Statistics:")
    pos_stats = calculate_statistics(position)
    for key, value in pos_stats.items():
        print(f"   {key.capitalize()}: {value:.2f}")
    
    print("\nVelocity Statistics:")
    vel_stats = calculate_statistics(velocity)
    for key, value in vel_stats.items():
        print(f"   {key.capitalize()}: {value:.2f}")
    
    # Create plots
    print("\nGenerating plots...")
    plot_motion(time, position, velocity)
    
    print("\n" + "=" * 50)


if __name__ == "__main__":
    main()
