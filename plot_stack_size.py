import matplotlib.pyplot as plt

stack_sizes = []
durations = []

# Reading data from the file
with open("stack_sizes.csv", "r") as f:
    for line in f.readlines():
        stack_size, duration = line.split(",")
        stack_sizes.append(int(stack_size))
        durations.append(int(duration) / 1_000_000)

# Create the first plot for stack_sizes
fig, ax1 = plt.subplots()
color = 'tab:red'
ax1.set_xlabel('Time (tokens)')
ax1.set_ylabel('Stack Size', color=color)
ax1.plot(stack_sizes, color=color, label='Stack size')
ax1.tick_params(axis='y', labelcolor=color)

# Create a second y-axis for durations
ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('Duration (seconds)', color=color)
ax2.plot(durations, color=color, label='Duration (seconds)')
ax2.tick_params(axis='y', labelcolor=color)

# Adding a title and showing the plot
plt.title('Grammar Stack Size and Duration Over Time')
fig.tight_layout()  # Adjust the layout
plt.show()
