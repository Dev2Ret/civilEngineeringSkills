import plotly.graph_objects as go

class CustomPlot:
    def FormatPlot(title, xtitle, ytitle):
        fig = go.Figure()
        fig.update_layout(title=title) # font, color
        fig.update_xaxes(title_text=xtitle, ticks='outside',
                        showline=True)
        fig.update_yaxes(title_text=ytitle, ticks='outside',
                        showline=True)
        return fig