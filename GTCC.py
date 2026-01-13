# GTCC Gorilla Tag Currency Converter by MamaMonke.
# Converts between SR, USD, and GS.
# You can add new currencies by following the existing pattern.
# Licensed under the MIT License.

import tkinter as tk

USD_PER_1000_SR = 4.99
SR_PER_GS = 0.1  # 1 GS = 0.1 SR
#--- theme (change if you want a different look) ---
BG_COLOR = "#121212"
ENTRY_BG = "#1e1e1e"
TEXT_COLOR = "#eaeaea"
BORDER_COLOR = "#2a2a2a"
#--- end theme ---
updating = False

def sr_changed(*args):
    global updating
    if updating:
        return
    try:
        updating = True
        sr = float(sr_var.get())

        usd = (sr / 1000) * USD_PER_1000_SR
        gs = sr / SR_PER_GS

        usd_var.set(f"{usd:.2f}")
        gs_var.set(f"{gs:.2f}")
    except ValueError:
        usd_var.set("")
        gs_var.set("")
    updating = False


def usd_changed(*args):
    global updating
    if updating:
        return
    try:
        updating = True
        usd = float(usd_var.get())

        sr = (usd / USD_PER_1000_SR) * 1000
        gs = sr / SR_PER_GS

        sr_var.set(f"{sr:.0f}")
        gs_var.set(f"{gs:.2f}")
    except ValueError:
        sr_var.set("")
        gs_var.set("")
    updating = False


def gs_changed(*args):
    global updating
    if updating:
        return
    try:
        updating = True
        gs = float(gs_var.get())

        sr = gs * SR_PER_GS
        usd = (sr / 1000) * USD_PER_1000_SR

        sr_var.set(f"{sr:.0f}")
        usd_var.set(f"{usd:.2f}")
    except ValueError:
        sr_var.set("")
        usd_var.set("")
    updating = False

root = tk.Tk()
root.title("Currency Converter")
root.geometry("420x340")
root.resizable(False, False)
root.configure(bg=BG_COLOR)

font_label = ("Arial", 11)
font_entry = ("Arial", 16)

sr_var = tk.StringVar()
usd_var = tk.StringVar()
gs_var = tk.StringVar()

sr_var.trace_add("write", sr_changed)
usd_var.trace_add("write", usd_changed)
gs_var.trace_add("write", gs_changed)

def currency_block(title, variable):
    frame = tk.Frame(root, bg=BG_COLOR)
    frame.pack(padx=20, pady=12, fill="x")

    label = tk.Label(
        frame,
        text=title,
        font=font_label,
        fg=TEXT_COLOR,
        bg=BG_COLOR
    )
    label.pack(anchor="w")

    entry = tk.Entry(
        frame,
        textvariable=variable,
        font=font_entry,
        fg=TEXT_COLOR,
        bg=ENTRY_BG,
        insertbackground=TEXT_COLOR,
        relief="solid",
        bd=1,
        highlightthickness=1,
        highlightbackground=BORDER_COLOR,
        highlightcolor=BORDER_COLOR
    )
    entry.pack(fill="x", pady=6, ipady=6)


currency_block("SR (Shiny Rocks)", sr_var)
currency_block("USD (US Dollar)", usd_var)
currency_block("GS (Ghost Stones)", gs_var)

root.mainloop()

#   MIT License
#
#   Copyright (c) 2026 MamaMonke
#
#   Permission is hereby granted, free of charge, to any person obtaining a copy
#   of this software and associated documentation files (the "Software"), to deal
#   in the Software without restriction, including without limitation the rights
#   to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#   copies of the Software, and to permit persons to whom the Software is
#   furnished to do so, subject to the following conditions:
#
#   The above copyright notice and this permission notice shall be included in all
#   copies or substantial portions of the Software.
#
#   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#   SOFTWARE.