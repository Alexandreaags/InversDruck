import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import serial
pico = serial.Serial("COM6", 115200)
# Function to generate random data for demonstration purposes


# Function to update the data and redraw the chart
def update_data(i):
    inst_acc_z = str(pico.readline())
    inst_acc_z = float(inst_acc_z[2:-6])
    print(inst_acc_z)
    # Get the new data point (replace this with your actual data source)
    new_data = inst_acc_z
    # Append the new data point to the list
    data.append(new_data)

    # Truncate the data to keep only the last 50 data points (adjust as needed)
    data[:] = data[-50:]

    # Clear the previous chart
    plt.clf()

    # Plot the data
    plt.plot(range(len(data)), data, color='b', marker='o', linestyle='-', markersize=5)
    plt.xlabel('Time')
    plt.ylabel('Acceleration on Z [g]')
    plt.title('Real-Time Acceleration')
    plt.grid()

    # Limitando o eixo y entre 0 e 100
    plt.ylim(-2, 2)

# Main function to set up and run the dashboard
if __name__ == '__main__':
    # Initialize an empty list to store the data points
    data = []

    # Set up the figure and axis for the chart
    fig, ax = plt.subplots()

    # Create the animation that calls the update_data function every 1000 ms (1 second)
    ani = FuncAnimation(fig, update_data, interval = 1)

    # Show the real-time dashboard
    plt.show()