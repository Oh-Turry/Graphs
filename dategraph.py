import datetime
from uuid import uuid4

import matplotlib.dates as dates
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d, make_interp_spline

# Plot with datetime! dates are on the X axis btw
def DatePlot(
    x_label: str,
    y_label: str,
    data: dict[datetime.datetime, int],
    grid: bool = False,
    savePath: str = None,
    x_colour: str = "blue",
    y_colour: str = "green",
    linecolour: str = "blue",
    marker_colour: str = "blue",
):
    def hideAxis(ax):
        # To hide the top and right borders so you can only have X, Y axis
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.get_xaxis().tick_bottom()
        ax.get_yaxis().tick_left()
        return True

    def smooth(x, y):
        # To smoothen the line
        x_smooth = np.linspace(x.min(), x.max(), 1000)
        spl = make_interp_spline(x, y, k=3)
        y_smooth = spl(x_smooth)
        return x_smooth, y_smooth

    def ColourWithName(x_colour, y_colour, x_label, y_label):
        xaxis = plt.xlabel(x_label)
        xaxis.set_color(x_colour)
        yaxis = plt.ylabel(y_label)
        yaxis.set_color(y_colour)
        return True

    # create data
    y = np.array(list(data.values()))
    x = dates.date2num(np.array(list(data.keys())))
    new_x, new_y = smooth(x, y)  # Call the smooth function
    new_x = dates.num2date(new_x)
    hideAxis(plt.subplot(111))
    ColourWithName(x_colour, y_colour, x_label, y_label)
    plt.plot(new_x, new_y, color=linecolour)  # Plot the new smooth curve.
    plt.plot(x, y, marker="o", linestyle="None", markersize=5, color=marker_colour)  # Hide the line but keep the markers
    if grid:
        plt.grid()
    if savePath is not None:
        path = f"{savePath}{str(uuid4())}.png"
        plt.savefig(path, transparent=True)
        return path
    plt.show()


# DatePlot("Test", "test", data, linecolour="red", marker_colour="green")
