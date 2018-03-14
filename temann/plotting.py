import ternary
from ternary.helpers import simplex_iterator

from .interpret import get_empirical_formula
from .prediction import predict_seebeck

__all__ = ['plot_ternary']


def three_elements_to_formula(e1, e2, e3, n1, n2, n3):
    """input 3 strs and 3 coefficients output the compound formula"""
    # Make into lists and check data type
    elem = [e1, e2, e3]
    stoich = [n1, n2, n3]
    assert all(isinstance(item, str) for item in elem), 'Element inputs must be strings'
    assert all(not isinstance(item, str) for item in stoich), 'Stoichiometry inputs must be numerical'

    return e1 + str(n1) + e2 + str(n2) + e3 + str(n3)


def generate_heatmap_data(e1, e2, e3, sg, T, scale):
    heat_dict = {}
    # Make sure sg, T, scale inputs are valid
    assert type(sg) == int, 'Space group input must be integer'
    assert sg < 231, 'Not a valid space group'
    assert T > 0, 'Choose a positive temperature in Kelvin'
    assert type(scale) == int, 'scale input must integer'
    assert scale > 0, 'scale must be positive value'

    for (i, j, k) in simplex_iterator(scale):
        compound = three_elements_to_formula(e1, e2, e3, i, j, k)
        heat = predict_seebeck(compound, sg, T)
        heat_dict[(i, j)] = heat
    return heat_dict


def plot_ternary(elements, sg, T=400, scale=10, fontsize=14, dpi=200,
                 inches=(10, 8), savefigure=False):

    assert not isinstance(formula, list), \
        'Cannot pass a list. Input must be a string'
    assert isinstance(formula, str), 'Must pass a string.'
    assert len(elements) < 7, 'Must pass 3 elements, at most a length of 6 letters'
    assert sum(1 for x in elements if x.isupper()) == 3, \
        'Must be 3 capital letters for input, 3 elements'

    # Boundary and Gridlines
    figure, tax = ternary.figure(scale=scale)
    figure.set_size_inches(inches)
    figure.set_dpi(dpi)

    # Draw Boundary and Gridlines
    tax.boundary(linewidth=1.0)
    tax.gridlines(color="black", multiple=6)
    tax.gridlines(color="blue", multiple=2, linewidth=0.5)

    # Parse the elements into individual variables
    e1, e2, e3 = list(get_empirical_formula(elements).keys())

    # Set Axis labels and Title
    tax.set_title("{}{}{} Ternary Seebeck Prediction".format(e1, e2, e3),
                  fontsize=fontsize)

    tax.left_axis_label("{} Content (out of {})".format(e3, scale),
                        fontsize=fontsize)

    tax.right_axis_label("{} Content (out of {})".format(e2, scale),
                         fontsize=fontsize)

    tax.bottom_axis_label("{} Content (out of {})".format(e1, scale),
                          fontsize=fontsize, ha='center')

    data = generate_heatmap_data(e1, e2, e3, sg, T, scale)
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
