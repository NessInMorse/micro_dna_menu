from tkinter import Tk, Frame, Button, mainloop, Label, messagebox, Entry, StringVar
from random import randint, choice

saved=""
class DnaMenu:
        def __init__(self):
                self.main_window = Tk()

                self.input_frame = Frame(self.main_window)
                self.menu_frame = Frame(self.main_window)
                self.output_frame = Frame(self.main_window)


                self.dna_entry = Entry(self.input_frame,width=10)
                self.value = StringVar()

                
                self.insertion = Button(self.menu_frame,
                                        text="Insert random base",
                                        command=self.insertion)
                
                self.reverse = Button(self.menu_frame,
                                        text="Reverse String",
                                        command=self.reverse)
                
                self.mutate = Button(self.menu_frame,
                                        text="Mutate Random base",
                                        command=self.mutate)
                
                self.complement = Button(self.menu_frame,
                                        text="Show Complementary String",
                                        command=self.complement)
                
                self.reset = Button(self.menu_frame,
                                        text="Reset current input",
                                        command=self.reset)

                self.quit = Button(self.menu_frame,
                                        text="Quit session",
                                        command=self.main_window.destroy)



                self.output = Label(self.output_frame,
                                    textvariable=self.value)

                self.dna_entry.pack(side="left")
                self.insertion.pack(side="top")
                self.reverse.pack(side="top")
                self.mutate.pack(side="top")
                self.complement.pack(side="top")
                self.reset.pack(side="top")
                self.quit.pack(side="top")
                self.output.pack(side="top")

                self.input_frame.pack()
                self.menu_frame.pack()
                self.output_frame.pack()

        def reset(self):
                global saved
                saved=""
                self.value.set(saved)
                

        def insertion(self):
                global saved
                if saved=="":
                        dna = self.dna_entry.get()
                else:
                        dna=saved
                change_index=randint(0,len(dna)-1)
                dna=list(dna)
                
                dna[change_index]+=choice(["A","C","G","T"])

                dna="".join(dna)
                
                self.value.set(dna)
                saved=dna

        def reverse(self):
                global saved
                if saved=="":
                        dna = self.dna_entry.get()
                else:
                        dna=saved
                self.value.set(dna[::-1])
                saved=dna[::-1]



        def mutate(self):
                global saved
                if saved=="":
                        dna = self.dna_entry.get()
                else:
                        dna=saved
                dna_mutated=dna
                m_r=randint(1,len(dna))
                while dna_mutated==dna:
                        dna_mutated=dna_mutated[:m_r-1]+choice(["A","C","G","T"])+dna_mutated[m_r:]
                self.value.set(dna_mutated)
                saved=dna_mutated

        def complement(self):
                global saved
                if saved=="":
                        dna = self.dna_entry.get()
                else:
                        dna=saved

                 

                saved = "".join([["A","C","G","T"]\
                                [3-["A","C","G","T"].index(i)]\
                                  for i in dna])
                self.value.set(saved)



dna_menu = DnaMenu()
