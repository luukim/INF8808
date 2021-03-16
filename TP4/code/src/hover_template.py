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
    # TODO : Generate tooltip : bubble get plot custom_data pour passer country name, et app custom_data , on peut faire 
    style_country = "<span style = 'font-weight:bold'>Country : </span>" + "<span style = 'font-weight:normal'>%{customdata}</span>" 
    style_population = "<br><span style = 'font-weight:bold'>Population : </span >" + "<span style = 'font-weight:normal'>%{marker.size} </span>"
    style_gdp = "<br><span style = 'font-weight:bold'>GDP : </span>" + "<span style = 'font-weight:normal'>%{x} $ (USD)</span>"
    style_co2 = "<br><span style = 'font-weight:bold'>CO2 : </span>" + "<span style = 'font-weight:normal'> %{y} metric tonnes </span>"
# change b for span, 
    return style_country + style_population + style_gdp + style_co2 +  "<extra></extra>"
