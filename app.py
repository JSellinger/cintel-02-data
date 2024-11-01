import plotly.express as px
import seaborn as sb
import palmerpenguins as pp
from shiny.express import input, render, ui
from shinywidgets import render_plotly
from shiny import render
import plotly.graph_objects as go

p_df = pp.load_penguins()

ui.page_opts(title="Filling layout", fillable=True)

with ui.layout_columns():
    
    with ui.card():
        ui.card_header("Data Table")
        @render.data_frame
        def table1():
            return render.DataTable(p_df)
        
            
    with ui.card():
        ui.card_header("Data Grid")
        @render.data_frame
        def datagrid1():
            return render.DataGrid(p_df)

with ui.layout_columns():

    with ui.card():
        ui.card_header("Plotly Histogram - Species")
        @render_plotly
        def plot1():
            return px.histogram(p_df, y="species")
                                
    with ui.card():
        ui.card_header("Seaborn Histogram - Species")
        @render.plot
        def plot2():
            return sb.histplot(p_df, y="species")
            
    with ui.card():
        ui.card_header("Scatter plot - Species")
        @render_plotly
        def plot3():
            return px.scatter(p_df, y = "species")
        


with ui.sidebar(bg="#ca5ccd"):
    ui.h1("This is my sidebar - there are many like it but this one is mine")
    ui.hr()
    ui.a( "Github", href = "https://github.com/JSellinger", target= "_blank")

    ui.h2("Random stuff under here")
    with ui.card():
        ui.card_header("Settings")
        ui.input_dark_mode()
        ui.hr()
    with ui.card():
        ui.hr()
        ui.card_header("Stupid Fricking Inputs")
        ui.input_slider("n", "Slider Thing", 0, 10000,12)
        ui.input_selectize("s", "Selectize Things", [1, 2, 3, 4])
        ui.input_numeric("num", "Shiny numbers", 50)
        ui.input_checkbox_group("check", "Checkboxes?", ["Thing 1", "Thing 2", "Dr. Seuss", "Git"])
        
     
