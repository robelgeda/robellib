def mpl_tick_frame(ax=None, minorticks=True, tick_fontsize=None):
    if ax is None:
        ax = plt.gca()
    if minorticks:
        ax.minorticks_on()
    ax.tick_params(which='minor', direction='in', top=True, right=True,
                   width=1.5, length=8 / 2, labelsize=tick_fontsize)
    ax.tick_params(which='major', direction='in', top=True, right=True,
                   width=1.5, length=8, labelsize=tick_fontsize)
