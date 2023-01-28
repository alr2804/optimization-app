import dearpygui.dearpygui as dpg
import algorithm as al

dpg.create_context()

#general options
dpg.set_global_font_scale(1.8)

#global variables
inputarr = [] #array of all the values on the table


#functions

#create a solution table, tab = solution array, optimal (bool) = max or min   
def create_solution_table(tab, optimal):
    #create new window
    # width=len(tab[0])* 100, horizontal_scrollbar=True,
    with dpg.window():
        with dpg.table(
            policy=dpg.mvTable_SizingFixedFit,
            # resizable=True,
            no_host_extendX=True,
            borders_innerV=True,
            borders_outerV=True,
            borders_outerH=True,
            scrollX=True,
            no_keep_columns_visible=False,
            freeze_columns=1,
            freeze_rows=1,
            # width=900,
            # height=500,
            scrollY=True, 
            ):
            #column names
            dpg.add_table_column(label=" ", width=700, width_fixed=True, no_hide=True)
            for i in range(len(tab[0])):
                dpg.add_table_column(label=f" {i+1}", width=700, width_fixed=True)
            
            #row iterations
            for i in range(len(tab)):
                tmp = []
                with dpg.table_row():
                    dpg.add_button(label=f" {i+1}" )
                    for j in range(len(tab[0])):
                        color = [255, 255, 255] #white color
                        if(tab[i][j] == 1): color = [144, 12, 32] #color change if
                        dpg.add_text(f" {dpg.get_value(inputarr[i][j])}", color=color)
        dpg.add_text(f"Optimal total:  {optimal}")
                        
            

def get_elements():
    print("----------")
    a = []
    for line in inputarr:
        tmp = []
        for e in line:
            print(dpg.get_value(e), end=" ")
            tmp.append(dpg.get_value(e))
        print(" ")
        a.append(tmp)

    print(a)
    print("............")
    #get info of the radius button
    max = dpg.get_value("radio_btn") == "Minimizar"
    print(max)

    result = al.solver(a, max, "aaaa")
    print(result[0])
    create_solution_table(result[0], result[1])


def create_table():
    global inputarr
    user_data =  [dpg.get_value("in1") , dpg.get_value("in2")]
    
    dpg.delete_item("testtable")
    dpg.delete_item("testbtn")
    # dpg.add_table(tag="testtable")

    #create a double array and init on 0s
    inputarr = []
    arr = []
    maxsize = min(1200, user_data[0]*130 )

    with dpg.table(
        policy=dpg.mvTable_SizingFixedFit,
        # resizable=True,
        no_host_extendX=True,
        borders_innerV=True,
        borders_outerV=True,
        borders_outerH=True,
        scrollX=True,
        no_keep_columns_visible=False,
        freeze_columns=1,
        freeze_rows=1,
        width=maxsize,
        # height=500,
        scrollY=True, 
        tag="testtable",parent="window",):
        #column names
        dpg.add_table_column(label=" ")
        for i in range(user_data[0]):
            dpg.add_table_column(label=f"Tarea {i+1}")
        
        #info

        for j in range(user_data[1]):
            tmp = []
            with dpg.table_row():
                dpg.add_button(label=f"Server {j+1}")
                for i in range(user_data[0]):
                    # dpg.add_text(f"{i} {j}")
                    x = dpg.add_input_int(step=False)
                    tmp.append(x)
                inputarr.append(tmp)
        
 
    # dpg.add_spacer()
    dpg.add_button(label="Calcular", tag="testbtn", parent="window", callback=get_elements)
    #after the button is clicked, get the values from all the inputs to the array
    #and execute the function



# main window
with dpg.window(label="Tutorial", tag="window"):
    
    dpg.add_text("Obejtivo de la optimizacion")
    dpg.add_radio_button(tag="radio_btn" ,items=['Minimizar', 'Maximizar'], default_value="Minimizar")
    dpg.add_separator()
    dpg.add_text("Cantidad de tareas: ")
    input1 = dpg.add_input_int(tag="in1", default_value=4, min_value=1, min_clamped=True, max_value=60, max_clamped=True)
    dpg.add_text("Cantidad de servidores: ")
    input2 = dpg.add_input_int(tag = "in2",default_value=4, min_value=1, min_clamped=True, max_value=60, max_clamped=True)

    dpg.add_button(label="Crear tabla", callback=create_table)
    dpg.add_spacer()

    create_table()


# dpg.show_item_registry()

dpg.create_viewport(title='Custom Title', width=1400, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()

#full screen with the tag name of the window
dpg.set_primary_window("window", True)


dpg.start_dearpygui()
dpg.destroy_context()