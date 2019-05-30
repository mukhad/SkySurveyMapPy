import matplotlib.pyplot as plt


def scatter_map(ra,dec,t,fmhz):
    fig = plt.figure()
    ax = plt.axes()

    plt.xlim(24, 0)
    plt.ylim(-15, 85)

    # ax.xaxis.set_major_locator(plt.MaxNLocator(10))
    ax.xaxis.set_major_locator(plt.MultipleLocator(6))

    # ax.yaxis.set_major_locator(plt.MaxNLocator(10))
    ax.yaxis.set_major_locator(plt.MultipleLocator(10))

    # https://matplotlib.org/tutorials/colors/colormaps.html
    map_clr = ['gray', 'viridis', 'hsv']

    plt.scatter(ra, dec, c=t, cmap=map_clr[2])

    plt.colorbar()
    plt.title('brightness sky map at {0} MHz'.format(fmhz), fontsize='14')

    #fig.savefig('tmp/scatter.png')

    fname = "tmp/scatter_{0}.png".format(fmhz)
    fig.savefig(fname)
    # plt.show()


def contour_map(ra, dec, t, fmhz):
    x = ra.reshape((51, 48))
    y = dec.reshape((51, 48))
    z = t.reshape((51, 48))

    fig = plt.figure(figsize=(16, 4))

    plt.xlim(24, 0)
    plt.ylim(-15, 85)

    # plt.contour(z, colors='black')
    # plt.contour(x, y, z, 20, colors='black')
    plt.contourf(x, y, z, 20, cmap='gray')

    plt.colorbar()
    plt.title('brightness sky map at {0} MHz'.format(fmhz), fontsize='14')  #
    plt.xlabel('ra', fontsize='14')
    plt.ylabel('dec', fontsize='14')

    # fig.savefig('tmp/contour.png')
    fname = "tmp/contour_{0}.png".format(fmhz)
    fig.savefig(fname)

    # plt.show()


def imshow_map(ra, dec, t, fmhz, desc):
    x = ra.reshape((51, 48))
    y = dec.reshape((51, 48))
    z = t.reshape((51, 48))

    fig = plt.figure(figsize=(16,4))
    plt.xlim(24,0)
    plt.ylim(-15,85)

    plt.rcParams["figure.figsize"] = 16,4

    contours = plt.contour(x,y,z, 10, colors='black')
    plt.clabel(contours, inline=True, fmt = '%1.0f', fontsize=10)

    plt.imshow(z,extent=[0,24,85,-15],  aspect= 'auto',cmap='gray', alpha=0.5)

    plt.axis(aspect='image')

    plt.colorbar()
    plt.title('brightness sky map at {0} MHz'.format(fmhz),fontsize='14') #
    plt.xlabel('ra',fontsize='14')
    plt.ylabel('dec',fontsize='14')

    # fig.savefig('tmp/imshow.png')
    fname = "tmp/imshow_{0}_{1}.png".format(fmhz,desc[0:4])
    fig.savefig(fname)

    # plt.show()