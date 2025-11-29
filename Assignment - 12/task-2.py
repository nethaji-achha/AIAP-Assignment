import tkinter as tk
from tkinter import messagebox

def bubble_sort(arr):
    n = len(arr)
    sorted_arr = arr.copy()
    for i in range(n):
        for j in range(0, n-i-1):
            if sorted_arr[j] > sorted_arr[j+1]:
                sorted_arr[j], sorted_arr[j+1] = sorted_arr[j+1], sorted_arr[j]
    return sorted_arr

def sort_clicked():
    input_str = entry.get()
    try:
        arr = [int(x) for x in input_str.strip().split()]
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter integers separated by spaces.")
        return
    result = bubble_sort(arr)
    output_var.set("Sorted Output: " + ' '.join(map(str, result)))

root = tk.Tk()
root.title("Bubble Sort")

tk.Label(root, text="Enter numbers (space-separated):").pack(pady=5)
entry = tk.Entry(root, width=40)
entry.pack(pady=5)

tk.Button(root, text="Bubble Sort", command=sort_clicked).pack(pady=10)

output_var = tk.StringVar()
output_label = tk.Label(root, textvariable=output_var, fg="blue")
output_label.pack(pady=5)

root.mainloop()
