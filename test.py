import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title='Custom Title', width=800, height=800)

def info():
    print(dpg.get_value("btn"))

with dpg.window(label="Example Window"):
    dpg.add_text("Hello, world")
    dpg.add_button(label="Save")
    dpg.add_input_text(label="string", default_value="Quick brown fox")
    dpg.add_slider_float(label="float", default_value=0.273, max_value=1)
    dpg.add_text("asdsadsa", color=[144, 12, 32])
    dpg.add_radio_button(tag="btn" ,items=['Minimizar', 'Maximizar'], default_value="Minimizar")
    dpg.add_button(label="get", callback=info)


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()