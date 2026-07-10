import tkinter as tk

initial_balance = 10000

class ATMApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ATM Interface")
        self.balance = initial_balance

        self.balance_var = tk.StringVar(value=f"Balance: ${self.balance}")
        self.status_var = tk.StringVar(value="Welcome! Use the buttons below to operate the ATM.")

        self.build_ui()

    def build_ui(self):
        tk.Label(self.root, text="ATM Machine", font=("Segoe UI", 16, "bold")).grid(row=0, column=0, columnspan=3, pady=(10, 5))
        tk.Label(self.root, textvariable=self.balance_var, font=("Segoe UI", 14)).grid(row=1, column=0, columnspan=3, pady=(0, 15))

        tk.Label(self.root, text="Deposit Amount:").grid(row=2, column=0, sticky="e", padx=(10, 5), pady=5)
        self.deposit_entry = tk.Entry(self.root)
        self.deposit_entry.grid(row=2, column=1, columnspan=2, sticky="we", padx=(0, 10), pady=5)
        tk.Button(self.root, text="Deposit", command=self.deposit).grid(row=3, column=0, columnspan=3, sticky="we", padx=10)

        tk.Label(self.root, text="Withdraw Amount:").grid(row=4, column=0, sticky="e", padx=(10, 5), pady=5)
        self.withdraw_entry = tk.Entry(self.root)
        self.withdraw_entry.grid(row=4, column=1, columnspan=2, sticky="we", padx=(0, 10), pady=5)
        tk.Button(self.root, text="Withdraw", command=self.withdraw).grid(row=5, column=0, columnspan=3, sticky="we", padx=10)

        tk.Button(self.root, text="Check Balance", command=self.check_balance).grid(row=6, column=0, columnspan=3, sticky="we", padx=10, pady=(10, 0))
        tk.Button(self.root, text="Exit", command=self.exit_app).grid(row=7, column=0, columnspan=3, sticky="we", padx=10, pady=(5, 10))

        tk.Label(self.root, textvariable=self.status_var, wraplength=320, justify="left").grid(row=8, column=0, columnspan=3, padx=10, pady=(0, 10))

        self.root.columnconfigure(1, weight=1)

    def update_balance_label(self):
        self.balance_var.set(f"Balance: ${self.balance}")

    def check_balance(self):
        self.status_var.set(f"Current balance is ${self.balance}.")

    def deposit(self):
        amount_text = self.deposit_entry.get().strip()
        try:
            amount = float(amount_text)
            if amount <= 0:
                raise ValueError
        except ValueError:
            self.status_var.set("Enter a valid positive amount to deposit.")
            return

        self.balance += amount
        self.update_balance_label()
        self.status_var.set(f"Deposit successful! New balance: ${self.balance}.")
        self.deposit_entry.delete(0, tk.END)

    def withdraw(self):
        amount_text = self.withdraw_entry.get().strip()
        try:
            amount = float(amount_text)
            if amount <= 0:
                raise ValueError
        except ValueError:
            self.status_var.set("Enter a valid positive amount to withdraw.")
            return

        if amount > self.balance:
            self.status_var.set("Insufficient funds for that withdrawal.")
            return

        self.balance -= amount
        self.update_balance_label()
        self.status_var.set(f"Withdrawal successful! New balance: ${self.balance}.")
        self.withdraw_entry.delete(0, tk.END)

    def exit_app(self):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ATMApp(root)
    root.mainloop()
