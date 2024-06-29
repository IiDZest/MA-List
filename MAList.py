from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import * 

root = Tk()
root.title('Maintenance Service Agreement')
root.iconbitmap('C:/Users/Administrator/Documents/GUI for Maintenance/MA-List/db.ico')
root.geometry('1000x620')

# Search Record
def search_record():
    my_tree_view()

# Add Record Entry Boxes
search_frame = LabelFrame(root, text="Search Record")
search_frame.pack(fill="x", expand="yes", padx=20)

sr_label = Label(search_frame, text="Service Name:")
sr_label.grid(row=0, column=0, padx=10, pady=10)
sr_entry = Entry(search_frame, width="50")
sr_entry.grid(row=0, column=1, padx=10, pady=10)

sr_btn = Button(search_frame, text ="Search Record", command=search_record)
sr_btn.grid(row=0, column=2, padx=10, pady=10)

style = ttk.Style() # Add Some Style
style.theme_use('default') # Pick A Theme

# Config the Treeview Colors
style.configure("Treeview",
                background="#D3D3D3",
                foreground="black",
                rowheight=25,
                fieldbackground="#D3D3D3")

# Change Selected Color
style.map('Treeview',
          background=[('selected', "#347083")])
# Create a Treeview Frame
tree_frame = Frame(root)
tree_frame.pack(pady=10)

# Create a Treeview Scrollbar
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

# Create The Treeview
my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
my_tree.pack()

# Config the Scrollbar
tree_scroll.config(command=my_tree.yview)

# Define Our Columns
my_tree['columns'] = ("ID", "Service Name", "Year", "Start Date", "End Date", "Partner", "Contact")

# Format Our Columns
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("ID", anchor=CENTER, width=30)
my_tree.column("Service Name", anchor=W, width=280)
my_tree.column("Year", anchor=CENTER, width=50)
my_tree.column("Start Date", anchor=CENTER, width=80)
my_tree.column("End Date", anchor=CENTER, width=80)
my_tree.column("Partner", anchor=W, width=200)
my_tree.column("Contact", anchor=W, width=200)

# Create Headings
my_tree.heading("#0", text="", anchor=W)
my_tree.heading("ID", text="ID", anchor=CENTER)
my_tree.heading("Service Name", text="Service Name", anchor=CENTER)
my_tree.heading("Year", text="Year", anchor=CENTER)
my_tree.heading("Start Date", text="Start Date", anchor=CENTER)
my_tree.heading("End Date", text="End Date", anchor=CENTER)
my_tree.heading("Partner", text="Partner", anchor=CENTER)
my_tree.heading("Contact", text="Contact", anchor=CENTER)

# Create Striped Row Tags
my_tree.tag_configure('oddrow', background="white")
my_tree.tag_configure('evenrow', background="lightblue")

# Add our data to the screen
def my_tree_view():
    sr_service_name = sr_entry.get()
    if sr_service_name:
        data = search_ma_list(sr_service_name)
        # sr_entry.delete(0, END)
    else:
        data = view_ma_list() # Add ma_list to List

    global count
    count = 0
    my_tree.delete(*my_tree.get_children())

    for record in data:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6]), tags='evenrow',)
        else:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6]), tags='oddrow',)
        count += 1

my_tree_view()

# Add Record Entry Boxes
data_frame = LabelFrame(root, text="Record")
data_frame.pack(fill="x", expand="yes", padx=20)

id_label = Label(data_frame, text="ID:")
id_label.grid(row=0, column=0, padx=10, pady=10)
id_entry = Entry(data_frame)
id_entry.grid(row=0, column=1, padx=10, pady=10)

sn_label = Label(data_frame, text="Service Name:")
sn_label.grid(row=0, column=2, padx=10, pady=10)
sn_entry = Entry(data_frame, width="60")
sn_entry.grid(row=0, column=3, columnspan=3, padx=10, pady=10, sticky="W")

y_label = Label(data_frame, text="Year:")
y_label.grid(row=1, column=0, padx=10, pady=10)
y_entry = Entry(data_frame)
y_entry.grid(row=1, column=1, padx=10, pady=10)

sd_label = Label(data_frame, text="Start Date:")
sd_label.grid(row=1, column=2, padx=10, pady=10)
sd_entry = Entry(data_frame)
sd_entry.grid(row=1, column=3, padx=10, pady=10, sticky="W")

ed_label = Label(data_frame, text="End Date:")
ed_label.grid(row=1, column=4, padx=10, pady=10)
ed_entry = Entry(data_frame)
ed_entry.grid(row=1, column=5, padx=10, pady=10, sticky="E")

