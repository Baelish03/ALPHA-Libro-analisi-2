import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon

plt.rcParams['text.usetex'] = True #using latex
matplotlib.rcParams.update({'font.size': 20}) #font size

fig, ax = plt.subplots()#figsize=(10, 10))

# Select length of axes and the space between tick labels
xmin, xmax, ymin, ymax = 0.9, 2, 0.9, 1
ticks_frequency = 0.1

# Set identical scales for both axes
ax.set(xlim=(xmin-1, xmax+1), ylim=(ymin-1, ymax+1), aspect='equal')

# Set bottom and left spines as x and y axes of coordinate system
ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')

# Remove top and right spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Create 'x' and 'y' labels placed at the end of the axes
ax.set_xlabel('$x$', labelpad=-24, x=1.03)
ax.set_ylabel('$y$', labelpad=-21, y=1.02, rotation=0)

# Create custom major ticks to determine position of tick labels
x_ticks = np.arange(xmin, xmax+1, ticks_frequency)
y_ticks = np.arange(ymin, ymax+1, ticks_frequency)
#ax.set_xticks(x_ticks[x_ticks != 0])
#ax.set_yticks(y_ticks[y_ticks != 0])

# Create minor ticks placed at each integer to enable drawing of minor grid
# lines: note that this has no effect in this example with ticks_frequency=1
#ax.set_xticks(np.arange(xmin, xmax+1), minor=True)
#ax.set_yticks(np.arange(ymin, ymax+1), minor=True)

# Draw major and minor grid lines
#ax.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)

# Draw arrows
arrow_fmt = dict(markersize=4, color='black', clip_on=False)
ax.plot((1), (0), marker='>', transform=ax.get_yaxis_transform(), **arrow_fmt)
ax.plot((0), (1), marker='^', transform=ax.get_xaxis_transform(), **arrow_fmt)

def function(x):
    return np.array(-np.log(x))

# Plot function
c = 0.1
a = 0.2
b = 1
x = np.arange(c, b + 0.1, 0.1)
plt.plot(x, function(x), color='r')

# Draw lines connecting points to axes
ax.plot([a, a], [0, function(a)], c='k', ls='--', lw=1.5, alpha=0.5)
ax.plot([b, b], [0, function(b)], c='k', ls='--', lw=1.5, alpha=0.5)

# Use tex in labels
ax.set_xticks([a, b])
ax.set_xticklabels(["$c$","$1$"], color="k")
ax.set_yticks([])

# Add text
ax.text(.3, function(a) , r"$y=f(x)$", color='r')
ax.text(2, 1, r"$0 < c \leq 1$", color='b')

# Draw integral area
ix = np.linspace(a, b)
iy = function(ix)
verts = [(a, 0), *zip(ix, iy), (b, 0)]
poly = Polygon(verts, color='r', alpha=0.2)
ax.add_patch(poly)

plt.show()