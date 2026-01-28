import tkinter as tk
from tkinter import messagebox

przychody = []   
wydatki = []     
 
def dodaj_przychod():
    try:
        kwota = float(kwota_entry.get())
        opis = opis_entry.get()
        kategoria = kategoria_var.get()
        przychody.append((kwota, opis, kategoria))
        lista.insert(tk.END, f"+ {kwota} zł | {opis} | {kategoria}")
        wyczysc_pola()
    except ValueError:
        messagebox.showerror("Błąd", "Podaj poprawną kwotę")

def dodaj_wydatek():
    try:
        kwota = float(kwota_entry.get())
        opis = opis_entry.get()
        kategoria = kategoria_var.get()
        wydatki.append((kwota, opis, kategoria))
        lista.insert(tk.END, f"- {kwota} zł | {opis} | {kategoria}")
        wyczysc_pola()
    except ValueError:
        messagebox.showerror("Błąd", "Podaj poprawną kwotę")

def pokaz_saldo():
    suma_przychodow = sum(p[0] for p in przychody)
    suma_wydatkow = sum(w[0] for w in wydatki)
    saldo = suma_przychodow - suma_wydatkow
    messagebox.showinfo("Saldo", f"Aktualne saldo: {saldo} zł")

def wyczysc_pola():
    kwota_entry.delete(0, tk.END)
    opis_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Budżet domowy v. 0.0.1")
root.geometry("600x600")
tk.Label(root, text="Kwota:").pack()
kwota_entry = tk.Entry(root)
kwota_entry.pack()
tk.Label(root, text="Opis:").pack()
opis_entry = tk.Entry(root)
opis_entry.pack()
tk.Label(root, text="Kategoria:").pack()
kategoria_var = tk.StringVar()
kategoria_var.set("Inne")
kategorie = ["Jedzenie", "Rachunki", "Transport","Edukacja","Rozrywka", "Inne"]
tk.OptionMenu(root, kategoria_var, *kategorie).pack()
tk.Button(root, text="Dodaj przychód", command=dodaj_przychod).pack(pady=5)
tk.Button(root, text="Dodaj wydatek", command=dodaj_wydatek).pack(pady=5)
tk.Button(root, text="Pokaż saldo", command=pokaz_saldo).pack(pady=10)
lista = tk.Listbox(root, width=60)
lista.pack(pady=10)

def pokaz_wykres():
    suma_przychodow = sum(p[0] for p in przychody)
    suma_wydatkow = sum(w[0] for w in wydatki)

    if suma_przychodow == 0 and suma_wydatkow == 0:
        messagebox.showinfo("Informacja", "Brak danych do wygenerowania wykresu")
        return

    import matplotlib.pyplot as plt
    etykiety = ["Przychody", "Wydatki"]
    wartosci = [suma_przychodow, suma_wydatkow]
    plt.figure()
    plt.bar(etykiety, wartosci)
    plt.title("Porównanie przychodów i wydatków")
    plt.ylabel("Kwota [zł]")
    plt.show()

tk.Button(root, text="Pokaż wykres", command=pokaz_wykres).pack(pady=5)
root.mainloop()