pt_label = Label(data_frame, text="Partner:")
pt_label.grid(row=2, column=0, padx=10, pady=10)
pt_entry = Entry(data_frame, width="35")
pt_entry.grid(row=2, column=1, columnspan=2, padx=10, pady=10, sticky="W")

ct_label = Label(data_frame, text="Contact:")
ct_label.grid(row=2, column=3, padx=10, pady=10)
ct_entry = Entry(data_frame, width="35")
ct_entry.grid(row=2, column=4, columnspan=2, padx=10, pady=10, sticky="W")

id_entry.config(state=DISABLED) # Disable ID Entry

# Add Record
def add_record():
    ID = id_entry.get()
    if ID:
        messagebox.showwarning(title="Warning", message="Please Reset Record!")
    else:
        service_name = sn_entry.get()
        year = y_entry.get()
        start_date = sd_entry.get()
        end_date = ed_entry.get()
        partner = pt_entry.get()
        contact = ct_entry.get()

        if service_name or year or start_date or end_date or partner or contact:
            insert_ma_list(f'{service_name}',f'{year}',f'{start_date}',f'{end_date}',f'{partner}',f'{contact}')

            messagebox.showinfo(title="Information", message="Add new record Done!")
            reset_record()
            my_tree_view()
        else:
            messagebox.showwarning(title="Warning", message="Please input data!")

# Update Record
def update_record():
    ID = id_entry.get()
    if ID:
        service_name = sn_entry.get()
        year = y_entry.get()
        start_date = sd_entry.get()
        end_date = ed_entry.get()
        partner = pt_entry.get()
        contact = ct_entry.get()

        update_ma_list(ID,"service_name",service_name)
        update_ma_list(ID,"year",year)
        update_ma_list(ID,"start_date",start_date)
        update_ma_list(ID,"end_date",end_date)
        update_ma_list(ID,"partner",partner)
        update_ma_list(ID,"contact",contact)

        messagebox.showinfo(title="Information", message="Update record Done!")
        reset_record()
        my_tree_view()
    else:
        messagebox.showwarning(title="Warning", message="Please select record!")

# Selected Record
def selected_record(e):
    # Clear Entry Boxes
    id_entry.config(state="normal")
    id_entry.delete(0, END)
    sn_entry.delete(0, END)
    y_entry.delete(0, END)
    sd_entry.delete(0, END)
    ed_entry.delete(0, END)
    pt_entry.delete(0, END)
    ct_entry.delete(0, END)

    # Grab record Number
    selected = my_tree.focus()
    # Grab record Values
    values = my_tree.item(selected, 'values')
    # print(values)

    # Output to Entry Boxes
    id_entry.insert(0, values[0])
    sn_entry.insert(0, values[1])
    y_entry.insert(0, values[2])
    sd_entry.insert(0, values[3])
    ed_entry.insert(0, values[4])
    pt_entry.insert(0, values[5])
    ct_entry.insert(0, values[6])
    id_entry.config(state=DISABLED) # Disable ID Entry

# Delete Record
def delete_record():
    ID = id_entry.get()
    if ID:
        msg = messagebox.askyesno(title="Confirm", message="Are you sure delete this item?")
        if msg:
            delete_ma_list(ID)
            messagebox.showinfo(title="Information", message="Delete record Done!")
            reset_record()
            my_tree_view()
        else:
            reset_record()
            my_tree_view()
    else:
        messagebox.showwarning(title="Warning", message="Please select record!")

# Reset Record
def reset_record():
    ID = id_entry.get()
    if ID:
        my_tree.selection_remove(my_tree.selection()[0]) # Deselect an item Treeview

    id_entry.config(state="normal")
    # Clear Entry Boxes
    sr_entry.delete(0, END)
    id_entry.delete(0, END)
    sn_entry.delete(0, END)
    y_entry.delete(0, END)
    sd_entry.delete(0, END)
    ed_entry.delete(0, END)
    pt_entry.delete(0, END)
    ct_entry.delete(0, END)
    id_entry.config(state=DISABLED) # Disable ID Entry
    my_tree_view()    

# Add Button
button_frame = LabelFrame(root, text="Commands")
button_frame.pack(fill="x", expand="yes", padx=20)

add_btn = Button(button_frame, text ="Add Record", command=add_record)
add_btn.grid(row=0, column=0, padx=10, pady=10)

update_btn = Button(button_frame, text ="Update Record", command=update_record)
update_btn.grid(row=0, column=1, padx=10, pady=10)

del_btn = Button(button_frame, text ="Delete Record", command=delete_record)
del_btn.grid(row=0, column=2, padx=10, pady=10)

reset_btn = Button(button_frame, text ="Reset Record", command=reset_record)
reset_btn.grid(row=0, column=6, padx=10, pady=10)

# Bind the treeview
my_tree.bind("<ButtonRelease-1>", selected_record)

root.mainloop()