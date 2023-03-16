import tkinter as tk
from tkinter.filedialog import askdirectory
import tkinter.ttk as ttk
from PIL import Image
import info
import os


class Application:
    def __init__(self) -> None:
        self.images: dict[str, Image.Image] = dict()
        self.window = tk.Tk()
        self.window.geometry("1070x700")
        self.tree = ttk.Treeview(self.window,
                                 columns=tuple(str(i) for i in range(7)),
                                 height=34)
        self.folder = ""
        self.tree["show"] = "headings"
        self.tree["displaycolumns"] = tuple()
        self.button_open_folder = tk.Button(self.window, text="Choose folder",
                                            command=self._open_folder)

        self.button_open_folder.place(x=485, y=10)
        self.tree.heading("0", text="Filename")
        self.tree.heading("1", text="Width")
        self.tree.heading("2", text="Height")
        self.tree.heading("3", text="DPI by width")
        self.tree.heading("4", text="DPI by height")
        self.tree.heading("5", text="Color depth")
        self.tree.heading("6", text="Compression")
        self.tree.place(x=10, y=50, width=1050)
        self.window.resizable(False, False)
        self.window.title("Metadata of images")

    def run(self) -> None:
        self.window.mainloop()

    def _construct_tuples_of_info(self) -> list[tuple[str, str, str, str, str,
                                                      str, str]]:
        res = []
        for filename, image in self.images.items():
            width, height = info.get_image_size(image)
            dpi_width, dpi_height = info.get_image_dpi(image)
            depth = info.get_image_color_depth(image)
            compression = info.get_image_compression(image)
            res.append((filename, str(width), str(height), str(dpi_width),
                        str(dpi_height), str(depth), f"{compression : .2}"))

        return res

    def _open_folder(self) -> None:
        self.folder = askdirectory(initialdir=os.getcwd(),
                                   title="Select folder")
        self.images = info.read_images_from_folder(self.folder)
        self.tree["displaycolumns"] = tuple(str(i) for i in range(7))
        for row in self.tree.get_children():
            self.tree.delete(row)
        tuples_of_info = self._construct_tuples_of_info()
        for tupl in tuples_of_info:
            self.tree.insert("", tk.END, values=tupl)

        for id in range(7):
            self.tree.column(id, anchor=tk.CENTER, stretch=tk.NO, width=150)
