import ternary
from ternary.helpers import simplex_iterator

from .interpret import get_empirical_formula
from .prediction import predict_seebeck

__all__ = ['plot_ternary']


def three_elements_to_formula(e1, e2, e3, n1, n2, n3):
    """input 3 strs and 3 coefficients output the compound formula"""
    elem = [e1, e2, e3]
    stoich = [n1, n2, n3]
    assert all(isinstance(item, str) for item in elem)
    assert ~ all(isinstance(item, str) for item in stoich)

    return e1 + str(n1) + e2 + str(n2) + e3 + str(n3)


def generate_heatmap_data(e1, e2, e3, sg, T, scale):
    heat_dict = {}
    for (i, j, k) in simplex_iterator(scale):
        compound = three_elements_to_formula(e1, e2, e3, i, j, k)
        heat = predict_seebeck(compound, sg, T)
        heat_dict[(i, j)] = heat
    return heat_dict


def plot_heatmap(data, e1, e2, e3, scale, fontsize, dpi, size, savefigure):
    # Boundary and Gridlines
    figure, tax = ternary.figure(scale=scale)
    figure.set_size_inches(size)
    figure.set_dpi(dpi)

    # Draw Boundary and Gridlines
    tax.boundary(linewidth=1.0)
    tax.gridlines(color="black", multiple=6)
    tax.gridlines(color="blue", multiple=2, linewidth=0.5)

    # Set Axis labels and Title
    tax.set_title("{}{}{} Ternary Seebeck Prediction".format(e1, e2, e3),
                  fontsize=fontsize)

    tax.left_axis_label("{} Content (out of {})".format(e3, scale),
                        fontsize=fontsize)

    tax.right_axis_label("{} Content (out of {})".format(e2, scale),
                         fontsize=fontsize)

    tax.bottom_axis_label("{} Content (out of {})".format(e1, scale),
                          fontsize=fontsize, ha='center')

    tax.heatmap(data, style="h", cbarlabel='Seebeck Coefficient (uV/K)')
    tax.boundary()
    tax.ticks(axis='lbr', linewidth=1, multiple=1)

    tax.clear_matplotlib_ticks()
    tax.ax.set_axis_off()

    if savefigure:
        tax.savefig('ternary.png', dpi=dpi)
    else:
        pass

    tax.show()


def plot_ternary(elements, sg, T=400, scale=10, fontsize=14, dpi=100,
                 size=(10, 8), savefigure=False):

    # Parse the elements into individual variables
    e1, e2, e3 = list(get_empirical_formula(elements).keys())

    data = generate_heatmap_data(e1, e2, e3, sg, T, scale)
    plot_heatmap(data, e1, e2, e3, scale, fontsize, dpi, size, savefigure)
    return
