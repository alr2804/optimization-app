import dearpygui.dearpygui as dpg

#always create context at the start
dpg.create_context()

dpg.set_global_font_scale(1.8)

with dpg.window(tag="Primary Window"):
    dpg.add_text("Hello, world")
    dpg.add_button(label="Save")
    dpg.add_input_text(label="string", default_value="Quick brown fox")
    dpg.add_slider_float(label="float", default_value=0.273, max_value=1)

#window size and tittle
dpg.create_viewport(title='Custom Title', width=1200, height=600)


dpg.setup_dearpygui()
dpg.show_viewport()

#full screen with the tag name of the window
dpg.set_primary_window("Primary Window", True)


#here can be the render loop
dpg.start_dearpygui()



dpg.destroy_context()