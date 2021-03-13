'''
    Provides the template for the tooltips.
'''


def get_bubble_hover_template():
    '''
        Sets the template for the hover tooltips.
        
        Contains four labels, followed by their corresponding
        value and units where appropriate, separated by a
        colon : country, population, GDP and CO2 emissions.

        The labels' font is bold and the values are normal weight

        returns:
            The content of the tooltip
    '''
    # TODO : Generate tooltip
    style_country = "<b style = 'font-weight:bold'>Country : </b>" + "<b style = 'font-weight:normal'>%{country}</b>" 
    style_population = "<br><b style = 'font-weight:bold'>Population : </b >" + "<b style = 'font-weight:normal'>{size} </b>"
    style_gdp = "<br><b style = 'font-weight:bold'>GDP : </b>" + "<b style = 'font-weight:normal'>%{x} $ (USD)</b>"
    style_co2 = "<br><b style = 'font-weight:bold'>CO2 : </b>" + "<b style = 'font-weight:normal'> %{y} metric tonnes </b>"

    return style_country + style_population + style_gdp + style_co2 +  "<extra></extra>"
