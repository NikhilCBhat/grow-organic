import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar

class GrowOrganicGUI(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        s = ttk.Style(self)
        s.theme_use('clam')
        self.calendar_date = None
        ttk.Button(self, text='Input Date', command=self.getDate).grid(row=0, columnspan=2)
        ttk.Label(self, text='Event Type:').grid(row=1, column=0)
        ttk.Entry(self).grid(row=1, column=1)
        ttk.Button(self, text='Schedule Event!', command=self.scheduleEvent).grid(row=2, columnspan=2)
    
    def set_date(self):
        self.calendar_date = self.cal.selection_get()

    def getDate(self):
        top = tk.Toplevel(self)

        self.cal = Calendar(top,
                    font="Arial 14", selectmode='day',
                    cursor="hand1", year=2020, month=10, day=5)
        self.cal.pack(fill="both", expand=True)
        ttk.Button(top, text="ok", command=self.set_date).pack()
        
    def scheduleEvent(self):
        print(f"Scheduling event on {self.calendar_date}")


if __name__ == "__main__":
    gui = GrowOrganicGUI()
    gui.mainloop()