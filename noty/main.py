import tkinter as tk
from recognize import Recognizer

def cli():
    import time
    current_time = time.strftime("%H:%M")
      # gets the current time.
    print("Welcome to Noty.You can now create sticky notes, easily.")
    time.sleep(2)
    
    root = tk.Tk()
    root.title("Noty")
    root.geometry("300x300")

    print("\n\n")
    note_input = input("Do you want to open previous notes? (Y/N)")
    print("hell0o\n")

    if note_input == "Y" or note_input == "y":
        # note_input = input("Which note do you want to open?")
        # do security
        name = input("Are you Carter lack? (Y/N")
        if name != "Y" or note_input != "y":
            security_check = Recognizer().recognize_carter()
            if security_check == True:
                root = tk.Tk()
                root.title("Noty")
                root.geometry("300x300")
                # changes the width and height of the GUI.
                tk.Label(root, text=current_time).pack()
                # prints the current time.
                f = open("noty/saved_notes/note.txt")
                note = f.read()
                tk.Label(root, text=note).pack()
                f.close()
            else:
                print("Security Check failed, bye!\n")
    
    else:
        # changes the width and height of the GUI.
        tk.Label(root, text=current_time).pack()
        # prints the current time.

        note_input = input("Type your notes here: ")
        note = ("*%s") % note_input
        time.sleep(1)
        # time.sleep prevents GUI from popping up before it receives input.
        tk.Label(root, text=note).pack()
        # saves the note to the notes folder
        f = open("noty/saved_notes/note.txt", "w+")
        f.write(note)
        f.close()
        # prints the input.
    root.mainloop()
    # keeps showing the note, until the user closes it.


cli()
