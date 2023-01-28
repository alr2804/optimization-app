import dearpygui.dearpygui as dpg


def create_sol_table(tab, optimal):
    # print("create sol table")
    # print(tab)
    with dpg.window():
        with dpg.table():
        #column names
            dpg.add_table_column(label=" ")
            for i in range(len(tab[0])):
                dpg.add_table_column(label=f"Tarea {i+1}")

            for i in range(len(tab)):
                tmp = []
                with dpg.table_row():
                    dpg.add_button(label=f"Server {i+1}")
                    for j in range(len(tab[0])):
                        # dpg.add_text(f"{i} {j}")
                        color = [255, 255, 255]
                        if(tab[i][j] == 1): color = [144, 12, 32]
                        dpg.add_text(f" {dpg.get_value(inputarr[i][j])}", color=color)
        dpg.add_text(f"Optimal total:  {optimal}")