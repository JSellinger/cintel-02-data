import plotly.express as px
from shiny.express import input, ui
from shinywidgets import render_plotly
import palmerpenguins as pp

penguins_df = pp.load_penguins()

ui.page_opts(title="Jacob 'Baby' Sellinger's Penguin Dataset", fillable=True)
with ui.layout_columns():
    
    @render_plotly
    def plot1():
        return px.histogram(px.data.tips(), y="tip")

    @render_plotly
    def plot2():
        return px.histogram(px.data.tips(), y="total_bill")
