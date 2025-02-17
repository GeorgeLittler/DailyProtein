import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Cursor

# Define body mass range (in pounds)
body_mass = np.arange(100, 301, 10)  # From 100 lb to 300 lb, step of 10 lb

# Calculate protein intake (grams) for different multipliers
protein_08 = body_mass * 0.8
protein_10 = body_mass * 1.0
protein_12 = body_mass * 1.2

# Create the figure and axis
fig, ax = plt.subplots(figsize=(8, 5))

# Fill the area between the lowest and highest lines with light green
ax.fill_between(body_mass, protein_08, protein_12, color='lightgreen', alpha=0.3)

# Plot the lines
line_08, = ax.plot(body_mass, protein_08, label="0.8g/lb", color="orange", linestyle='-', marker='o')
line_10, = ax.plot(body_mass, protein_10, label="1.0g/lb", color="blue", linestyle='-', marker='o')
line_12, = ax.plot(body_mass, protein_12, label="1.2g/lb", color="red", linestyle='-', marker='o')

# Labels and title
ax.set_xlabel("Body Mass (lb)")
ax.set_ylabel("Protein Intake (g)")
ax.set_title("Protein Intake Recommendations Based on Body Mass")
ax.legend()
ax.grid(True)

# Add interactive cursor
cursor = Cursor(ax, useblit=True, color='black', linewidth=1)

# Create annotation for hover effect
annot = ax.annotate("", xy=(0, 0), xytext=(10, 10),
                    textcoords="offset points", 
                    bbox=dict(boxstyle="round", fc="w"),
                    arrowprops=dict(arrowstyle="->"))
annot.set_visible(False)

# Function to update annotation on hover
def update_annot(line, event):
    xdata, ydata = line.get_xdata(), line.get_ydata()
    if event.xdata is not None and event.ydata is not None:
        index = np.argmin(np.abs(xdata - event.xdata))
        x, y = xdata[index], ydata[index]
        annot.xy = (x, y)
        annot.set_text(f"({x}lb, {y}g)")
        annot.set_visible(True)
        fig.canvas.draw_idle()

# Event handler for motion
def on_motion(event):
    vis = annot.get_visible()
    if event.inaxes == ax:
        for line in [line_08, line_10, line_12]:
            cont, _ = line.contains(event)
            if cont:
                update_annot(line, event)
                return
    if vis:
        annot.set_visible(False)
        fig.canvas.draw_idle()

# Connect event to figure
fig.canvas.mpl_connect("motion_notify_event", on_motion)

# Show the graph
plt.show()
