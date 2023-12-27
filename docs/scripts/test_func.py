import plotly.express as px
import tempfile
import plotly
import plotly.io as pio
import plotly.graph_objects as go
import sphinx_plotly_directive as spd

def func():
    # fig = px.scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16])

    # return fig

    fig = go.Figure(data=[go.Sankey(
        node = dict(
        pad = 15,
        thickness = 20,
        line = dict(color = "black", width = 0.5),
        label = ["A1", "A2", "B1", "B2", "C1", "C2"],
        color = "blue"
        ),
        link = dict(
        source = [0, 1, 0, 2, 3, 3], # indices correspond to labels, eg A1, A2, A1, B1, ...
        target = [2, 3, 3, 4, 4, 5],
        value = [8, 4, 2, 8, 4, 2]
    ))])

    fig.update_layout(title_text="Basic Sankey Diagram", font_size=10)
    spd.save_plotly_figure(fig, 'docs/_static/html/mitigationsanddatasources-1.html')
    return fig
func()
# func()

    # fig.write_html("docs/scripts/test_func.html", include_plotlyjs="cdn", auto_open=True)
    # # figure.show()
    # # return px.scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16])
    # # path = tempfile.NamedTemporaryFile(suffix=".html").name
    # fig_html = plotly.offline.plot(fig, output_type="div", include_plotlyjs="cdn", auto_open=False)
    # with open("docs/_build/mitigationsanddatasources/test_func.html", "w") as f:
    #     f.write(fig_html)
    # with open("docs/scripts/test_func.html", "w") as f:
    #     f.write(fig_html)