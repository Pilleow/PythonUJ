import random
import tkinter as tk

from PIL import Image, ImageTk


def spin():
    symbols = [random.randint(1, 5) for _ in range(3)]
    result_label.config(text="", fg="#000000")

    def update_labels(step=0):
        if step < 20:
            label1.config(text=str(random.randint(1, 5)))
            label2.config(text=str(random.randint(1, 5)))
            label3.config(text=str(random.randint(1, 5)))
            root.after(50, update_labels, step + 1)
        else:
            label1.config(text=str(symbols[0]))
            label2.config(text=str(symbols[1]))
            label3.config(text=str(symbols[2]))

            if symbols[0] == symbols[1] == symbols[2]:
                result_label.config(text="\u2728 Wygrana! \u2728", fg="#32CD32")
            elif len(set(symbols)) == 2:
                result_label.config(text="Prawie ci się udało", fg="#FF6347")
            else:
                result_label.config(text="Spróbuj ponownie", fg="#FF6347")

    update_labels()


def confirm_exit():
    exit_window = tk.Toplevel(root)
    exit_window.title("Drogi Użytkowniku")
    exit_window.configure(bg="#FFFFFF")

    img = Image.open("exit_image.png").resize((300, 300))
    img = ImageTk.PhotoImage(img)
    img_label = tk.Label(exit_window, image=img, bg="#FFFFFF")
    img_label.image = img
    img_label.pack(pady=10)

    question_label = tk.Label(
        exit_window, text="Czy na pewno chcesz wyjść?",
        font=("Arial", 14), bg="#FFFFFF"
    )
    question_label.pack(pady=10)

    def on_confirm():
        root.destroy()

    def on_cancel():
        exit_window.destroy()

    confirm_button = tk.Button(
        exit_window, text="Tak", font=("Arial", 10),
        bg="#FFFFFF", fg="#000000",command=on_confirm
    )
    confirm_button.pack(side="left", expand=True, padx=20, pady=20)

    cancel_button = tk.Button(
        exit_window, text="Nie", font=("Arial", 24),
        bg="#4CAF50", fg="#FFFFFF", command=on_cancel
    )
    cancel_button.pack(side="right", expand=True, padx=20, pady=20)


root = tk.Tk()
root.title("Jednoręki Bandyta")
root.resizable(False, False)
root.configure(bg="#1E1E2F")
root.protocol("WM_DELETE_WINDOW", confirm_exit)

label1 = tk.Label(root, text="-", font=("Arial", 32), width=5, relief="ridge", bg="#FFD700", fg="#000000")
label1.grid(row=0, column=0, padx=10, pady=10)

label2 = tk.Label(root, text="-", font=("Arial", 32), width=5, relief="ridge", bg="#FFD700", fg="#000000")
label2.grid(row=0, column=1, padx=10, pady=10)

label3 = tk.Label(root, text="-", font=("Arial", 32), width=5, relief="ridge", bg="#FFD700", fg="#000000")
label3.grid(row=0, column=2, padx=10, pady=10)

spin_button = tk.Button(root, text="SPIN", font=("Arial", 16, "bold"), bg="#4CAF50", fg="#FFFFFF", relief="raised",
                        bd=3, command=spin)
spin_button.grid(row=1, column=0, columnspan=3, pady=20)

result_label = tk.Label(root, text="", font=("Arial", 20), bg="#1E1E2F", fg="#FFFFFF")
result_label.grid(row=2, column=0, columnspan=3, pady=10)

root.mainloop()
