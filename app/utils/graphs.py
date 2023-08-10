######################
#                    #
#   Plotly Graphs    #
#                    #
######################



# Import libraries
import plotly.graph_objects as go


def line_plot(df, x, y, title, x_title, y_title):
    """
    Create a line plot using plotly
    """

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df[x],
        y=df[y],
        mode='lines',
        line_shape="spline",
        line=dict(width=1),
        fill="tozeroy"
    ))

    fig.update_layout(
        title=title,
        xaxis_title=x_title,
        yaxis_title=y_title,
        font=dict(
            family="Courier New, monospace",
            size=18,
            color="#7f7f7f"
        )
    )

    return fig


def bar_plot(df, x, y, title, x_title, y_title):
    """
    Create a bar plot using plotly
    """
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=x,
        y=y,
        marker_color='indianred'
    ))

    fig.update_layout(
        title=title,
        xaxis_title=x_title,
        yaxis_title=y_title,
        font=dict(
            family="Courier New, monospace",
            size=18,
            color="#7f7f7f"
        )
    )

    return fig


def pie_plot(df, labels, values, title):
    """
    Create a pie plot using plotly
    """
    fig = go.Figure()

    fig.add_trace(
        go.Pie(
            labels=df[labels],
            values=df[values],
            name=title)
    )

    # Use `hole` to create a donut-like pie chart
    fig.update_traces(hole=.4, hoverinfo="label+percent+name")

    fig.update_layout(
        title=title,
        width=700,
        annotations=[dict(text='Title', x=0.5, y=0.5,
                          font_size=20, showarrow=False)],
        legend=dict(orientation="h"),
        font=dict(
            family="Courier New, monospace",
            size=18,
            color="#7f7f7f"
        )
    )

    return fig


def percentage_ring_plot(perc:int):

    fig = go.Figure()

    fig.add_trace(
        go.Pie(
            labels=["A", "B"],
            values=[perc, 100-perc])
    )

    # Use `hole` to create a donut-like pie chart
    fig.update_traces(
        hole=.9,
        hoverinfo='none',
        textinfo='none',
        marker=dict(colors=["#228be6", "#f0f3f5"]),
    )

    fig.update_layout(
        annotations=[
            dict(text=f'<b>{perc}%</b> <br>Completed',
                 x=0.5, y=0.5, 
                 # font_size=20
                 showarrow=False)],
        showlegend=False,
        margin=dict(t=40, b=20, l=20, r=20),
        width=160,
        height=160,
    )

    return fig