import sqlite3

def create_database():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY,
                    task TEXT NOT NULL,
                    completed BOOLEAN NOT NULL
                )''')
    conn.commit()
    conn.close()

create_database()

import tkinter as tk

def create_gui():
    window = tk.Tk()
    window.title('To-Do List App')
    window.geometry('400x300')

    entry = tk.Entry(window, width=30)
    entry.pack()

    def add_task():
        task = entry.get()
        if task != '':
            conn = sqlite3.connect('todo.db')
            c = conn.cursor()
            c.execute("INSERT INTO tasks (task, completed) VALUES (?, ?)", (task, False))
            conn.commit()
            conn.close()
            entry.delete(0, tk.END)
            get_tasks()

    add_button = tk.Button(window, text='Add Task', command=add_task)
    add_button.pack()

    def get_tasks():
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        tasks = c.execute("SELECT * FROM tasks ORDER BY completed ASC, id DESC").fetchall()
        conn.close()

        for task in tasks:
            # Create a new label for each task
            label = tk.Label(window, text=task[1], font=('Helvetica', 12), wraplength=200)
            label.pack()

    get_tasks()

    window.mainloop()

create_gui()