import tkinter as tk

initial_balance = 10000

class ATMApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bank ATM")
        self.root.configure(bg="#2b2f3d")
        self.balance = initial_balance
        self.entered_amount = ""

        self.balance_var = tk.StringVar(value=f"Balance: ${self.balance}")
        self.screen_var = tk.StringVar(value="Welcome! Enter an amount and choose an action.")
        self.input_var = tk.StringVar(value="")

        self.build_ui()

    def build_ui(self):
        self.root.geometry("420x560")
        self.root.resizable(False, False)

        title = tk.Label(self.root, text="BANK ATM", font=("Helvetica", 18, "bold"), bg="#1f242f", fg="#f1f3f6", bd=2, relief="ridge")
        title.pack(fill="x", padx=12, pady=(12, 6))

        screen_frame = tk.Frame(self.root, bg="#0d111b", bd=4, relief="sunken")
        screen_frame.pack(fill="x", padx=12, pady=(0, 10))

        tk.Label(screen_frame, textvariable=self.balance_var, font=("Arial", 14, "bold"), bg="#0d111b", fg="#b8d6ff").pack(padx=12, pady=(10, 5), anchor="w")
        tk.Label(screen_frame, textvariable=self.screen_var, font=("Arial", 12), bg="#0d111b", fg="#e6e6e6", wraplength=380, justify="left").pack(padx=12, pady=(0, 12))

        entry_frame = tk.Frame(self.root, bg="#2b2f3d")
        entry_frame.pack(fill="x", padx=12)

        tk.Label(entry_frame, text="Amount", font=("Arial", 11, "bold"), bg="#2b2f3d", fg="#f1f3f6").grid(row=0, column=0, sticky="w", pady=(0, 5))
        self.amount_display = tk.Entry(entry_frame, textvariable=self.input_var, font=("Arial", 16), justify="right", state="readonly", readonlybackground="#1c1f27", fg="#ffffff", bd=2, relief="sunken")
        self.amount_display.grid(row=1, column=0, columnspan=3, sticky="we", pady=(0, 10))

        control_frame = tk.Frame(self.root, bg="#2b2f3d")
        control_frame.pack(fill="x", padx=12, pady=(0, 10))

        self.create_side_button(control_frame, "BALANCE", self.check_balance).grid(row=0, column=0, sticky="we", padx=(0, 6))
        self.create_side_button(control_frame, "DEPOSIT", self.deposit).grid(row=0, column=1, sticky="we", padx=6)
        self.create_side_button(control_frame, "WITHDRAW", self.withdraw).grid(row=0, column=2, sticky="we", padx=6)
        self.create_side_button(control_frame, "EXIT", self.exit_app).grid(row=0, column=3, sticky="we", padx=(6, 0))

        keypad_frame = tk.Frame(self.root, bg="#2b2f3d")
        keypad_frame.pack(padx=12, pady=(0, 10))

        buttons = [
            ("1", 0, 0), ("2", 0, 1), ("3", 0, 2),
            ("4", 1, 0), ("5", 1, 1), ("6", 1, 2),
            ("7", 2, 0), ("8", 2, 1), ("9", 2, 2),
            ("C", 3, 0), ("0", 3, 1), ("⌫", 3, 2)
        ]

        for (text, row, col) in buttons:
            action = self.key_pressed
            tk.Button(keypad_frame, text=text, command=lambda t=text: action(t), width=8, height=3, bg="#3c4353", fg="#f1f3f6", font=("Arial", 11, "bold"), bd=2, relief="raised").grid(row=row, column=col, padx=4, pady=4)

        status_frame = tk.Frame(self.root, bg="#0d111b", bd=3, relief="ridge")
        status_frame.pack(fill="x", padx=12, pady=(0, 12))
        tk.Label(status_frame, text="ATM Status", font=("Arial", 12, "bold"), bg="#0d111b", fg="#b8d6ff").pack(anchor="w", padx=10, pady=(8, 0))
        tk.Label(status_frame, textvariable=self.screen_var, font=("Arial", 11), bg="#0d111b", fg="#e6e6e6", wraplength=380, justify="left").pack(anchor="w", padx=10, pady=(4, 10))

        self.root.columnconfigure(0, weight=1)
        self.root.bind_all("<Key>", self.on_key_press)

    def create_side_button(self, parent, text, command):
        return tk.Button(parent, text=text, command=command, bg="#4f5a76", fg="#ffffff", font=("Arial", 10, "bold"), bd=2, relief="raised", height=2)

    def update_balance_label(self):
        self.balance_var.set(f"Balance: ${self.balance}")

    def get_entered_amount(self):
        amount_text = self.input_var.get().strip()
        if not amount_text:
            self.screen_var.set("Please enter an amount using the keypad.")
            return None
        try:
            amount = float(amount_text)
            if amount <= 0:
                raise ValueError
            return amount
        except ValueError:
            self.screen_var.set("Enter a valid positive amount using the keypad.")
            return None

    def check_balance(self):
        self.screen_var.set(f"Current balance is ${self.balance}.")

    def deposit(self):
        amount = self.get_entered_amount()
        if amount is None:
            return
        self.balance += amount
        self.update_balance_label()
        self.screen_var.set(f"Deposit successful! New balance: ${self.balance}.")
        self.clear_input()

    def withdraw(self):
        amount = self.get_entered_amount()
        if amount is None:
            return
        if amount > self.balance:
            self.screen_var.set("Insufficient funds for that withdrawal.")
            return
        self.balance -= amount
        self.update_balance_label()
        self.screen_var.set(f"Withdrawal successful! New balance: ${self.balance}.")
        self.clear_input()

    def clear_input(self):
        self.entered_amount = ""
        self.input_var.set("")
        self.screen_var.set("Amount cleared. Enter new value or choose an action.")

    def key_pressed(self, key):
        if key == "C":
            self.clear_input()
            return
        if key == "⌫":
            self.entered_amount = self.entered_amount[:-1]
        else:
            self.entered_amount += key
        self.input_var.set(self.entered_amount)

    def on_key_press(self, event):
        if event.keysym.isdigit():
            self.entered_amount += event.keysym
            self.input_var.set(self.entered_amount)
        elif event.keysym in ["BackSpace", "Delete"]:
            self.entered_amount = self.entered_amount[:-1]
            self.input_var.set(self.entered_amount)
        elif event.keysym in ["Return", "KP_Enter"]:
            self.screen_var.set("Press DEPOSIT or WITHDRAW after entering amount.")
        elif event.keysym.lower() == "c":
            self.clear_input()

    def exit_app(self):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ATMApp(root)
    root.mainloop()
