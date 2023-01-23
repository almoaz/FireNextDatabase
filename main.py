import time
import tkinter

import customtkinter
import os
from PIL import Image
from FireNext.NextDatabase import *
from FireNext.NextTable import *


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

        # Next Table Item Frame
        self.Create_Table_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.Read_Table_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.Delete_Table_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.Add_Col_Name_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.Read_Col_Name_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.Update_Col_Name_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.Delete_Col_Name_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.Add_Data_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.Search_Data_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.Update_Data_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.Delete_Data_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.Search_Row_Data_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.Update_Row_Data_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.Delete_Row_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.Search_Column_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.Delete_Column_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # Converter Item Frame
        self.NextTable_To_NextDatabase_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.NextTable_To_Excel_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.Excel_To_NextTable_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.NextTable_To_Txt_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.NextDatabase_To_Txt_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

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
                                                           font=("arial", 16),
                                                           command=self.NextDatabaseBtnEvent)

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
                                                        font=("arial", 16), command=self.ConverterBtnEvent)
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
                                                font=("arial", 18))
        self.Add_Input.grid(row=0, column=0, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.NextDatabase_addBtn = customtkinter.CTkButton(master=self.Add_frame, text="Add", font=("arial", 18),
                                                           width=120, height=30, command=self.addBtn)
        self.NextDatabase_addBtn.grid(row=0, column=2, padx=(20, 20), pady=(0, 0))

        self.NextDatabase_add_result = customtkinter.CTkTextbox(master=self.Add_frame, wrap="none", corner_radius=0,
                                                                border_width=0, font=("Terminal", 18))
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
                                                                 border_width=0, font=("Terminal", 18))
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
                                                                  border_width=0, font=("Terminal", 18))
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
                                                                  border_width=0, font=("Terminal", 18))
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
                                                                   border_width=0, font=("Terminal", 18))
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
                                                    anchor="w", border_spacing=8, width=200,
                                                    command=self.Create_Table_Btn)
        self.Create_Table.grid(row=0, padx=(0, 0), pady=(0, 1))

        self.Read_Table = customtkinter.CTkButton(master=self.NextTable_frame,
                                                  text="Read Table",
                                                  corner_radius=0, font=("arial", 16),
                                                  fg_color="transparent",
                                                  text_color=("gray10", "gray90"),
                                                  hover_color=("gray70", "gray30"),
                                                  anchor="w", border_spacing=8, width=200,
                                                  command=self.Read_Table_Btn)
        self.Read_Table.grid(row=1, padx=(0, 0), pady=(0, 1))

        self.Delete_Table = customtkinter.CTkButton(master=self.NextTable_frame, text="Delete Table",
                                                    corner_radius=0, font=("arial", 16),
                                                    fg_color="transparent",
                                                    text_color=("gray10", "gray90"),
                                                    hover_color=("gray70", "gray30"),
                                                    anchor="w", border_spacing=8, width=200,
                                                    command=self.Delete_Table_Btn)
        self.Delete_Table.grid(row=2, padx=(0, 0), pady=(0, 1))

        self.Add_Col_Name = customtkinter.CTkButton(master=self.NextTable_frame, text="Add Column Name",
                                                    corner_radius=0, font=("arial", 16),
                                                    fg_color="transparent",
                                                    text_color=("gray10", "gray90"),
                                                    hover_color=("gray70", "gray30"),
                                                    anchor="w", border_spacing=8, width=200,
                                                    command=self.Add_Col_Name_Btn)
        self.Add_Col_Name.grid(row=3, padx=(0, 0), pady=(0, 1))

        self.Read_Col_Name = customtkinter.CTkButton(master=self.NextTable_frame, text="Read Column Name",
                                                     corner_radius=0, font=("arial", 16),
                                                     fg_color="transparent",
                                                     text_color=("gray10", "gray90"),
                                                     hover_color=("gray70", "gray30"),
                                                     anchor="w", border_spacing=8, width=200,
                                                     command=self.Read_Col_Name_Btn)
        self.Read_Col_Name.grid(row=4, padx=(0, 0), pady=(0, 1))

        self.Update_Col_Name = customtkinter.CTkButton(master=self.NextTable_frame, text="Update Column Name",
                                                       corner_radius=0, font=("arial", 16),
                                                       fg_color="transparent",
                                                       text_color=("gray10", "gray90"),
                                                       hover_color=("gray70", "gray30"),
                                                       anchor="w", border_spacing=8, width=200,
                                                       command=self.Update_Col_Name_Btn)
        self.Update_Col_Name.grid(row=5, padx=(0, 0), pady=(0, 1))

        self.Delete_Col_Name = customtkinter.CTkButton(master=self.NextTable_frame, text="Delete Column Name",
                                                       corner_radius=0, font=("arial", 16),
                                                       fg_color="transparent",
                                                       text_color=("gray10", "gray90"),
                                                       hover_color=("gray70", "gray30"),
                                                       anchor="w", border_spacing=8, width=200,
                                                       command=self.Delete_Col_Name_Btn)
        self.Delete_Col_Name.grid(row=6, padx=(0, 0), pady=(0, 1))

        self.Add_Data = customtkinter.CTkButton(master=self.NextTable_frame, text="Add Data",
                                                corner_radius=0, font=("arial", 16),
                                                fg_color="transparent",
                                                text_color=("gray10", "gray90"),
                                                hover_color=("gray70", "gray30"),
                                                anchor="w", border_spacing=8, width=200,
                                                command=self.Add_Data_Btn)
        self.Add_Data.grid(row=7, padx=(0, 0), pady=(0, 1))

        self.Search_Data = customtkinter.CTkButton(master=self.NextTable_frame, text="Search Data",
                                                   corner_radius=0, font=("arial", 16),
                                                   fg_color="transparent",
                                                   text_color=("gray10", "gray90"),
                                                   hover_color=("gray70", "gray30"),
                                                   anchor="w", border_spacing=8, width=200,
                                                   command=self.Search_Data_Btn)
        self.Search_Data.grid(row=8, padx=(0, 0), pady=(0, 1))

        self.Update_Data = customtkinter.CTkButton(master=self.NextTable_frame, text="Update Data",
                                                   corner_radius=0, font=("arial", 16),
                                                   fg_color="transparent",
                                                   text_color=("gray10", "gray90"),
                                                   hover_color=("gray70", "gray30"),
                                                   anchor="w", border_spacing=8, width=200,
                                                   command=self.Update_Data_Btn)
        self.Update_Data.grid(row=9, padx=(0, 0), pady=(0, 1))

        self.Delete_Data = customtkinter.CTkButton(master=self.NextTable_frame, text="Delete Data",
                                                   corner_radius=0, font=("arial", 16),
                                                   fg_color="transparent",
                                                   text_color=("gray10", "gray90"),
                                                   hover_color=("gray70", "gray30"),
                                                   anchor="w", border_spacing=8, width=200,
                                                   command=self.Delete_Data_Btn)
        self.Delete_Data.grid(row=10, padx=(0, 0), pady=(0, 1))

        self.Search_Row = customtkinter.CTkButton(master=self.NextTable_frame, text="Search Row Data",
                                                  corner_radius=0, font=("arial", 16),
                                                  fg_color="transparent",
                                                  text_color=("gray10", "gray90"),
                                                  hover_color=("gray70", "gray30"),
                                                  anchor="w", border_spacing=8, width=200,
                                                  command=self.Search_Row_Btn)
        self.Search_Row.grid(row=11, padx=(0, 0), pady=(0, 1))

        self.Update_Row = customtkinter.CTkButton(master=self.NextTable_frame, text="Update Row Data",
                                                  corner_radius=0, font=("arial", 16),
                                                  fg_color="transparent",
                                                  text_color=("gray10", "gray90"),
                                                  hover_color=("gray70", "gray30"),
                                                  anchor="w", border_spacing=8, width=200,
                                                  command=self.Update_Row_Btn)
        self.Update_Row.grid(row=12, padx=(0, 0), pady=(0, 1))

        self.Delete_Row = customtkinter.CTkButton(master=self.NextTable_frame, text="Delete Row",
                                                  corner_radius=0, font=("arial", 16),
                                                  fg_color="transparent",
                                                  text_color=("gray10", "gray90"),
                                                  hover_color=("gray70", "gray30"),
                                                  anchor="w", border_spacing=8, width=200,
                                                  command=self.Delete_Row_Btn)
        self.Delete_Row.grid(row=13, padx=(0, 0), pady=(0, 1))

        self.Search_Column = customtkinter.CTkButton(master=self.NextTable_frame, text="Search Column Data",
                                                     corner_radius=0, font=("arial", 16),
                                                     fg_color="transparent",
                                                     text_color=("gray10", "gray90"),
                                                     hover_color=("gray70", "gray30"),
                                                     anchor="w", border_spacing=8, width=200,
                                                     command=self.Search_Col_Btn)
        self.Search_Column.grid(row=14, padx=(0, 0), pady=(0, 1))

        self.Delete_Column = customtkinter.CTkButton(master=self.NextTable_frame, text="Delete Column",
                                                     corner_radius=0, font=("arial", 16),
                                                     fg_color="transparent",
                                                     text_color=("gray10", "gray90"),
                                                     hover_color=("gray70", "gray30"),
                                                     anchor="w", border_spacing=8, width=200,
                                                     command=self.Delete_Col_Btn)

        self.Delete_Column.grid(row=15, padx=(0, 0), pady=(0, 1))

        # Next Table Create Table Interface
        self.Create_Table_frame.grid_columnconfigure(1, weight=1)
        self.Create_Table_frame.grid_rowconfigure(1, weight=1)

        self.Create_Table_Input = customtkinter.CTkEntry(master=self.Create_Table_frame, placeholder_text="Table Name",
                                                         height=30,
                                                         font=("arial", 18))
        self.Create_Table_Input.grid(row=0, column=0, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.Create_Table_Btn = customtkinter.CTkButton(master=self.Create_Table_frame, text="Create Table",
                                                        font=("arial", 18),
                                                        width=120, height=30, command=self.create_table_btn)
        self.Create_Table_Btn.grid(row=0, column=2, padx=(20, 20), pady=(0, 0))

        self.Create_Table_result = customtkinter.CTkTextbox(master=self.Create_Table_frame, wrap="none",
                                                            corner_radius=0,
                                                            border_width=0, font=("Terminal", 18))
        self.Create_Table_result.grid(row=1, column=1, columnspan=2, padx=(20, 20), pady=(0, 20), sticky="nsew")
        self.Create_Table_result.configure(state='disabled')

        # Next Table Read Table Interface
        self.Read_Table_frame.grid_columnconfigure(1, weight=1)
        self.Read_Table_frame.grid_rowconfigure(1, weight=1)

        self.Read_Table_Input = customtkinter.CTkEntry(master=self.Read_Table_frame, placeholder_text="Table Name",
                                                       height=30,
                                                       font=("arial", 18))
        self.Read_Table_Input.grid(row=0, column=0, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.Read_Table_Btn = customtkinter.CTkButton(master=self.Read_Table_frame, text="Read Table",
                                                      font=("arial", 18),
                                                      width=120, height=30, command=self.read_table_btn)
        self.Read_Table_Btn.grid(row=0, column=2, padx=(20, 20), pady=(0, 0))

        self.Read_Table_result = customtkinter.CTkTextbox(master=self.Read_Table_frame, wrap="none",
                                                          corner_radius=0,
                                                          border_width=0, font=("Terminal", 18))
        self.Read_Table_result.grid(row=1, column=1, columnspan=2, padx=(20, 20), pady=(0, 20), sticky="nsew")
        self.Read_Table_result.configure(state='disabled')

        # Next Table Delete Table Interface
        self.Delete_Table_frame.grid_columnconfigure(1, weight=1)
        self.Delete_Table_frame.grid_rowconfigure(1, weight=1)

        self.Delete_Table_Input = customtkinter.CTkEntry(master=self.Delete_Table_frame, placeholder_text="Table Name",
                                                         height=30,
                                                         font=("arial", 18))
        self.Delete_Table_Input.grid(row=0, column=0, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.Delete_Table_Btn = customtkinter.CTkButton(master=self.Delete_Table_frame, text="Delete Table",
                                                        font=("arial", 18),
                                                        width=120, height=30, command=self.delete_table_btn)
        self.Delete_Table_Btn.grid(row=0, column=2, padx=(20, 20), pady=(0, 0))

        self.Delete_Table_result = customtkinter.CTkTextbox(master=self.Delete_Table_frame, wrap="none",
                                                            corner_radius=0,
                                                            border_width=0, font=("Terminal", 18))
        self.Delete_Table_result.grid(row=1, column=1, columnspan=2, padx=(20, 20), pady=(0, 20), sticky="nsew")
        self.Delete_Table_result.configure(state='disabled')

        # Next Table Add Column Name Interface
        self.Add_Col_Name_frame.grid_columnconfigure(1, weight=1)
        self.Add_Col_Name_frame.grid_rowconfigure(1, weight=1)

        self.Add_Col_Name_Input1 = customtkinter.CTkEntry(master=self.Add_Col_Name_frame, placeholder_text="Table Name",
                                                          height=30,
                                                          font=("arial", 18), width=300)
        self.Add_Col_Name_Input1.grid(row=0, column=0, columnspan=1, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.Add_Col_Name_Input2 = customtkinter.CTkEntry(master=self.Add_Col_Name_frame,
                                                          placeholder_text="Column Name",
                                                          height=30,
                                                          font=("arial", 18))
        self.Add_Col_Name_Input2.grid(row=0, column=1, columnspan=1, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.Add_Col_Name_Btn = customtkinter.CTkButton(master=self.Add_Col_Name_frame, text="Add Column Name",
                                                        font=("arial", 18),
                                                        width=120, height=30, command=self.add_col_name_btn)
        self.Add_Col_Name_Btn.grid(row=0, column=2, padx=(20, 20), pady=(0, 0))

        self.Add_Col_Name_result = customtkinter.CTkTextbox(master=self.Add_Col_Name_frame, wrap="none",
                                                            corner_radius=0,
                                                            border_width=0, font=("Terminal", 18))
        self.Add_Col_Name_result.grid(row=1, column=0, columnspan=4, padx=(20, 20), pady=(0, 20), sticky="nsew")

        self.Add_Col_Name_result.configure(state='disabled')

        # Next Table Read Column Name Interface
        self.Read_Col_Name_frame.grid_columnconfigure(1, weight=1)
        self.Read_Col_Name_frame.grid_rowconfigure(1, weight=1)

        self.Read_Col_Name_Input = customtkinter.CTkEntry(master=self.Read_Col_Name_frame,
                                                          placeholder_text="Table Name",
                                                          height=30,
                                                          font=("arial", 18))
        self.Read_Col_Name_Input.grid(row=0, column=0, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.Read_Col_Name_Btn = customtkinter.CTkButton(master=self.Read_Col_Name_frame, text="Read Column Name",
                                                         font=("arial", 18),
                                                         width=120, height=30, command=self.read_col_name_btn)
        self.Read_Col_Name_Btn.grid(row=0, column=2, padx=(20, 20), pady=(0, 0))

        self.Read_Col_Name_result = customtkinter.CTkTextbox(master=self.Read_Col_Name_frame, wrap="none",
                                                             corner_radius=0,
                                                             border_width=0, font=("Terminal", 18))
        self.Read_Col_Name_result.grid(row=1, column=0, columnspan=4, padx=(20, 20), pady=(0, 20), sticky="nsew")
        self.Read_Col_Name_result.configure(state='disabled')

        # Next Table Update Column Name Interface
        self.Update_Col_Name_frame.grid_columnconfigure(2, weight=1)
        self.Update_Col_Name_frame.grid_rowconfigure(1, weight=1)

        self.Update_Col_Name_Input1 = customtkinter.CTkEntry(master=self.Update_Col_Name_frame,
                                                             placeholder_text="Table Name",
                                                             height=30,
                                                             font=("arial", 18), width=200)
        self.Update_Col_Name_Input1.grid(row=0, column=0, columnspan=1, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.Update_Col_Name_Input2 = customtkinter.CTkEntry(master=self.Update_Col_Name_frame,
                                                             placeholder_text="Old Column Name",
                                                             height=30,
                                                             font=("arial", 18), width=200)
        self.Update_Col_Name_Input2.grid(row=0, column=1, columnspan=1, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.Update_Col_Name_Input3 = customtkinter.CTkEntry(master=self.Update_Col_Name_frame,
                                                             placeholder_text="New Column Name",
                                                             height=30,
                                                             font=("arial", 18))
        self.Update_Col_Name_Input3.grid(row=0, column=2, columnspan=1, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.Update_Col_Name_Btn = customtkinter.CTkButton(master=self.Update_Col_Name_frame, text="Update Column Name",
                                                           font=("arial", 18),
                                                           width=120, height=30, command=self.update_col_name_btn)

        self.Update_Col_Name_Btn.grid(row=0, column=4, padx=(20, 20), pady=(0, 0))

        self.Update_Col_Name_result = customtkinter.CTkTextbox(master=self.Update_Col_Name_frame, wrap="none",
                                                               corner_radius=0,
                                                               border_width=0, font=("Terminal", 18))
        self.Update_Col_Name_result.grid(row=1, column=0, columnspan=5, padx=(20, 20), pady=(0, 20), sticky="nsew")

        self.Update_Col_Name_result.configure(state='disabled')

        # Next Table Delete Column Name Interface
        self.Delete_Col_Name_frame.grid_columnconfigure(1, weight=1)
        self.Delete_Col_Name_frame.grid_rowconfigure(1, weight=1)

        self.Delete_Col_Name_Input1 = customtkinter.CTkEntry(master=self.Delete_Col_Name_frame,
                                                             placeholder_text="Table Name",
                                                             height=30,
                                                             font=("arial", 18), width=300)
        self.Delete_Col_Name_Input1.grid(row=0, column=0, columnspan=1, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.Delete_Col_Name_Input2 = customtkinter.CTkEntry(master=self.Delete_Col_Name_frame,
                                                             placeholder_text="Column Name",
                                                             height=30,
                                                             font=("arial", 18))
        self.Delete_Col_Name_Input2.grid(row=0, column=1, columnspan=1, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.Delete_Col_Name_Btn = customtkinter.CTkButton(master=self.Delete_Col_Name_frame, text="Delete Column Name",
                                                           font=("arial", 18),
                                                           width=120, height=30, command=self.delete_col_name_btn)
        self.Delete_Col_Name_Btn.grid(row=0, column=2, padx=(20, 20), pady=(0, 0))

        self.Delete_Col_Name_result = customtkinter.CTkTextbox(master=self.Delete_Col_Name_frame, wrap="none",
                                                               corner_radius=0,
                                                               border_width=0, font=("Terminal", 18))
        self.Delete_Col_Name_result.grid(row=1, column=0, columnspan=4, padx=(20, 20), pady=(0, 20), sticky="nsew")

        self.Delete_Col_Name_result.configure(state='disabled')

        # Next Table Add Data Interface
        self.Add_Data_frame.grid_columnconfigure(1, weight=1)
        self.Add_Data_frame.grid_rowconfigure(1, weight=1)

        self.Add_Data_Input1 = customtkinter.CTkEntry(master=self.Add_Data_frame,
                                                      placeholder_text="Table Name",
                                                      height=30,
                                                      font=("arial", 18), width=300)
        self.Add_Data_Input1.grid(row=0, column=0, columnspan=1, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.Add_Data_Input2 = customtkinter.CTkEntry(master=self.Add_Data_frame,
                                                      placeholder_text="Row Data",
                                                      height=30,
                                                      font=("arial", 18))
        self.Add_Data_Input2.grid(row=0, column=1, columnspan=1, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.Add_Data_Btn = customtkinter.CTkButton(master=self.Add_Data_frame, text="Add Data",
                                                    font=("arial", 18),
                                                    width=120, height=30, command=self.add_data_btn)
        self.Add_Data_Btn.grid(row=0, column=2, padx=(20, 20), pady=(0, 0))

        self.Add_Data_result = customtkinter.CTkTextbox(master=self.Add_Data_frame, wrap="none",
                                                        corner_radius=0,
                                                        border_width=0, font=("Terminal", 18))
        self.Add_Data_result.grid(row=1, column=0, columnspan=4, padx=(20, 20), pady=(0, 20), sticky="nsew")

        self.Add_Data_result.configure(state='disabled')

        # Next Table Search Data Interface
        self.Search_Data_frame.grid_columnconfigure(2, weight=1)
        self.Search_Data_frame.grid_rowconfigure(1, weight=1)

        self.Search_Data_Input1 = customtkinter.CTkEntry(master=self.Search_Data_frame,
                                                         placeholder_text="Table Name",
                                                         height=30,
                                                         font=("arial", 18), width=200)
        self.Search_Data_Input1.grid(row=0, column=0, columnspan=1, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.Search_Data_Input2 = customtkinter.CTkEntry(master=self.Search_Data_frame,
                                                         placeholder_text="Row Id",
                                                         height=30,
                                                         font=("arial", 18), width=200)
        self.Search_Data_Input2.grid(row=0, column=1, columnspan=1, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.Search_Data_Input3 = customtkinter.CTkEntry(master=self.Search_Data_frame,
                                                         placeholder_text="Column name",
                                                         height=30,
                                                         font=("arial", 18))
        self.Search_Data_Input3.grid(row=0, column=2, columnspan=1, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.Search_Data_Btn = customtkinter.CTkButton(master=self.Search_Data_frame, text="Search Data",
                                                       font=("arial", 18),
                                                       width=120, height=30, command=self.search_data_btn)

        self.Search_Data_Btn.grid(row=0, column=4, padx=(20, 20), pady=(0, 0))

        self.Search_Data_result = customtkinter.CTkTextbox(master=self.Search_Data_frame, wrap="none",
                                                           corner_radius=0,
                                                           border_width=0, font=("Terminal", 18))
        self.Search_Data_result.grid(row=1, column=0, columnspan=5, padx=(20, 20), pady=(0, 20), sticky="nsew")

        self.Search_Data_result.configure(state='disabled')

        # Next Table Update Data Interface
        self.Update_Data_frame.grid_columnconfigure(3, weight=1)
        self.Update_Data_frame.grid_rowconfigure(1, weight=1)

        self.Update_Data_Input1 = customtkinter.CTkEntry(master=self.Update_Data_frame,
                                                         placeholder_text="Table Name",
                                                         height=30,
                                                         font=("arial", 18), width=200)
        self.Update_Data_Input1.grid(row=0, column=0, columnspan=1, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.Update_Data_Input2 = customtkinter.CTkEntry(master=self.Update_Data_frame,
                                                         placeholder_text="Row Id",
                                                         height=30,
                                                         font=("arial", 18), width=200)
        self.Update_Data_Input2.grid(row=0, column=1, columnspan=1, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.Update_Data_Input3 = customtkinter.CTkEntry(master=self.Update_Data_frame,
                                                         placeholder_text="Column name",
                                                         height=30,
                                                         font=("arial", 18), width=200)
        self.Update_Data_Input3.grid(row=0, column=2, columnspan=1, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.Update_Data_Input4 = customtkinter.CTkEntry(master=self.Update_Data_frame,
                                                         placeholder_text="New Column Data",
                                                         height=30,
                                                         font=("arial", 18))
        self.Update_Data_Input4.grid(row=0, column=3, columnspan=1, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.Update_Data_Btn = customtkinter.CTkButton(master=self.Update_Data_frame, text="Update Data",
                                                       font=("arial", 18),
                                                       width=120, height=30, command=self.update_data_btn)

        self.Update_Data_Btn.grid(row=0, column=5, padx=(20, 20), pady=(0, 0))

        self.Update_Data_result = customtkinter.CTkTextbox(master=self.Update_Data_frame, wrap="none",
                                                           corner_radius=0,
                                                           border_width=0, font=("Terminal", 18))
        self.Update_Data_result.grid(row=1, column=0, columnspan=6, padx=(20, 20), pady=(0, 20), sticky="nsew")

        self.Update_Data_result.configure(state='disabled')

        # Next Table Delete Data Interface
        self.Delete_Data_frame.grid_columnconfigure(2, weight=1)
        self.Delete_Data_frame.grid_rowconfigure(1, weight=1)

        self.Delete_Data_Input1 = customtkinter.CTkEntry(master=self.Delete_Data_frame,
                                                         placeholder_text="Table Name",
                                                         height=30,
                                                         font=("arial", 18), width=200)
        self.Delete_Data_Input1.grid(row=0, column=0, columnspan=1, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.Delete_Data_Input2 = customtkinter.CTkEntry(master=self.Delete_Data_frame,
                                                         placeholder_text="Row Id",
                                                         height=30,
                                                         font=("arial", 18), width=200)
        self.Delete_Data_Input2.grid(row=0, column=1, columnspan=1, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.Delete_Data_Input3 = customtkinter.CTkEntry(master=self.Delete_Data_frame,
                                                         placeholder_text="Column name",
                                                         height=30,
                                                         font=("arial", 18))
        self.Delete_Data_Input3.grid(row=0, column=2, columnspan=1, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.Delete_Data_Btn = customtkinter.CTkButton(master=self.Delete_Data_frame, text="Delete Data",
                                                       font=("arial", 18),
                                                       width=120, height=30, command=self.delete_data_btn)

        self.Delete_Data_Btn.grid(row=0, column=4, padx=(20, 20), pady=(0, 0))

        self.Delete_Data_result = customtkinter.CTkTextbox(master=self.Delete_Data_frame, wrap="none",
                                                           corner_radius=0,
                                                           border_width=0, font=("Terminal", 18))
        self.Delete_Data_result.grid(row=1, column=0, columnspan=5, padx=(20, 20), pady=(0, 20), sticky="nsew")

        self.Delete_Data_result.configure(state='disabled')

        # Next Table Search Row Data Interface
        self.Search_Row_Data_frame.grid_columnconfigure(1, weight=1)
        self.Search_Row_Data_frame.grid_rowconfigure(1, weight=1)

        self.Search_Row_Data_Input1 = customtkinter.CTkEntry(master=self.Search_Row_Data_frame,
                                                             placeholder_text="Table Name",
                                                             height=30,
                                                             font=("arial", 18), width=300)
        self.Search_Row_Data_Input1.grid(row=0, column=0, columnspan=1, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.Search_Row_Data_Input2 = customtkinter.CTkEntry(master=self.Search_Row_Data_frame,
                                                             placeholder_text="Row Id",
                                                             height=30,
                                                             font=("arial", 18))
        self.Search_Row_Data_Input2.grid(row=0, column=1, columnspan=1, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.Search_Row_Data_Btn = customtkinter.CTkButton(master=self.Search_Row_Data_frame, text="Search Row Data",
                                                           font=("arial", 18),
                                                           width=120, height=30, command=self.search_row_btn)
        self.Search_Row_Data_Btn.grid(row=0, column=2, padx=(20, 20), pady=(0, 0))

        self.Search_Row_Data_result = customtkinter.CTkTextbox(master=self.Search_Row_Data_frame, wrap="none",
                                                               corner_radius=0,
                                                               border_width=0, font=("Terminal", 18))
        self.Search_Row_Data_result.grid(row=1, column=0, columnspan=4, padx=(20, 20), pady=(0, 20), sticky="nsew")

        self.Search_Row_Data_result.configure(state='disabled')

        # Next Table Update Row Data Interface
        self.Update_Row_Data_frame.grid_columnconfigure(2, weight=1)
        self.Update_Row_Data_frame.grid_rowconfigure(1, weight=1)

        self.Update_Row_Data_Input1 = customtkinter.CTkEntry(master=self.Update_Row_Data_frame,
                                                             placeholder_text="Table Name",
                                                             height=30,
                                                             font=("arial", 18), width=200)
        self.Update_Row_Data_Input1.grid(row=0, column=0, columnspan=1, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.Update_Row_Data_Input2 = customtkinter.CTkEntry(master=self.Update_Row_Data_frame,
                                                             placeholder_text="Row Id",
                                                             height=30,
                                                             font=("arial", 18), width=200)
        self.Update_Row_Data_Input2.grid(row=0, column=1, columnspan=1, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.Update_Row_Data_Input3 = customtkinter.CTkEntry(master=self.Update_Row_Data_frame,
                                                             placeholder_text="New Data",
                                                             height=30,
                                                             font=("arial", 18))
        self.Update_Row_Data_Input3.grid(row=0, column=2, columnspan=1, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.Update_Row_Data_Btn = customtkinter.CTkButton(master=self.Update_Row_Data_frame, text="Update Row Data",
                                                           font=("arial", 18),
                                                           width=120, height=30, command=self.update_row_btn)

        self.Update_Row_Data_Btn.grid(row=0, column=4, padx=(20, 20), pady=(0, 0))

        self.Update_Row_Data_result = customtkinter.CTkTextbox(master=self.Update_Row_Data_frame, wrap="none",
                                                               corner_radius=0,
                                                               border_width=0, font=("Terminal", 18))
        self.Update_Row_Data_result.grid(row=1, column=0, columnspan=5, padx=(20, 20), pady=(0, 20), sticky="nsew")

        self.Update_Row_Data_result.configure(state='disabled')

        # Next Table Delete Row Data Interface
        self.Delete_Row_frame.grid_columnconfigure(1, weight=1)
        self.Delete_Row_frame.grid_rowconfigure(1, weight=1)

        self.Delete_Row_Input1 = customtkinter.CTkEntry(master=self.Delete_Row_frame,
                                                        placeholder_text="Table Name",
                                                        height=30,
                                                        font=("arial", 18), width=300)
        self.Delete_Row_Input1.grid(row=0, column=0, columnspan=1, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.Delete_Row_Input2 = customtkinter.CTkEntry(master=self.Delete_Row_frame,
                                                        placeholder_text="Row Id",
                                                        height=30,
                                                        font=("arial", 18))
        self.Delete_Row_Input2.grid(row=0, column=1, columnspan=1, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.Delete_Row_Btn = customtkinter.CTkButton(master=self.Delete_Row_frame, text="Delete Row",
                                                      font=("arial", 18),
                                                      width=120, height=30, command=self.delete_row_btn)
        self.Delete_Row_Btn.grid(row=0, column=2, padx=(20, 20), pady=(0, 0))

        self.Delete_Row_result = customtkinter.CTkTextbox(master=self.Delete_Row_frame, wrap="none",
                                                          corner_radius=0,
                                                          border_width=0, font=("Terminal", 18))
        self.Delete_Row_result.grid(row=1, column=0, columnspan=4, padx=(20, 20), pady=(0, 20), sticky="nsew")

        self.Delete_Row_result.configure(state='disabled')

        # Next Table Search Column Data Interface
        self.Search_Column_frame.grid_columnconfigure(1, weight=1)
        self.Search_Column_frame.grid_rowconfigure(1, weight=1)

        self.Search_Column_Input1 = customtkinter.CTkEntry(master=self.Search_Column_frame,
                                                           placeholder_text="Table Name",
                                                           height=30,
                                                           font=("arial", 18), width=300)
        self.Search_Column_Input1.grid(row=0, column=0, columnspan=1, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.Search_Column_Input2 = customtkinter.CTkEntry(master=self.Search_Column_frame,
                                                           placeholder_text="Column Name",
                                                           height=30,
                                                           font=("arial", 18))
        self.Search_Column_Input2.grid(row=0, column=1, columnspan=1, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.Search_Column_Btn = customtkinter.CTkButton(master=self.Search_Column_frame, text="Search Column Data",
                                                         font=("arial", 18),
                                                         width=120, height=30, command=self.search_col_btn)
        self.Search_Column_Btn.grid(row=0, column=2, padx=(20, 20), pady=(0, 0))

        self.Search_Column_result = customtkinter.CTkTextbox(master=self.Search_Column_frame, wrap="none",
                                                             corner_radius=0,
                                                             border_width=0, font=("Terminal", 18))
        self.Search_Column_result.grid(row=1, column=0, columnspan=4, padx=(20, 20), pady=(0, 20), sticky="nsew")

        self.Search_Column_result.configure(state='disabled')

        # Next Table Delete Column Interface
        self.Delete_Column_frame.grid_columnconfigure(1, weight=1)
        self.Delete_Column_frame.grid_rowconfigure(1, weight=1)

        self.Delete_Column_Input1 = customtkinter.CTkEntry(master=self.Delete_Column_frame,
                                                           placeholder_text="Table Name",
                                                           height=30,
                                                           font=("arial", 18), width=300)
        self.Delete_Column_Input1.grid(row=0, column=0, columnspan=1, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.Delete_Column_Input2 = customtkinter.CTkEntry(master=self.Delete_Column_frame,
                                                           placeholder_text="Column Name",
                                                           height=30,
                                                           font=("arial", 18))
        self.Delete_Column_Input2.grid(row=0, column=1, columnspan=1, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.Delete_Column_Btn = customtkinter.CTkButton(master=self.Delete_Column_frame,
                                                         text="Delete Column",
                                                         font=("arial", 18),
                                                         width=120, height=30, command=self.delete_column_btn)
        self.Delete_Column_Btn.grid(row=0, column=2, padx=(20, 20), pady=(0, 0))

        self.Delete_Column_result = customtkinter.CTkTextbox(master=self.Delete_Column_frame, wrap="none",
                                                             corner_radius=0,
                                                             border_width=0, font=("Terminal", 18))
        self.Delete_Column_result.grid(row=1, column=0, columnspan=4, padx=(20, 20), pady=(0, 20), sticky="nsew")

        self.Delete_Column_result.configure(state='disabled')

        # Next Table <Enter Position>
        self.NextTable_button.bind("<Enter>", self.onPositionNextTable)
        self.Create_Table_frame.bind("<Enter>", self.onLeave)
        self.Create_Table_Input.bind("<Enter>", self.onLeave)
        self.Create_Table_result.bind("<Enter>", self.onLeave)

        self.Read_Table_frame.bind("<Enter>", self.onLeave)
        self.Read_Table_Input.bind("<Enter>", self.onLeave)
        self.Read_Table_result.bind("<Enter>", self.onLeave)

        self.Delete_Table_frame.bind("<Enter>", self.onLeave)
        self.Delete_Table_Input.bind("<Enter>", self.onLeave)
        self.Delete_Table_result.bind("<Enter>", self.onLeave)

        self.Add_Col_Name_frame.bind("<Enter>", self.onLeave)
        self.Add_Col_Name_Input1.bind("<Enter>", self.onLeave)
        self.Add_Col_Name_Input2.bind("<Enter>", self.onLeave)
        self.Add_Col_Name_result.bind("<Enter>", self.onLeave)

        self.Read_Col_Name_frame.bind("<Enter>", self.onLeave)
        self.Read_Col_Name_Input.bind("<Enter>", self.onLeave)
        self.Read_Col_Name_result.bind("<Enter>", self.onLeave)

        self.Update_Col_Name_frame.bind("<Enter>", self.onLeave)
        self.Update_Col_Name_Input1.bind("<Enter>", self.onLeave)
        self.Update_Col_Name_Input2.bind("<Enter>", self.onLeave)
        self.Update_Col_Name_Input3.bind("<Enter>", self.onLeave)
        self.Update_Col_Name_result.bind("<Enter>", self.onLeave)

        self.Delete_Col_Name_frame.bind("<Enter>", self.onLeave)
        self.Delete_Col_Name_Input1.bind("<Enter>", self.onLeave)
        self.Delete_Col_Name_Input2.bind("<Enter>", self.onLeave)
        self.Delete_Col_Name_result.bind("<Enter>", self.onLeave)

        self.Add_Data_frame.bind("<Enter>", self.onLeave)
        self.Add_Data_Input1.bind("<Enter>", self.onLeave)
        self.Add_Data_Input2.bind("<Enter>", self.onLeave)
        self.Add_Data_result.bind("<Enter>", self.onLeave)

        self.Search_Data_frame.bind("<Enter>", self.onLeave)
        self.Search_Data_Input1.bind("<Enter>", self.onLeave)
        self.Search_Data_Input2.bind("<Enter>", self.onLeave)
        self.Search_Data_Input3.bind("<Enter>", self.onLeave)
        self.Search_Data_result.bind("<Enter>", self.onLeave)

        self.Update_Data_frame.bind("<Enter>", self.onLeave)
        self.Update_Data_Input1.bind("<Enter>", self.onLeave)
        self.Update_Data_Input2.bind("<Enter>", self.onLeave)
        self.Update_Data_Input3.bind("<Enter>", self.onLeave)
        self.Update_Data_Input4.bind("<Enter>", self.onLeave)
        self.Update_Data_result.bind("<Enter>", self.onLeave)

        self.Delete_Data_frame.bind("<Enter>", self.onLeave)
        self.Delete_Data_Input1.bind("<Enter>", self.onLeave)
        self.Delete_Data_Input2.bind("<Enter>", self.onLeave)
        self.Delete_Data_Input3.bind("<Enter>", self.onLeave)
        self.Delete_Data_result.bind("<Enter>", self.onLeave)

        self.Search_Row_Data_frame.bind("<Enter>", self.onLeave)
        self.Search_Row_Data_Input1.bind("<Enter>", self.onLeave)
        self.Search_Row_Data_Input2.bind("<Enter>", self.onLeave)
        self.Search_Row_Data_result.bind("<Enter>", self.onLeave)

        self.Update_Row_Data_frame.bind("<Enter>", self.onLeave)
        self.Update_Row_Data_Input1.bind("<Enter>", self.onLeave)
        self.Update_Row_Data_Input2.bind("<Enter>", self.onLeave)
        self.Update_Row_Data_Input3.bind("<Enter>", self.onLeave)
        self.Update_Row_Data_result.bind("<Enter>", self.onLeave)

        self.Delete_Row_frame.bind("<Enter>", self.onLeave)
        self.Delete_Row_Input1.bind("<Enter>", self.onLeave)
        self.Delete_Row_Input2.bind("<Enter>", self.onLeave)
        self.Delete_Row_result.bind("<Enter>", self.onLeave)

        self.Search_Column_frame.bind("<Enter>", self.onLeave)
        self.Search_Column_Input1.bind("<Enter>", self.onLeave)
        self.Search_Column_Input2.bind("<Enter>", self.onLeave)
        self.Search_Column_result.bind("<Enter>", self.onLeave)

        self.Delete_Column_frame.bind("<Enter>", self.onLeave)
        self.Delete_Column_Input1.bind("<Enter>", self.onLeave)
        self.Delete_Column_Input2.bind("<Enter>", self.onLeave)
        self.Delete_Column_result.bind("<Enter>", self.onLeave)

        # Converter
        self.Converter_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.Converter_frame.rowconfigure(5, weight=1)

        self.NextTable_To_NextDatabase = customtkinter.CTkButton(master=self.Converter_frame,
                                                                 text="NextTable To NextDatabase", border_spacing=8,
                                                                 corner_radius=0, font=("arial", 16),
                                                                 fg_color="transparent",
                                                                 text_color=("gray10", "gray90"),
                                                                 hover_color=("gray70", "gray30"),
                                                                 anchor="w", width=220
                                                                 , command=self.NextTable_To_NextDatabase_Btn)
        self.NextTable_To_NextDatabase.grid(row=0, padx=(0, 0), pady=(0, 1))

        self.NextTable_To_Excel = customtkinter.CTkButton(master=self.Converter_frame, text="NextTable To Excel",
                                                          corner_radius=0, font=("arial", 16), fg_color="transparent",
                                                          text_color=("gray10", "gray90"),
                                                          hover_color=("gray70", "gray30"),
                                                          anchor="w",
                                                          border_spacing=8, width=220)
        self.NextTable_To_Excel.grid(row=1, padx=(0, 0), pady=(0, 1))

        self.Excel_To_NextTable = customtkinter.CTkButton(master=self.Converter_frame, text="Excel To NextTable",
                                                          corner_radius=0, font=("arial", 16), fg_color="transparent",
                                                          text_color=("gray10", "gray90"),
                                                          hover_color=("gray70", "gray30"),
                                                          anchor="w",
                                                          border_spacing=8, width=220)
        self.Excel_To_NextTable.grid(row=2, padx=(0, 0), pady=(0, 1))

        self.NextTable_To_Txt = customtkinter.CTkButton(master=self.Converter_frame, text="NextTable To Txt File",
                                                        corner_radius=0, font=("arial", 16), fg_color="transparent",
                                                        text_color=("gray10", "gray90"),
                                                        hover_color=("gray70", "gray30"),
                                                        anchor="w",
                                                        border_spacing=8, width=220)
        self.NextTable_To_Txt.grid(row=3, padx=(0, 0), pady=(0, 1))

        self.NextDatabase_To_Txt = customtkinter.CTkButton(master=self.Converter_frame, text="NextDatabase To Txt File",
                                                           corner_radius=0, font=("arial", 16), fg_color="transparent",
                                                           text_color=("gray10", "gray90"),
                                                           hover_color=("gray70", "gray30"),
                                                           anchor="w",
                                                           border_spacing=8, width=220)
        self.NextDatabase_To_Txt.grid(row=4, padx=(0, 0), pady=(0, 1))

        # NextTable To NextDatabase  Interface
        self.NextTable_To_NextDatabase_frame.grid_columnconfigure(1, weight=1)
        self.NextTable_To_NextDatabase_frame.grid_rowconfigure(1, weight=1)

        self.NextTable_To_NextDatabase_Input1 = customtkinter.CTkEntry(master=self.NextTable_To_NextDatabase_frame,
                                                                       placeholder_text="Table Name",
                                                                       height=30,
                                                                       font=("arial", 18), width=300)
        self.NextTable_To_NextDatabase_Input1.grid(row=0, column=0, columnspan=1, padx=(20, 0), pady=(20, 20),
                                                   sticky="nsew")

        self.NextTable_To_NextDatabase_Input2 = customtkinter.CTkEntry(master=self.NextTable_To_NextDatabase_frame,
                                                                       placeholder_text="Column Name",
                                                                       height=30,
                                                                       font=("arial", 18))
        self.NextTable_To_NextDatabase_Input2.grid(row=0, column=1, columnspan=1, padx=(20, 0), pady=(20, 20),
                                                   sticky="nsew")

        self.NextTable_To_NextDatabase_Btn = customtkinter.CTkButton(master=self.NextTable_To_NextDatabase_frame,
                                                                     text="Convert",
                                                                     font=("arial", 18),
                                                                     width=120, height=30,
                                                                     command=self.nextTable_to_nextDatabase_btn)
        self.NextTable_To_NextDatabase_Btn.grid(row=0, column=2, padx=(20, 20), pady=(0, 0))

        self.NextTable_To_NextDatabase_result = customtkinter.CTkLabel(master=self.NextTable_To_NextDatabase_frame,
                                                                    text="", fg_color=("gray100", "gray10"), font=("Terminal", 18))
        self.NextTable_To_NextDatabase_result.grid(row=1, column=0, columnspan=4, padx=(20, 20), pady=(0, 20),
                                                   sticky="nsew")

        # Converter <Enter Position>
        self.Converter_button.bind("<Enter>", self.onPositionConverter)

        self.NextTable_To_NextDatabase_frame.bind("<Enter>", self.onLeave)
        self.NextTable_To_NextDatabase_Input1.bind("<Enter>", self.onLeave)
        self.NextTable_To_NextDatabase_Input2.bind("<Enter>", self.onLeave)
        self.NextTable_To_NextDatabase_result.bind("<Enter>", self.onLeave)

        self.Home_frame.bind("<Enter>", self.onLeave)

    def onPositionNextDatabase(self, name):
        self.select_frame_by_name("NextDatabase")

    def onPositionNextTable(self, name):
        self.select_frame_by_name("NextTable")

    def onPositionConverter(self, name):
        self.select_frame_by_name("Converter")

    def onLeave(self, name):
        self.select_frame_by_name("")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.NextDatabase_button.configure(fg_color=("gray75", "gray25") if name == "NextDatabase" else "transparent")
        self.NextTable_button.configure(fg_color=("gray75", "gray25") if name == "NextTable" else "transparent")
        self.Converter_button.configure(fg_color=("gray75", "gray25") if name == "Converter" else "transparent")
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
        if name == "Converter":
            self.Converter_frame.place(x=242, y=42)
        else:
            self.Converter_frame.grid()
            self.Converter_frame.grid_forget()

    def NextDatabaseBtnEvent(self):
        self.select_frame_by_name("NextDatabase")

    def NextTableBtnEvent(self):
        self.select_frame_by_name("NextTable")

    def ConverterBtnEvent(self):
        self.select_frame_by_name("Converter")

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
        elif name == "create_table":
            returnValue = NextTable.create_table(self.Create_Table_Input.get())
            self.Create_Table_result.configure(state='normal')
            self.Create_Table_result.delete("1.0", "end")
            if returnValue == "true":
                self.Create_Table_result.insert("0.0", "Successful!")
                self.Create_Table_result.configure(state='disabled')
            else:
                self.Create_Table_result.insert("0.0", returnValue)
                self.Create_Table_result.configure(state='disabled')

        elif name == "read_table":
            returnValue = NextTable.read_table(self.Read_Table_Input.get())
            self.Read_Table_result.configure(state='normal')
            self.Read_Table_result.delete("1.0", "end")
            if returnValue is None:
                self.Read_Table_result.insert("0.0", "Empty Table")
                self.Read_Table_result.configure(state='disabled')
            else:
                self.Read_Table_result.insert("0.0", returnValue)
                self.Read_Table_result.configure(state='disabled')

        elif name == "delete_table":
            returnValue = NextTable.delete_table(self.Delete_Table_Input.get())
            self.Delete_Table_result.configure(state='normal')
            self.Delete_Table_result.delete("1.0", "end")
            if returnValue == "true":
                self.Delete_Table_result.insert("0.0", "Successful!")
                self.Delete_Table_result.configure(state='disabled')
            else:
                self.Delete_Table_result.insert("0.0", returnValue)
                self.Delete_Table_result.configure(state='disabled')

        elif name == "add_column_name":
            returnValue = NextTable.add_col_name(self.Add_Col_Name_Input1.get(), self.Add_Col_Name_Input2.get())
            self.Add_Col_Name_result.configure(state='normal')
            self.Add_Col_Name_result.delete("1.0", "end")
            if returnValue == "true":
                self.Add_Col_Name_result.insert("0.0", "Successful!")
                self.Add_Col_Name_result.configure(state='disabled')
            else:
                self.Add_Col_Name_result.insert("0.0", returnValue)
                self.Add_Col_Name_result.configure(state='disabled')

        elif name == "read_column_name":
            returnValue = NextTable.read_col_name(self.Read_Col_Name_Input.get())
            self.Read_Col_Name_result.configure(state='normal')
            self.Read_Col_Name_result.delete("1.0", "end")
            if returnValue is None:
                self.Read_Col_Name_result.insert("0.0", "Empty Table")
                self.Read_Col_Name_result.configure(state='disabled')
            else:
                self.Read_Col_Name_result.insert("0.0", returnValue)
                self.Read_Col_Name_result.configure(state='disabled')

        elif name == "update_column_name":
            returnValue = NextTable.update_col_data(self.Update_Col_Name_Input1.get(),
                                                    self.Update_Col_Name_Input2.get(),
                                                    self.Update_Col_Name_Input3.get())
            self.Update_Col_Name_result.configure(state='normal')
            self.Update_Col_Name_result.delete("1.0", "end")
            if returnValue == "true":
                self.Update_Col_Name_result.insert("0.0", "Successful!")
                self.Update_Col_Name_result.configure(state='disabled')
            else:
                self.Update_Col_Name_result.insert("0.0", returnValue)
                self.Update_Col_Name_result.configure(state='disabled')

        elif name == "delete_column_name":
            returnValue = NextTable.delete_col_name(self.Delete_Col_Name_Input1.get(),
                                                    self.Delete_Col_Name_Input2.get())
            self.Delete_Col_Name_result.configure(state='normal')
            self.Delete_Col_Name_result.delete("1.0", "end")
            if returnValue == "true":
                self.Delete_Col_Name_result.insert("0.0", "Successful!")
                self.Delete_Col_Name_result.configure(state='disabled')
            else:
                self.Delete_Col_Name_result.insert("0.0", returnValue)
                self.Delete_Col_Name_result.configure(state='disabled')
        elif name == "add_data":
            returnValue = NextTable.add_data(self.Add_Data_Input1.get(), self.Add_Data_Input2.get())
            self.Add_Data_result.configure(state='normal')
            self.Add_Data_result.delete("1.0", "end")
            if returnValue == "true":
                self.Add_Data_result.insert("0.0", "Successful!")
                self.Add_Data_result.configure(state='disabled')
            else:
                self.Add_Data_result.insert("0.0", returnValue)
                self.Add_Data_result.configure(state='disabled')

        elif name == "search_data":
            returnValue = NextTable.search_data(self.Search_Data_Input1.get(), self.Search_Data_Input2.get(),
                                                self.Search_Data_Input3.get())
            self.Search_Data_result.configure(state='normal')
            self.Search_Data_result.delete("1.0", "end")
            if returnValue == "true":
                self.Search_Data_result.insert("0.0", "Successful!")
                self.Search_Data_result.configure(state='disabled')
            else:
                self.Search_Data_result.insert("0.0", returnValue)
                self.Search_Data_result.configure(state='disabled')

        elif name == "delete_data":
            returnValue = NextTable.delete_data(self.Delete_Data_Input1.get(), self.Delete_Data_Input2.get(),
                                                self.Delete_Data_Input3.get())
            self.Delete_Data_result.configure(state='normal')
            self.Delete_Data_result.delete("1.0", "end")
            if returnValue == "true":
                self.Delete_Data_result.insert("0.0", "Successful!")
                self.Delete_Data_result.configure(state='disabled')
            else:
                self.Delete_Data_result.insert("0.0", returnValue)
                self.Delete_Data_result.configure(state='disabled')

        elif name == "search_row":
            returnValue = NextTable.search_row_data(self.Search_Row_Data_Input1.get(),
                                                    self.Search_Row_Data_Input2.get())
            self.Search_Row_Data_result.configure(state='normal')
            self.Search_Row_Data_result.delete("1.0", "end")
            self.Search_Row_Data_result.insert("0.0", returnValue)
            self.Search_Row_Data_result.configure(state='disabled')

        elif name == "update_row":
            returnValue = NextTable.update_row(self.Update_Row_Data_Input1.get(), self.Update_Row_Data_Input2.get(),
                                               self.Update_Row_Data_Input3.get())
            self.Update_Row_Data_result.configure(state='normal')
            self.Update_Row_Data_result.delete("1.0", "end")
            if returnValue == "true":
                self.Update_Row_Data_result.insert("0.0", "Successful!")
                self.Update_Row_Data_result.configure(state='disabled')
            else:
                self.Update_Row_Data_result.insert("0.0", returnValue)
                self.Update_Row_Data_result.configure(state='disabled')

        elif name == "delete_row":
            returnValue = NextTable.delete_row(self.Delete_Row_Input1.get(), self.Delete_Row_Input1.get())
            self.Delete_Row_result.configure(state='normal')
            self.Delete_Row_result.delete("1.0", "end")
            if returnValue == "true":
                self.Delete_Row_result.insert("0.0", "Successful!")
                self.Delete_Row_result.configure(state='disabled')
            else:
                self.Delete_Row_result.insert("0.0", returnValue)
                self.Delete_Row_result.configure(state='disabled')

        elif name == "search_column":
            returnValue = NextTable.search_col_data(self.Search_Column_Input1.get(), self.Search_Column_Input2.get())
            self.Search_Column_result.configure(state='normal')
            self.Search_Column_result.delete("1.0", "end")
            if returnValue == "true":
                self.Search_Column_result.insert("0.0", "Successful!")
                self.Search_Column_result.configure(state='disabled')
            else:
                self.Search_Column_result.insert("0.0", returnValue)
                self.Search_Column_result.configure(state='disabled')

        elif name == "delete_column":
            returnValue = NextTable.delete_col(self.Delete_Column_Input1.get(), self.Delete_Column_Input2.get())
            self.Delete_Column_result.configure(state='normal')
            self.Delete_Column_result.delete("1.0", "end")
            if returnValue == "true":
                self.Delete_Column_result.insert("0.0", "Successful!")
                self.Delete_Column_result.configure(state='disabled')
            else:
                self.Delete_Column_result.insert("0.0", returnValue)
                self.Delete_Column_result.configure(state='disabled')

        elif name == "nextTable_to_nextDatabase":
            returnValue = NextTable.table_to_doc(self.NextTable_To_NextDatabase_Input1.get(),
                                                 self.NextTable_To_NextDatabase_Input2.get())

            self.NextTable_To_NextDatabase_result.configure(text="")
            if returnValue != "false":
                self.NextTable_To_NextDatabase_result.configure(text="Successful!")
            else:
                self.NextTable_To_NextDatabase_result.configure(text=returnValue)

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

        if name == "Create_Table":
            self.select_frame_by_name("")
            self.Create_Table_frame.grid(row=1, column=0, sticky="nsew")
        else:
            self.Create_Table_frame.grid_forget()

        if name == "Read_Table":
            self.select_frame_by_name("")
            self.Read_Table_frame.grid(row=1, column=0, sticky="nsew")
        else:
            self.Read_Table_frame.grid_forget()

        if name == "Delete_Table":
            self.select_frame_by_name("")
            self.Delete_Table_frame.grid(row=1, column=0, sticky="nsew")
        else:
            self.Delete_Table_frame.grid_forget()

        if name == "Add_Column_Name":
            self.select_frame_by_name("")
            self.Add_Col_Name_frame.grid(row=1, column=0, sticky="nsew")
        else:
            self.Add_Col_Name_frame.grid_forget()

        if name == "Read_Column_Name":
            self.select_frame_by_name("")
            self.Read_Col_Name_frame.grid(row=1, column=0, sticky="nsew")
        else:
            self.Read_Col_Name_frame.grid_forget()

        if name == "Update_Column_Name":
            self.select_frame_by_name("")
            self.Update_Col_Name_frame.grid(row=1, column=0, sticky="nsew")
        else:
            self.Update_Col_Name_frame.grid_forget()

        if name == "Delete_Column_Name":
            self.select_frame_by_name("")
            self.Delete_Col_Name_frame.grid(row=1, column=0, sticky="nsew")
        else:
            self.Delete_Col_Name_frame.grid_forget()

        if name == "Add_Data":
            self.select_frame_by_name("")
            self.Add_Data_frame.grid(row=1, column=0, sticky="nsew")
        else:
            self.Add_Data_frame.grid_forget()

        if name == "Search_Data":
            self.select_frame_by_name("")
            self.Search_Data_frame.grid(row=1, column=0, sticky="nsew")
        else:
            self.Search_Data_frame.grid_forget()

        if name == "Update_Data":
            self.select_frame_by_name("")
            self.Update_Data_frame.grid(row=1, column=0, sticky="nsew")
        else:
            self.Update_Data_frame.grid_forget()

        if name == "Delete_Data":
            self.select_frame_by_name("")
            self.Delete_Data_frame.grid(row=1, column=0, sticky="nsew")
        else:
            self.Delete_Data_frame.grid_forget()

        if name == "Search_Row":
            self.select_frame_by_name("")
            self.Search_Row_Data_frame.grid(row=1, column=0, sticky="nsew")
        else:
            self.Search_Row_Data_frame.grid_forget()

        if name == "Update_Row":
            self.select_frame_by_name("")
            self.Update_Row_Data_frame.grid(row=1, column=0, sticky="nsew")
        else:
            self.Update_Row_Data_frame.grid_forget()

        if name == "Delete_Row":
            self.select_frame_by_name("")
            self.Delete_Row_frame.grid(row=1, column=0, sticky="nsew")
        else:
            self.Delete_Row_frame.grid_forget()

        if name == "Search_Column":
            self.select_frame_by_name("")
            self.Search_Column_frame.grid(row=1, column=0, sticky="nsew")
        else:
            self.Search_Column_frame.grid_forget()

        if name == "Delete_Column":
            self.select_frame_by_name("")
            self.Delete_Column_frame.grid(row=1, column=0, sticky="nsew")
        else:
            self.Delete_Column_frame.grid_forget()

        if name == "NextTable_To_NextDatabase":
            self.select_frame_by_name("")
            self.NextTable_To_NextDatabase_frame.grid(row=1, column=0, sticky="nsew")
        else:
            self.NextTable_To_NextDatabase_frame.grid_forget()

        if name == "NextTable_To_Excel":
            self.select_frame_by_name("")
            self.NextTable_To_Excel_frame.grid(row=1, column=0, sticky="nsew")
        else:
            self.NextTable_To_Excel_frame.grid_forget()

        if name == "Excel_To_NextTable":
            self.select_frame_by_name("")
            self.Excel_To_NextTable_frame.grid(row=1, column=0, sticky="nsew")
        else:
            self.Excel_To_NextTable_frame.grid_forget()

        if name == "NextTable_To_Txt":
            self.select_frame_by_name("")
            self.NextTable_To_Txt_frame.grid(row=1, column=0, sticky="nsew")
        else:
            self.NextTable_To_Txt_frame.grid_forget()

        if name == "NextDatabase_To_Txt":
            self.select_frame_by_name("")
            self.NextDatabase_To_Txt_frame.grid(row=1, column=0, sticky="nsew")
        else:
            self.NextDatabase_To_Txt_frame.grid_forget()

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

    def Create_Table_Btn(self):
        self.category_selection("Create_Table")

    def create_table_btn(self):
        if self.Create_Table_Input.get() != "":
            self.databaseCheckBtn("create_table")

    def Read_Table_Btn(self):
        self.category_selection("Read_Table")

    def read_table_btn(self):
        if self.Read_Table_Input.get() != "":
            self.databaseCheckBtn("read_table")

    def delete_table_btn(self):
        if self.Delete_Table_Input.get() != "":
            self.databaseCheckBtn("delete_table")

    def Delete_Table_Btn(self):
        self.category_selection("Delete_Table")

    def Add_Col_Name_Btn(self):
        self.category_selection("Add_Column_Name")

    def add_col_name_btn(self):
        if self.Add_Col_Name_Input1.get() != "" and self.Add_Col_Name_Input2.get() != "":
            self.databaseCheckBtn("add_column_name")

    def Read_Col_Name_Btn(self):
        self.category_selection("Read_Column_Name")

    def read_col_name_btn(self):
        if self.Read_Col_Name_Input.get() != "":
            self.databaseCheckBtn("read_column_name")

    def Update_Col_Name_Btn(self):
        self.category_selection("Update_Column_Name")

    def update_col_name_btn(self):
        if self.Update_Col_Name_Input1.get() != "" and self.Update_Col_Name_Input2.get() != "" and self.Update_Col_Name_Input3.get() != "":
            self.databaseCheckBtn("update_column_name")

    def Delete_Col_Name_Btn(self):
        self.category_selection("Delete_Column_Name")

    def delete_col_name_btn(self):
        if self.Delete_Col_Name_Input1.get() != "" and self.Delete_Col_Name_Input2.get() != "":
            self.databaseCheckBtn("delete_column_name")

    def Add_Data_Btn(self):
        self.category_selection("Add_Data")

    def add_data_btn(self):
        if self.Add_Data_Input1.get() != "" and self.Add_Data_Input2.get() != "":
            self.databaseCheckBtn("add_data")

    def Search_Data_Btn(self):
        self.category_selection("Search_Data")

    def search_data_btn(self):
        if self.Search_Data_Input1.get() != "" and self.Search_Data_Input2.get() != "" and self.Search_Data_Input3.get() != "":
            self.databaseCheckBtn("search_data")

    def Update_Data_Btn(self):
        self.category_selection("Update_Data")

    def update_data_btn(self):
        if self.Update_Data_Input1.get() != "" and self.Update_Data_Input2.get() != "" and self.Update_Data_Input3.get() != "" and self.Update_Data_Input4.get() != "":
            self.databaseCheckBtn("update_data")

    def Delete_Data_Btn(self):
        self.category_selection("Delete_Data")

    def delete_data_btn(self):
        if self.Delete_Data_Input1.get() != "" and self.Delete_Data_Input2.get() != "" and self.Delete_Data_Input3.get() != "":
            self.databaseCheckBtn("delete_data")

    def Search_Row_Btn(self):
        self.category_selection("Search_Row")

    def search_row_btn(self):
        if self.Search_Row_Data_Input1.get() != "" and self.Search_Row_Data_Input2.get() != "":
            self.databaseCheckBtn("search_row")

    def Update_Row_Btn(self):
        self.category_selection("Update_Row")

    def update_row_btn(self):
        if self.Update_Row_Data_Input1.get() != "" and self.Update_Row_Data_Input2.get() != "" and self.Update_Row_Data_Input3.get() != "":
            self.databaseCheckBtn("update_row")

    def Delete_Row_Btn(self):
        self.category_selection("Delete_Row")

    def delete_row_btn(self):
        if self.Delete_Row_Input1.get() != "" and self.Delete_Row_Input2.get() != "":
            self.databaseCheckBtn("delete_row")

    def Search_Col_Btn(self):
        self.category_selection("Search_Column")

    def search_col_btn(self):
        if self.Search_Column_Input1.get() != "" and self.Search_Column_Input2.get() != "":
            self.databaseCheckBtn("search_column")

    def Delete_Col_Btn(self):
        self.category_selection("Delete_Column")

    def delete_column_btn(self):
        if self.Delete_Column_Input1.get() != "" and self.Delete_Column_Input2.get() != "":
            self.databaseCheckBtn("delete_column")

    def NextTable_To_NextDatabase_Btn(self):
        self.category_selection("NextTable_To_NextDatabase")

    def nextTable_to_nextDatabase_btn(self):
        if self.NextTable_To_NextDatabase_Input1.get() != "" and self.NextTable_To_NextDatabase_Input2.get() != "":
            self.databaseCheckBtn("nextTable_to_nextDatabase")


if __name__ == "__main__":
    app = App()
    app.mainloop()
