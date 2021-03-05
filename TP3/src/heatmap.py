'''
    Contains some functions related to the creation of the heatmap.
'''
import plotly.express as px
import hover_template as template


def get_figure(data):
    '''
        Generates the heatmap from the given dataset.

        Make sure to set the title of the color bar to 'Trees'
        and to display each year as an x-tick.

        Args:
            data: The data to display
        Returns:
            The figure to be displayed.
    '''

    # TODO : Create the heatmap. Make sure to set dragmode=False in
    # the layout. Also don't forget to include the hover template.
    fig = px.imshow(data)
    fig.update_xaxes(title=dict(text=''), type='log')
    fig.update_yaxes(title=dict(text=''))
    fig.update_layout(coloraxis_colorbar=dict(title="Trees"))
    fig.update_traces(hovertemplate=template.get_heatmap_hover_template())
    return fig
