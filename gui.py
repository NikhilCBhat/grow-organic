import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar

class GrowOrganicGUI(tk.Tk):

    def __init__(self):
        super().__init__()
        s = ttk.Style(self)
        s.theme_use('clam')

        ttk.Label(self, text='Grow Organic!\n', font="Arial 20").grid(row=0, columnspan=2)
        self._add_calendar_widget()
        self._add_event_time_widget()
        self._add_event_type_widget()
        ttk.Button(self, text='Schedule Event!', command=self.scheduleEvent).grid(row=4, columnspan=2)

    def _add_calendar_widget(self):
        self.calendar_date = None
        self.calendar_widget = Calendar(self,font="Arial 14", 
            selectmode='day',cursor="hand1", year=2020, month=10, day=5)
        self.calendar_widget.grid(row=1, columnspan=2)

    def _add_event_time_widget(self):
        ttk.Label(self, text='Select Time:').grid(row=2, column=0)
        self.event_time = tk.StringVar(self)
        self.event_time.set("0:00")
        tk.OptionMenu(self, self.event_time, *[f"{time}:00" for time in range(24)]).grid(row=2, column=1)

    def _add_event_type_widget(self):
        ttk.Label(self, text='Event Type:').grid(row=3, column=0)
        self.event_type = tk.StringVar(self)
        self.event_type.set("AERATE")
        tk.OptionMenu(self, self.event_type, *["AERATE", "WATER"]).grid(row=3, column=1)

    def scheduleEvent(self):
        print(
            f"Scheduling {self.event_type.get()} event on " +
            f"{self.calendar_widget.selection_get()} at {self.event_time.get()}")


if __name__ == "__main__":
    gui = GrowOrganicGUI()
    gui.mainloop()