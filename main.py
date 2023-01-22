import time
import tkinter

import customtkinter
import os
from PIL import Image
from FireNext.NextDatabase import *


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        TEST_CONFIGURE = True
        TEST_REMOVING = False
        self.title("FireNext")
        self.geometry("1200x800+100+100")
        self.minsize(900, 500)

        # set grid layout
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Home Frame
        self.Home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color=("gray100", "gray10"))
        self.Home_frame.grid(row=1, column=0, sticky="nsew")
        # Next Database Item Frame
        self.Add_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.Read_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.Child_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.Query_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.Delete_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # create header frame
        self.header_frame = customtkinter.CTkFrame(self)
        self.header_frame.grid(row=0, column=0, sticky="nsew")
        self.header_frame.columnconfigure(6, weight=1)
        self.header_frame.rowconfigure(0, weight=1)

        self.NextDatabase_button = customtkinter.CTkButton(self.header_frame, corner_radius=0, height=40, width=100,
                                                           border_spacing=10,
                                                           text="NextDatabase",
                                                           fg_color="transparent", text_color=("gray10", "gray90"),
                                                           hover_color=("gray70", "gray30"), anchor="w",
                                                           font=("arial", 16)
                                                           , command=self.NextDatabaseBtnEvent)

        self.NextDatabase_button.grid(row=0, column=0, padx=(20, 0), pady=(1, 1), sticky="ew")

        self.NextTable_button = customtkinter.CTkButton(self.header_frame, corner_radius=0, height=40, width=100,
                                                        border_spacing=10,
                                                        text="NextTable",
                                                        fg_color="transparent", text_color=("gray10", "gray90"),
                                                        hover_color=("gray70", "gray30"), anchor="w",
                                                        font=("arial", 16), command=self.NextTableBtnEvent)

        self.NextTable_button.grid(row=0, column=1, padx=(0, 0), pady=(1, 1), sticky="ew")

        self.Converter_button = customtkinter.CTkButton(self.header_frame, corner_radius=0, height=40, width=100,
                                                        border_spacing=10,
                                                        text="Converter",
                                                        fg_color="transparent", text_color=("gray10", "gray90"),
                                                        hover_color=("gray70", "gray30"), anchor="w",
                                                        font=("arial", 16))
        self.Converter_button.grid(row=0, column=2, padx=(0, 0), pady=(1, 1), sticky="ew")

        self.Tutorials_button = customtkinter.CTkButton(self.header_frame, corner_radius=0, height=40, width=100,
                                                        border_spacing=10,
                                                        text="Tutorials",
                                                        fg_color="transparent", text_color=("gray10", "gray90"),
                                                        hover_color=("gray70", "gray30"), anchor="w",
                                                        font=("arial", 16))
        self.Tutorials_button.grid(row=0, column=3, padx=(0, 0), pady=(1, 1), sticky="ew")

        self.Settings_button = customtkinter.CTkButton(self.header_frame, corner_radius=0, height=40, width=100,
                                                       border_spacing=10,
                                                       text="Settings",
                                                       fg_color="transparent", text_color=("gray10", "gray90"),
                                                       hover_color=("gray70", "gray30"), anchor="w",
                                                       font=("arial", 16))
        self.Settings_button.grid(row=0, column=4, padx=(0, 0), pady=(1, 1), sticky="ew")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.header_frame, font=("arial", 15),
                                                                values=["Dark", "Light", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=0, column=7, padx=20, pady=1)
        self.change_appearance_mode_event("dark")

        # Create NextDatabase_frame
        self.NextDatabase_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.NextDatabase_frame.rowconfigure(5, weight=1)

        self.NextDatabase_add = customtkinter.CTkButton(master=self.NextDatabase_frame, text="Add", border_spacing=8,
                                                        corner_radius=0, font=("arial", 16), fg_color="transparent",
                                                        text_color=("gray10", "gray90"),
                                                        hover_color=("gray70", "gray30"),
                                                        anchor="w", width=123,
                                                        command=self.AddBtn)
        self.NextDatabase_add.grid(row=0, padx=(0, 0), pady=(0, 1))

        self.NextDatabase_read = customtkinter.CTkButton(master=self.NextDatabase_frame, text="Read",
                                                         corner_radius=0, font=("arial", 16), fg_color="transparent",
                                                         text_color=("gray10", "gray90"),
                                                         hover_color=("gray70", "gray30"),
                                                         anchor="w",
                                                         border_spacing=8, width=123, command=self.ReadBtn)
        self.NextDatabase_read.grid(row=1, padx=(0, 0), pady=(0, 1))

        self.NextDatabase_child = customtkinter.CTkButton(master=self.NextDatabase_frame, text="Has Child",
                                                          corner_radius=0, font=("arial", 16), fg_color="transparent",
                                                          text_color=("gray10", "gray90"),
                                                          hover_color=("gray70", "gray30"),
                                                          anchor="w",
                                                          border_spacing=8, width=123, command=self.ChildBtn)
        self.NextDatabase_child.grid(row=2, padx=(0, 0), pady=(0, 1))

        self.NextDatabase_query = customtkinter.CTkButton(master=self.NextDatabase_frame, text="Query",
                                                          corner_radius=0, font=("arial", 16), fg_color="transparent",
                                                          text_color=("gray10", "gray90"),
                                                          hover_color=("gray70", "gray30"),
                                                          anchor="w",
                                                          border_spacing=8, width=123, command=self.QueryBtn)
        self.NextDatabase_query.grid(row=3, padx=(0, 0), pady=(0, 1))

        self.NextDatabase_delete = customtkinter.CTkButton(master=self.NextDatabase_frame, text="Delete",
                                                           corner_radius=0, font=("arial", 16), fg_color="transparent",
                                                           text_color=("gray10", "gray90"),
                                                           hover_color=("gray70", "gray30"),
                                                           anchor="w",
                                                           border_spacing=8, width=123, command=self.DeleteBtn)
        self.NextDatabase_delete.grid(row=4, padx=(0, 0), pady=(0, 1))

        # Next Database Add Interface
        self.Add_frame.grid_columnconfigure(1, weight=1)
        self.Add_frame.grid_rowconfigure(1, weight=1)

        self.txt_var = tkinter.StringVar(value="")
        self.Add_Input = customtkinter.CTkEntry(master=self.Add_frame, placeholder_text="Parent>Child>ValueChild:Value",
                                                height=30,
                                                font=("arial", 18), )
        self.Add_Input.grid(row=0, column=0, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")
        self.NextDatabase_addBtn = customtkinter.CTkButton(master=self.Add_frame, text="Add", font=("arial", 18),
                                                           width=120, height=30, command=self.addBtn)
        self.NextDatabase_addBtn.grid(row=0, column=2, padx=(20, 20), pady=(0, 0))

        self.NextDatabase_add_result = customtkinter.CTkTextbox(master=self.Add_frame, wrap="none", corner_radius=0,
                                                                border_width=0, font=("arial", 18))
        self.NextDatabase_add_result.grid(row=1, column=1, columnspan=2, padx=(20, 20), pady=(0, 20), sticky="nsew")
        self.NextDatabase_add_result.configure(state='disabled')

        # Next Database Read Interface

        self.Read_frame.grid_columnconfigure(1, weight=1)
        self.Read_frame.grid_rowconfigure(1, weight=1)

        self.Read_Input = customtkinter.CTkEntry(master=self.Read_frame,
                                                 placeholder_text="Parent or Parent>Child or Parent>Child>ValueChild:",
                                                 height=30,
                                                 font=("arial", 18))
        self.Read_Input.grid(row=0, column=0, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")
        self.NextDatabase_readBtn = customtkinter.CTkButton(master=self.Read_frame, text="Read", font=("arial", 18),
                                                            width=120, height=30, command=self.readBtn)
        self.NextDatabase_readBtn.grid(row=0, column=2, padx=(20, 20), pady=(0, 0))

        self.NextDatabase_read_result = customtkinter.CTkTextbox(master=self.Read_frame, wrap="none", corner_radius=0,
                                                                 border_width=0, font=("arial", 18))
        self.NextDatabase_read_result.grid(row=1, column=1, columnspan=2, padx=(20, 20), pady=(0, 20), sticky="nsew")
        self.NextDatabase_read_result.configure(state='disabled')

        # Next Database Has Child Interface

        self.Child_frame.grid_columnconfigure(1, weight=1)
        self.Child_frame.grid_rowconfigure(1, weight=1)

        self.Child_Input = customtkinter.CTkEntry(master=self.Child_frame,
                                                  placeholder_text="Parent or Parent>Child or Parent>Child>ValueChild:",
                                                  height=30,
                                                  font=("arial", 18))
        self.Child_Input.grid(row=0, column=0, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")
        self.NextDatabase_childBtn = customtkinter.CTkButton(master=self.Child_frame, text="Has Child",
                                                             font=("arial", 18),
                                                             width=120, height=30, command=self.childBtn)
        self.NextDatabase_childBtn.grid(row=0, column=2, padx=(20, 20), pady=(0, 0))

        self.NextDatabase_child_result = customtkinter.CTkTextbox(master=self.Child_frame, wrap="none", corner_radius=0,
                                                                  border_width=0, font=("arial", 18))
        self.NextDatabase_child_result.grid(row=1, column=1, columnspan=2, padx=(20, 20), pady=(0, 20), sticky="nsew")
        self.NextDatabase_child_result.configure(state='disabled')

        # Next Database Query Interface
        self.Query_frame.grid_columnconfigure(1, weight=1)
        self.Query_frame.grid_rowconfigure(1, weight=1)

        self.txt_var = tkinter.StringVar(value="")
        self.Query_Input = customtkinter.CTkEntry(master=self.Query_frame, placeholder_text="Parent>ValueChild:",
                                                  height=30,
                                                  font=("arial", 18))
        self.Query_Input.grid(row=0, column=0, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")
        self.NextDatabase_queryBtn = customtkinter.CTkButton(master=self.Query_frame, text="Query",
                                                             font=("arial", 18),
                                                             width=120, height=30, command=self.queryBtn)
        self.NextDatabase_queryBtn.grid(row=0, column=2, padx=(20, 20), pady=(0, 0))

        self.NextDatabase_query_result = customtkinter.CTkTextbox(master=self.Query_frame, wrap="none", corner_radius=0,
                                                                  border_width=0, font=("arial", 18))
        self.NextDatabase_query_result.grid(row=1, column=1, columnspan=2, padx=(20, 20), pady=(0, 20), sticky="nsew")
        self.NextDatabase_query_result.configure(state='disabled')

        # Next Database Delete Interface
        self.Delete_frame.grid_columnconfigure(1, weight=1)
        self.Delete_frame.grid_rowconfigure(1, weight=1)

        self.Delete_Input = customtkinter.CTkEntry(master=self.Delete_frame,
                                                   placeholder_text="Parent or Parent>Child or Parent>Child>ValueChild:",
                                                   height=30,
                                                   font=("arial", 18))
        self.Delete_Input.grid(row=0, column=0, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")
        self.NextDatabase_deleteBtn = customtkinter.CTkButton(master=self.Delete_frame, text="Delete",
                                                              font=("arial", 18),
                                                              width=120, height=30, command=self.deleteBtn)
        self.NextDatabase_deleteBtn.grid(row=0, column=2, padx=(20, 20), pady=(0, 0))

        self.NextDatabase_delete_result = customtkinter.CTkTextbox(master=self.Delete_frame, wrap="none",
                                                                   corner_radius=0,
                                                                   border_width=0, font=("arial", 18))
        self.NextDatabase_delete_result.grid(row=1, column=1, columnspan=2, padx=(20, 20), pady=(0, 20), sticky="nsew")
        self.NextDatabase_delete_result.configure(state='disabled')

        # Next Database <Enter> Position
        self.NextDatabase_button.bind("<Enter>", self.onPositionNextDatabase)
        self.Add_frame.bind("<Enter>", self.onLeave)
        self.Add_Input.bind("<Enter>", self.onLeave)
        self.NextDatabase_add_result.bind("<Enter>", self.onLeave)

        self.Read_frame.bind("<Enter>", self.onLeave)
        self.Read_Input.bind("<Enter>", self.onLeave)
        self.NextDatabase_read_result.bind("<Enter>", self.onLeave)

        self.Child_frame.bind("<Enter>", self.onLeave)
        self.Child_Input.bind("<Enter>", self.onLeave)
        self.NextDatabase_child_result.bind("<Enter>", self.onLeave)

        self.Query_frame.bind("<Enter>", self.onLeave)
        self.Query_Input.bind("<Enter>", self.onLeave)
        self.NextDatabase_query_result.bind("<Enter>", self.onLeave)

        self.Delete_frame.bind("<Enter>", self.onLeave)
        self.Delete_Input.bind("<Enter>", self.onLeave)
        self.NextDatabase_delete_result.bind("<Enter>", self.onLeave)

        # Create NextTable_frame
        self.NextTable_frame = customtkinter.CTkFrame(master=self, fg_color="transparent")
        self.NextTable_frame.rowconfigure(16, weight=1)

        self.Create_Table = customtkinter.CTkButton(master=self.NextTable_frame,
                                                    text="Create Table",
                                                    corner_radius=0, font=("arial", 16),
                                                    fg_color="transparent",
                                                    text_color=("gray10", "gray90"),
                                                    hover_color=("gray70", "gray30"),
                                                    anchor="w",
                                                    border_spacing=8, width=200)
        self.Create_Table.grid(row=0, padx=(0, 0), pady=(0, 1))

        self.Read_Table = customtkinter.CTkButton(master=self.NextTable_frame,
                                                  text="Read Table",
                                                  corner_radius=0, font=("arial", 16),
                                                  fg_color="transparent",
                                                  text_color=("gray10", "gray90"),
                                                  hover_color=("gray70", "gray30"),
                                                  anchor="w",
                                                  border_spacing=8, width=200)
        self.Read_Table.grid(row=1, padx=(0, 0), pady=(0, 1))

        self.Delete_Table = customtkinter.CTkButton(master=self.NextTable_frame, text="Delete Table",
                                                    corner_radius=0, font=("arial", 16),
                                                    fg_color="transparent",
                                                    text_color=("gray10", "gray90"),
                                                    hover_color=("gray70", "gray30"),
                                                    anchor="w",
                                                    border_spacing=8, width=200)
        self.Delete_Table.grid(row=2, padx=(0, 0), pady=(0, 1))

        self.Add_Col_Name = customtkinter.CTkButton(master=self.NextTable_frame, text="Add Column Name",
                                                    corner_radius=0, font=("arial", 16),
                                                    fg_color="transparent",
                                                    text_color=("gray10", "gray90"),
                                                    hover_color=("gray70", "gray30"),
                                                    anchor="w",
                                                    border_spacing=8, width=200)
        self.Add_Col_Name.grid(row=3, padx=(0, 0), pady=(0, 1))

        self.Read_Col_Name = customtkinter.CTkButton(master=self.NextTable_frame, text="Read Column Name",
                                                     corner_radius=0, font=("arial", 16),
                                                     fg_color="transparent",
                                                     text_color=("gray10", "gray90"),
                                                     hover_color=("gray70", "gray30"),
                                                     anchor="w",
                                                     border_spacing=8, width=200)
        self.Read_Col_Name.grid(row=4, padx=(0, 0), pady=(0, 1))

        self.Update_Col_Name = customtkinter.CTkButton(master=self.NextTable_frame, text="Update Column Name",
                                                       corner_radius=0, font=("arial", 16),
                                                       fg_color="transparent",
                                                       text_color=("gray10", "gray90"),
                                                       hover_color=("gray70", "gray30"),
                                                       anchor="w",
                                                       border_spacing=8, width=200)
        self.Update_Col_Name.grid(row=5, padx=(0, 0), pady=(0, 1))

        self.Delete_Col_Name = customtkinter.CTkButton(master=self.NextTable_frame, text="Delete Column Name",
                                                       corner_radius=0, font=("arial", 16),
                                                       fg_color="transparent",
                                                       text_color=("gray10", "gray90"),
                                                       hover_color=("gray70", "gray30"),
                                                       anchor="w",
                                                       border_spacing=8, width=200)
        self.Delete_Col_Name.grid(row=6, padx=(0, 0), pady=(0, 1))

        self.Add_Data = customtkinter.CTkButton(master=self.NextTable_frame, text="Add Data",
                                                corner_radius=0, font=("arial", 16),
                                                fg_color="transparent",
                                                text_color=("gray10", "gray90"),
                                                hover_color=("gray70", "gray30"),
                                                anchor="w",
                                                border_spacing=8, width=200)
        self.Add_Data.grid(row=7, padx=(0, 0), pady=(0, 1))

        self.Search_Data = customtkinter.CTkButton(master=self.NextTable_frame, text="Search Data",
                                                   corner_radius=0, font=("arial", 16),
                                                   fg_color="transparent",
                                                   text_color=("gray10", "gray90"),
                                                   hover_color=("gray70", "gray30"),
                                                   anchor="w",
                                                   border_spacing=8, width=200)
        self.Search_Data.grid(row=8, padx=(0, 0), pady=(0, 1))

        self.Update_Data = customtkinter.CTkButton(master=self.NextTable_frame, text="Update Data",
                                                   corner_radius=0, font=("arial", 16),
                                                   fg_color="transparent",
                                                   text_color=("gray10", "gray90"),
                                                   hover_color=("gray70", "gray30"),
                                                   anchor="w",
                                                   border_spacing=8, width=200)
        self.Update_Data.grid(row=9, padx=(0, 0), pady=(0, 1))

        self.Delete_Data = customtkinter.CTkButton(master=self.NextTable_frame, text="Delete Data",
                                                   corner_radius=0, font=("arial", 16),
                                                   fg_color="transparent",
                                                   text_color=("gray10", "gray90"),
                                                   hover_color=("gray70", "gray30"),
                                                   anchor="w",
                                                   border_spacing=8, width=200)
        self.Delete_Data.grid(row=10, padx=(0, 0), pady=(0, 1))

        self.Search_Row_Data = customtkinter.CTkButton(master=self.NextTable_frame, text="Search Row Data",
                                                       corner_radius=0, font=("arial", 16),
                                                       fg_color="transparent",
                                                       text_color=("gray10", "gray90"),
                                                       hover_color=("gray70", "gray30"),
                                                       anchor="w",
                                                       border_spacing=8, width=200)
        self.Search_Row_Data.grid(row=11, padx=(0, 0), pady=(0, 1))

        self.Update_Row_Data = customtkinter.CTkButton(master=self.NextTable_frame, text="Update Row Data",
                                                       corner_radius=0, font=("arial", 16),
                                                       fg_color="transparent",
                                                       text_color=("gray10", "gray90"),
                                                       hover_color=("gray70", "gray30"),
                                                       anchor="w",
                                                       border_spacing=8, width=200)
        self.Update_Row_Data.grid(row=12, padx=(0, 0), pady=(0, 1))

        self.Delete_Row = customtkinter.CTkButton(master=self.NextTable_frame, text="Delete Row",
                                                  corner_radius=0, font=("arial", 16),
                                                  fg_color="transparent",
                                                  text_color=("gray10", "gray90"),
                                                  hover_color=("gray70", "gray30"),
                                                  anchor="w",
                                                  border_spacing=8, width=200)
        self.Delete_Row.grid(row=13, padx=(0, 0), pady=(0, 1))

        self.Search_Col_Data = customtkinter.CTkButton(master=self.NextTable_frame, text="Search Column Data",
                                                       corner_radius=0, font=("arial", 16),
                                                       fg_color="transparent",
                                                       text_color=("gray10", "gray90"),
                                                       hover_color=("gray70", "gray30"),
                                                       anchor="w",
                                                       border_spacing=8, width=200)
        self.Search_Col_Data.grid(row=14, padx=(0, 0), pady=(0, 1))

        self.Delete_Col = customtkinter.CTkButton(master=self.NextTable_frame, text="Delete Column",
                                                  corner_radius=0, font=("arial", 16),
                                                  fg_color="transparent",
                                                  text_color=("gray10", "gray90"),
                                                  hover_color=("gray70", "gray30"),
                                                  anchor="w",
                                                  border_spacing=8, width=200)

        self.Delete_Col.grid(row=15, padx=(0, 0), pady=(0, 1))

        # Next Table <Enter Position>
        self.NextTable_button.bind("<Enter>", self.onPositionNextTable)

        self.Home_frame.bind("<Enter>", self.onLeave)


    def onPositionNextDatabase(self, name):
        self.select_frame_by_name("NextDatabase")

    def onPositionNextTable(self, name):
        self.select_frame_by_name("NextTable")

    def onLeave(self, name):
        self.select_frame_by_name("")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.NextDatabase_button.configure(fg_color=("gray75", "gray25") if name == "NextDatabase" else "transparent")
        self.NextTable_button.configure(fg_color=("gray75", "gray25") if name == "NextTable" else "transparent")
        # show selected frame
        if name == "NextDatabase":
            self.NextDatabase_frame.place(x=20, y=42)
        else:
            self.NextDatabase_frame.grid()
            self.NextDatabase_frame.grid_forget()
        if name == "NextTable":
            self.NextTable_frame.place(x=142, y=42)
        else:
            self.NextTable_frame.grid()
            self.NextTable_frame.grid_forget()

    def NextDatabaseBtnEvent(self):
        self.select_frame_by_name("NextDatabase")

    def NextTableBtnEvent(self):
        self.select_frame_by_name("NextTable")

    def databaseCheckBtn(self, name):

        if name == "add":
            returnValue = NextDatabase.add(self.Add_Input.get())
            self.NextDatabase_add_result.configure(state='normal')
            self.NextDatabase_add_result.delete("1.0", "end")
            if returnValue == "true":
                self.NextDatabase_add_result.insert("0.0", "Successful!")
                self.NextDatabase_add_result.configure(state='disabled')
            else:
                self.NextDatabase_add_result.insert("0.0", returnValue)
                self.NextDatabase_add_result.configure(state='disabled')
        elif name == "read":
            returnValue = NextDatabase.read(self.Read_Input.get())
            self.NextDatabase_read_result.configure(state='normal')
            self.NextDatabase_read_result.delete("1.0", "end")
            self.NextDatabase_read_result.insert("0.0", returnValue)
            self.NextDatabase_read_result.configure(state='disabled')

        elif name == "child":
            returnValue = NextDatabase.hasChild(self.Child_Input.get())
            self.NextDatabase_child_result.configure(state='normal')
            self.NextDatabase_child_result.delete("1.0", "end")
            self.NextDatabase_child_result.insert("0.0", returnValue)
            self.NextDatabase_child_result.configure(state='disabled')

        elif name == "query":
            returnValue = NextDatabase.query(self.Query_Input.get())
            self.NextDatabase_query_result.configure(state='normal')
            self.NextDatabase_query_result.delete("1.0", "end")
            self.NextDatabase_query_result.insert("0.0", returnValue)
            self.NextDatabase_query_result.configure(state='disabled')

        elif name == "delete":
            returnValue = NextDatabase.delete(self.Delete_Input.get())
            self.NextDatabase_delete_result.configure(state='normal')
            self.NextDatabase_delete_result.delete("1.0", "end")
            if returnValue == "true":
                self.NextDatabase_delete_result.insert("0.0", "Successful!")
                self.NextDatabase_delete_result.configure(state='disabled')
            else:
                self.NextDatabase_delete_result.insert("0.0", returnValue)
                self.NextDatabase_delete_result.configure(state='disabled')

    def category_selection(self, name):
        if name == "Add":
            self.select_frame_by_name("")
            self.Add_frame.grid(row=1, column=0, sticky="nsew")
        else:
            self.Add_frame.grid_forget()
        if name == "Read":
            self.select_frame_by_name("")
            self.Read_frame.grid(row=1, column=0, sticky="nsew")
        else:
            self.Read_frame.grid_forget()
        if name == "Child":
            self.select_frame_by_name("")
            self.Child_frame.grid(row=1, column=0, sticky="nsew")
        else:
            self.Child_frame.grid_forget()
        if name == "Query":
            self.select_frame_by_name("")
            self.Query_frame.grid(row=1, column=0, sticky="nsew")
        else:
            self.Query_frame.grid_forget()
        if name == "Delete":
            self.select_frame_by_name("")
            self.Delete_frame.grid(row=1, column=0, sticky="nsew")
        else:
            self.Delete_frame.grid_forget()

    def AddBtn(self):
        self.category_selection("Add")

    def addBtn(self):
        if self.Add_Input.get() != "":
            self.databaseCheckBtn("add")

    def ReadBtn(self):
        self.category_selection("Read")

    def readBtn(self):
        if self.Read_Input.get() != "":
            self.databaseCheckBtn("read")

    def ChildBtn(self):
        self.category_selection("Child")

    def childBtn(self):
        if self.Child_Input.get() != "":
            self.databaseCheckBtn("child")

    def QueryBtn(self):
        self.category_selection("Query")

    def queryBtn(self):
        if self.Query_Input.get() != "":
            self.databaseCheckBtn("query")

    def DeleteBtn(self):
        self.category_selection("Delete")

    def deleteBtn(self):
        if self.Delete_Input.get() != "":
            self.databaseCheckBtn("delete")


if __name__ == "__main__":
    app = App()
    app.mainloop()
