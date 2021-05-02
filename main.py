import tkinter as tk
from tkinter import simpledialog
from recognize import Recognizer
import os



class NoteApp():

    def run_app(self):
        import time
        current_time = time.strftime("%H:%M")
        # gets the current time.
        print("Welcome to Carter's Secure Note App.")
        time.sleep(2)
        
        root = tk.Tk()
        root.title("Noty")
        root.geometry("500x300")

        print("\n\n")
        note_input = input("Do you want to open previous notes? (Y/N)")
        print("hell0o\n")

        if note_input == "Y" or note_input == "y":
            # note_input = input("Which note do you want to open?")
            # do security
            name = input("Are you Carter lack? (Y/N")
            if name != "Y" or name != "y":
                security_check = Recognizer().recognize_carter()
                if security_check == True:
                    root = tk.Tk()
                    root.title("Noty")
                    root.geometry("300x300")
                    # changes the width and height of the GUI.
                    tk.Label(root, text=current_time).pack()
                    #
                    found = False
                    thing = simpledialog.askstring(title="Which file do you want to open?", prompt="What is the name of the file you want to open?")
                    while not found:
                        # look for the file name
                        for file in os.listdir("noty/saved_notes"):
                            file_text = self.open_file(root, file, thing)
                            if file_text != 0:
                                found = True
                                break
                        # Make popup if file is not found
                        if found == False:
                            thing = simpledialog.askstring(title="Error", prompt="This file doesn't exist, please re enter the file name (without extensions)")   
                else:
                    print("Security Check failed, bye!\n")
                    return
                
        
        # We are trying to make a new note
        else:

            # changes the width and height of the GUI.
            tk.Label(root, text=current_time).pack()
            # prints the current time.
            note_box = tk.Text(root, width = 50, height = 30)
            note_box.pack()

            save_button = tk.Button(root, text= "save note", command = lambda: self.save_note(note_box, root))
            save_button.place(x= 0, y =0)
            save_button.pack()

                     # saves the note to the notes folder
            # prints the input.
        root.mainloop()
        # keeps showing the note, until the user closes it.

    def open_file(self, root, file, thing):
        filename = os.fsdecode(file)
        print(filename)
        print(filename.startswith(thing))
        if filename.startswith(thing):
            # prints the current time.
            f = open("noty/saved_notes/" + thing + ".txt")
            note = f.read()
            tk.Label(root, text=note).pack()
            f.close()
            print("Returning 1")
            return note
        return 0

    def save_note(self, note_box, root):
        # 1. get the current text from the note box
        # 2. name the file something the user wants
        # 3. save the text into a .txt file
        note_text = note_box.get("1.0", "end")
        file_name = simpledialog.askstring(title="asking stuff", prompt="Please name your note file")
        path = "noty/saved_notes/" + file_name + ".txt"
        new_note_file = open(path, "w+")
        new_note_file.write(note_text)
        new_note_file.close()


if __name__ == "__main__":    
    NoteApp().run_app()
