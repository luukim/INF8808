'''
    Contains some functions related to the creation of the bar chart.
    The bar chart displays the data either as counts or as percentages.
'''

import plotly.graph_objects as go
import plotly.io as pio

from hover_template import get_hover_template
from modes import MODES, MODE_TO_COLUMN


def init_figure():
    '''
        Initializes the Graph Object figure used to display the bar chart.
        Sets the template to be used to "simple_white" as a base with
        our custom template on top. Sets the title to 'Lines per act'

        Returns:
            fig: The figure which will display the bar chart
    '''
    fig = go.Figure()

    # TODO : Update the template to include our new theme and set the title

    fig.update_layout(
        template=pio.templates['simple_white+new_template'],
        dragmode=False,
        title=dict(text='Lines per act'),
    )

    return fig


def draw(fig, data, mode):
    '''
        Draws the bar chart.

        Arg:
            fig: The figure comprising the bar chart
            data: The data to be displayed
            mode: Whether to display the count or percent data.
        Returns:
            fig: The figure comprising the drawn bar chart
    '''
    fig = go.Figure(fig)  # conversion back to Graph Object
    # TODO : Update the figure's data according to the selected mode
   

    y_axis = ""
    if (mode ==  MODES['count']): 
        y_axis = 'PlayerLine'
    elif (mode ==  MODES['percent']): 
        y_axis = 'PlayerPercent'

    data = update_x_axis(data)

    fig = go.Figure(data=[
        go.Bar(name='Benvolio', x=data.loc[data['Player'] == 'Benvolio']['Act'], y=data.loc[data['Player'] == 'Benvolio'][y_axis]),
        go.Bar(name='Juliet', x=data.loc[data['Player'] == 'Juliet']['Act'], y=data.loc[data['Player'] == 'Juliet'][y_axis]),
        go.Bar(name='Mercutio', x=data.loc[data['Player'] == 'Mercutio']['Act'], y=data.loc[data['Player'] == 'Mercutio'][y_axis]),
        go.Bar(name='Nurse', x=data.loc[data['Player'] == 'Nurse']['Act'], y=data.loc[data['Player'] == 'Nurse'][y_axis]),
        go.Bar(name='Other', x=data.loc[data['Player'] == 'Other']['Act'], y=data.loc[data['Player'] == 'Other'][y_axis]),
        go.Bar(name='Romeo', x=data.loc[data['Player'] == 'Romeo']['Act'], y=data.loc[data['Player'] == 'Romeo'][y_axis])
    ])

    fig.update_layout(barmode='stack', 
    template=pio.templates['simple_white+new_template'],
    title=dict(text='Lines per act'))
    return fig


def update_y_axis(fig, mode):
    '''
        Updates the y axis to say 'Lines (%)' or 'Lines (Count) depending on
        the current display.

        Args:
            mode: Current display mode
        Returns: 
            The updated figure
    '''
    y_axis = ""
    if (mode ==  MODES['count']): 
        y_axis = 'Lines (Count)'
    elif (mode ==  MODES['percent']): 
        y_axis = 'Lines (%)'
    
    fig.update_layout(yaxis_title = y_axis)

    return fig
    # TODO : Update the y axis title according to the current mode

def update_x_axis(data):
    data['Act'] = data['Act'].replace(1, 'Act 1')
    data['Act'] = data['Act'].replace(2, 'Act 2')
    data['Act'] = data['Act'].replace(3, 'Act 3')
    data['Act'] = data['Act'].replace(4, 'Act 4')
    data['Act'] = data['Act'].replace(5, 'Act 5')

    return data