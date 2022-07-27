#!/usr/bin/env python3

import os
import shutil
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox


def process_extensions():
    extensions = []
    if extension_entry.get():
        # split entries and sanitize
        for ext in extension_entry.get().split(","):
            # add period so we can use endswith
            extensions.append("." + "".join(filter(str.isalnum, ext)))
    return extensions


def requirements_met():
    if not source_entry.get() or not os.path.exists(source_entry.get()):
        messagebox.showerror("Source path error", "You must choose a source path")
        return False
    if not destination_entry.get() or not os.path.exists(destination_entry.get()):
        messagebox.showerror("Destination path error", "You must choose a destination path")
        return False
    return True


def on_preview():
    if requirements_met():
        ignored_extensions = process_extensions()
        output_list.delete(0, tk.END)
        for (dirpath, dirnames, filenames) in os.walk(source_entry.get()):
            if filenames:
                for filename in filenames:
                    filename_extension = ""
                    # is there an extension
                    if "." in filename:
                        filename_extension = "." + filename.split(".")[-1]
                    if not filename_extension or filename_extension not in ignored_extensions:
                        output_filename = os.path.join(dirpath[len(source_entry.get()) + 1:], filename).replace(os.path.sep,
                                                                                                                '-')
                        if output_filename[-4:].lower() != ".dcm":
                            output_filename += '.dcm'
                        abs_source = os.path.join(os.path.abspath(dirpath), filename)
                        abs_destination = os.path.join(os.path.abspath(destination_entry.get()), output_filename)
                        output_list.insert(tk.END, abs_source + " -->  " + abs_destination)
                        root.update()


def on_submit():
    if requirements_met():
        ignored_extensions = process_extensions()
        output_list.delete(0, tk.END)
        for (dirpath, dirnames, filenames) in os.walk(source_entry.get()):
            if filenames:
                for filename in filenames:
                    filename_extension = ""
                    # is there an extension
                    if "." in filename:
                        filename_extension = "." + filename.split(".")[-1]
                    if not filename_extension or filename_extension not in ignored_extensions:
                        output_filename = os.path.join(dirpath[len(source_entry.get()) + 1:], filename).replace(os.path.sep,
                                                                                                            '-')
                        if output_filename[-4:].lower() != ".dcm":
                            output_filename += '.dcm'
                        abs_source = os.path.join(os.path.abspath(dirpath), filename)
                        abs_destination = os.path.join(os.path.abspath(destination_entry.get()), output_filename)
                        shutil.copyfile(abs_source, abs_destination)
                        output_list.insert(tk.END, "DONE -- " + abs_source + " -->  " + abs_destination)
                        root.update()
        messagebox.showinfo(title="Process Complete",
                            message="Copy the files from the destination directory to Nextcloud and share the folder. When someone clicks on one of the files, the DICOM viewer will load and show the series.")


def choose_source():
    source_entry.delete(0, tk.END)
    source_entry.insert(1, filedialog.askdirectory())


def choose_destination():
    destination_entry.delete(0, tk.END)
    destination_entry.insert(1, filedialog.askdirectory())


root = tk.Tk()
root.title("DICOM to Nextcloud DICOM Viewer")
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=10)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
root.rowconfigure(4, weight=100)

source_button = ttk.Button(text="Choose Source Directory")
source_entry = tk.Entry(width=120)
source_button.config(command=choose_source)
source_button.grid(row=0, column=0, sticky=tk.W + tk.E)
source_entry.grid(row=0, column=1, sticky=tk.W)

destination_button = ttk.Button(text="Choose Destination Directory")
destination_entry = tk.Entry(width=120)
destination_button.config(command=choose_destination)
destination_button.grid(row=1, column=0, sticky=tk.W + tk.E)
destination_entry.grid(row=1, column=1, sticky=tk.W)

extension_label = ttk.Label(root, text="Extensions to ignore (separated by commas):")
extension_label.grid(row=2, column=0)
extension_entry = tk.Entry(width=120)
extension_entry.grid(row=2, column=1, sticky=tk.W)

preview_button = ttk.Button(root, text="Preview")
preview_button.config(command=on_preview)
preview_button.grid(row=3, column=0, sticky=tk.W + tk.E)

submit_button = ttk.Button(root, text="Submit")
submit_button.config(command=on_submit)
submit_button.config(width=25)
submit_button.grid(row=3, column=1, sticky=tk.W)

output_frame = tk.Frame(root)
output_frame.grid(row=4, columnspan=2, sticky=tk.W + tk.E + tk.S + tk.N)
output_frame.columnconfigure(0, weight=100)
output_frame.columnconfigure(1, weight=1)
output_frame.rowconfigure(0, weight=100)
output_list = tk.Listbox(output_frame)
output_list.grid(row=0, column=0, sticky=tk.W + tk.E + tk.S + tk.N)
scrollbar = tk.Scrollbar(output_frame)
scrollbar.grid(row=0, column=1, sticky=tk.W + tk.E + tk.S + tk.N)

output_list.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=output_list.yview)

root.mainloop()
