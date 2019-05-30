import matplotlib.pyplot as plt
import numpy as np

def tt_plot(t1, t2, f1, f2, desc):
    fig = plt.figure(figsize=(5, 5))
    ax = plt.axes()

    # ax.xaxis.set_major_locator(plt.MaxNLocator(10))
    # ax.xaxis.set_major_locator(plt.MultipleLocator(6))

    # ax.yaxis.set_major_locator(plt.MaxNLocator(10))
    # ax.yaxis.set_major_locator(plt.MultipleLocator(10))

    plt.plot(np.log10(t1), np.log10(t2), 'ob', markersize=2)

    # for i in range(len(t)):
    #    if t[i]<40:
    #        plt.plot(np.log10(t[i]), np.log10(t2[i]),'og', markersize=2)

    plt.title('T-T at {0}-{1} MHz'.format(f1, f2), fontsize='14')  #

    plt.xlabel('log10(T{0})'.format(f1), fontsize='14')
    plt.ylabel('log10(T{0})'.format(f2), fontsize='14')

    # fig.savefig('tmp/tt.png')
    fname = "tmp/tt_{0}_{1}_{2}.png".format(f1,f2,desc[0:4])
    fig.savefig(fname)


    # plt.show()