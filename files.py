import dearpygui.dearpygui as dpg

dpg.create_context()

def callback(sender, app_data, user_data):
    print("Sender: ", sender)
    print("App Data: ", app_data)

with dpg.file_dialog(directory_selector=False, show=False, callback=callback, id="file_dialog_id", height=400, width=400):
    dpg.add_file_extension(".csv", color=(255, 0, 255, 255), custom_text="[header]")


with dpg.window(label="Tutorial", width=800, height=500):
    dpg.add_button(label="File Selector", callback=lambda: dpg.show_item("file_dialog_id"))

dpg.create_viewport(title='Custom Title', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()