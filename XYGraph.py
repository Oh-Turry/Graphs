import datetime
from uuid import uuid4

import matplotlib.dates as dates
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d, make_interp_spline
# x and y are numpy arrays. Please use numpy arrays only. Path should have a trailing '/'
def XYPlot(
    x,
    y,
    x_label: str,
    y_label: str,
    plot_name: str = None,
    grid: bool = False,
    savePath: str = None,
    x_colour: str = "blue",
    y_colour: str = "blue",
    linecolour: str = "blue",
    marker_colour: str = "green",
):
    plt.style.use("classic")
    plt.figure(figsize=[7, 6])

    def smoothCurve(x, y):
        cim = interp1d(x, y, kind="cubic")
        X_ = np.linspace(x.min(), x.max(), 500)
        Y_ = cim(X_)
        return X_, Y_

    def hideAxis(ax):
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.get_xaxis().tick_bottom()
        ax.get_yaxis().tick_left()
        return True

    def ColourWithName(x_colour, y_colour, x_label, y_label):
        xaxis = plt.xlabel(x_label)
        xaxis.set_color(x_colour)
        yaxis = plt.ylabel(y_label)
        yaxis.set_color(y_colour)
        return True

    ax = plt.subplot(111)
    hideAxis(ax)
    ColourWithName(x_colour, y_colour, x_label, y_label)
    newx, newy = smoothCurve(x, y)
    plt.plot(newx, newy, color=linecolour)
    plt.plot(x, y, marker="o", linestyle="None", markersize=5, color=marker_colour)
    plt.title(plot_name)
    if grid:
        plt.grid()
    if savePath is not None:
        path = f"{savePath}{str(uuid4())}.png"
        plt.savefig(path, transparent=True)
        return path
    plt.show()
