import tkinter as tk
from tkinter import ttk, messagebox
from inventory import add_item, remove_item, load_inventory, search_item

class InventoryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Store Inventory Manager")
        self.root.geometry("800x500")

        self.create_widgets()
        self.update_table(load_inventory())

    def create_widgets(self):
        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Item Name").grid(row=0, column=0, padx=5)
        self.name_entry = tk.Entry(input_frame)
        self.name_entry.grid(row=0, column=1)

        tk.Label(input_frame, text="Quantity").grid(row=0, column=2, padx=5)
        self.quantity_entry = tk.Entry(input_frame)
        self.quantity_entry.grid(row=0, column=3)

        tk.Label(input_frame, text="Comment").grid(row=0, column=4, padx=5)
        self.comment_entry = tk.Entry(input_frame, width=20)
        self.comment_entry.grid(row=0, column=5)

        tk.Label(input_frame, text="Threshold").grid(row=0, column=6, padx=5)
        self.threshold_entry = tk.Entry(input_frame, width=5)
        self.threshold_entry.grid(row=0, column=7)

        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=5)

        tk.Button(btn_frame, text="Add Item", command=self.add_item).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Remove Item", command=self.remove_item).grid(row=0, column=1, padx=5)

        tk.Label(btn_frame, text="Search:").grid(row=0, column=2, padx=5)
        self.search_entry = tk.Entry(btn_frame)
        self.search_entry.grid(row=0, column=3)
        tk.Button(btn_frame, text="Find", command=self.search_item).grid(row=0, column=4, padx=5)
        tk.Button(btn_frame, text="Show All", command=self.show_all).grid(row=0, column=5, padx=5)
        tk.Button(btn_frame, text="Low Stock Only", command=self.show_low_stock).grid(row=0, column=6, padx=5)

        self.tree = ttk.Treeview(self.root, columns=('Item Name', 'Quantity', 'Comment', 'Low Stock Threshold'), show='headings')
        for col in ('Item Name', 'Quantity', 'Comment', 'Low Stock Threshold'):
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150 if col == 'Comment' else 100)
        self.tree.pack(fill=tk.BOTH, expand=True, pady=10)

    def update_table(self, data):
        self.tree.delete(*self.tree.get_children())
        for item in data:
            qty = int(item['Quantity'])
            threshold = int(item.get('Low Stock Threshold', '5'))
            tag = 'low' if qty < threshold else ''
            self.tree.insert('', 'end', values=(
                item['Item Name'], item['Quantity'], item['Comment'], item['Low Stock Threshold']
            ), tags=(tag,))
        self.tree.tag_configure('low', background='lightcoral')

    def add_item(self):
        name = self.name_entry.get().strip()
        qty = self.quantity_entry.get().strip()
        comment = self.comment_entry.get().strip()
        threshold = self.threshold_entry.get().strip()

        if not name or not qty.isdigit() or not threshold.isdigit():
            messagebox.showerror("Error", "Invalid input.")
            return

        add_item(name, qty, comment, threshold)
        self.show_all()
        self.clear_inputs()

    def remove_item(self):
        name = self.name_entry.get().strip()
        qty = self.quantity_entry.get().strip()

        if not name or not qty.isdigit():
            messagebox.showerror("Error", "Invalid input.")
            return

        remove_item(name, qty)
        self.show_all()
        self.clear_inputs()

    def search_item(self):
        keyword = self.search_entry.get().strip()
        results = search_item(keyword)
        self.update_table(results)

    def show_all(self):
        self.update_table(load_inventory())

    def show_low_stock(self):
        data = load_inventory()
        low_stock = []
        for item in data:
            qty = int(item['Quantity'])
            threshold = int(item.get('Low Stock Threshold', '5'))
            if qty < threshold:
                low_stock.append(item)
        self.update_table(low_stock)

    def clear_inputs(self):
        self.name_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)
        self.comment_entry.delete(0, tk.END)
        self.threshold_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryApp(root)
    root.mainloop()
