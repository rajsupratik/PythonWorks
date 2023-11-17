import math
import random

def launch_rocket(velocity, angle):
    # Constants
    g = 9.8  # Acceleration due to gravity on Earth (m/s^2)
    initial_height = 0  # Initial height of the rocket (meters)

    # Convert launch angle to radians
    launch_angle_rad = math.radians(angle)

    # Calculate horizontal and vertical components of velocity
    horizontal_velocity = velocity * math.cos(launch_angle_rad)
    vertical_velocity = velocity * math.sin(launch_angle_rad)

    # Calculate time of flight
    time_of_flight = (2 * vertical_velocity) / g

    # Calculate horizontal range
    horizontal_range = horizontal_velocity * time_of_flight

    # Calculate maximum height
    max_height = (vertical_velocity ** 2) / (2 * g) + initial_height

    return horizontal_range, max_height

def simulate_rocket_launch():
    # Randomly generate launch parameters for simulation
    velocity = random.uniform(50, 100)  # Random velocity between 50 and 100 m/s
    launch_angle = random.uniform(30, 60)  # Random launch angle between 30 and 60 degrees

    # Simulate rocket launch
    horizontal_range, max_height = launch_rocket(velocity, launch_angle)

    # Display simulation results
    print(f"Rocket Launch Simulation:")
    print(f"Velocity: {velocity:.2f} m/s")
    print(f"Launch Angle: {launch_angle:.2f} degrees")
    print(f"Horizontal Range: {horizontal_range:.2f} meters")
    print(f"Maximum Height: {max_height:.2f} meters")

if __name__ == "__main__":
    simulate_rocket_launch()
