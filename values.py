import dearpygui.dearpygui as dpg

dpg.create_context()

def print_value(sender):
    print(dpg.get_value(sender))

def create_table(sender, app_data, user_data):
    #every item should have a tag to delete when create a new table
    print(f"sender is: {sender}")
    print(f"app_data is: {app_data}")
    print(f"user_data is: {user_data}")
    print("-------------------")
    print(dpg.get_value(input1))

with dpg.window(width=300):
    input_txt1 = dpg.add_input_text()
    # The value for input_text2 will have a starting value
    # of "This is a default value!"
    input_txt2 = dpg.add_input_text(
        label="InputTxt2",
        default_value="This is a default value!",
        callback=print_value
    )

    slider_float1 = dpg.add_slider_float()
    # The slider for slider_float2 will have a starting value
    # of 50.0.
    slider_float2 = dpg.add_slider_float(
        label="SliderFloat2",
        default_value=50.0,
        callback=print_value
    )
    input1 = dpg.add_input_int(tag="in1", default_value=1, min_value=1, min_clamped=True, max_value=60, max_clamped=True)
    # print(f"input1:  {type(dpg.get_value(input1))}")

    dpg.add_button(
        label="Crear tabla", 
        callback = create_table, 
        user_data= [],
         )

    dpg.set_item_callback(input_txt1, print_value)
    dpg.set_item_callback(slider_float1, print_value)

    print(dpg.get_value(input_txt1))
    print(dpg.get_value(input_txt2))
    print(dpg.get_value(slider_float1))
    print(dpg.get_value(slider_float2))

dpg.create_viewport(title='Custom Title', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()