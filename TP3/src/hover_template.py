'''
    Provides the templates for the tooltips.
'''


def get_heatmap_hover_template():
    '''
        Sets the template for the hover tooltips in the heatmap.

        Contains three labels, followed by their corresponding
        value, separated by a colon : neighborhood, year and
        trees planted.

        The labels are font 'Roboto Slab' and bold. The values
        are font 'Roboto' and regular weight.
    '''
    # TODO : Define and return the hover template
    return "<b style = 'font-weight:bold; font-family:Roboto Slab'>Neighborhood : </b>" + "<b style = 'font-family:Roboto'>%{x} </b>" + "<br><b style = 'font-family:Roboto Slab'>Year : </b>" + "<b style = 'font-family:Roboto'>%{y}</b>" + "<br><b style = 'font-family:Roboto Slab'>Trees planted : </b>" + "<b style = 'font-family:Roboto'>%{z}</b>"+ "<extra></extra>"

def get_linechart_hover_template():
    '''
        Sets the template for the hover tooltips in the heatmap.

        Contains two labels, followed by their corresponding
        value, separated by a colon : date and trees planted.

        The labels are font 'Roboto Slab' and bold. The values
        are font 'Roboto' and regular weight.
    '''
    # TODO : Define and return the hover template
    return "<b style = 'font-family:Roboto Slab'>Date : </b>" + "<b style = 'font-family:Roboto'>%{x}</b>" + "<br><b style = 'font-family:Roboto Slab'>Trees planted : </b>" + "<b style = 'font-family:Roboto'>%{y}</b>" + "<extra></extra>"

