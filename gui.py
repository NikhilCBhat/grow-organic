import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar

class GrowOrganicGUI(tk.Tk):

    def __init__(self):
        super().__init__()
        s = ttk.Style(self)
        s.theme_use('clam')
        self.current_row = 0

        ttk.Label(self, text='Grow Organic!\n', font="Arial 20").grid(row=self.current_row, columnspan=2)
        self.current_row += 1

        self._add_calendar_widget()
        self._add_event_time_widget()
        self._add_event_type_widget()
        self._add_frequency_widget()
        ttk.Button(self, text='Schedule Event!', command=self.scheduleEvent).grid(row=self.current_row, columnspan=2)
        self.current_row += 1

    def _add_calendar_widget(self):
        self.calendar_date = None
        self.calendar_widget = Calendar(self,font="Arial 14", 
            selectmode='day',cursor="hand1", year=2020, month=10, day=5)
        self.calendar_widget.grid(row=self.current_row, columnspan=2)
        self.current_row += 1

    def _add_event_time_widget(self):
        ttk.Label(self, text='Select Time:').grid(row=self.current_row, column=0)
        self.event_time = tk.StringVar(self)
        self.event_time.set("0:00")
        tk.OptionMenu(self, self.event_time, *[f"{time}:00" for time in range(24)]).grid(row=self.current_row, column=1)
        self.current_row += 1

    def _add_event_type_widget(self):
        ttk.Label(self, text='Event Type:').grid(row=self.current_row, column=0)
        self.event_type = tk.StringVar(self)
        self.event_type.set("AERATE")
        tk.OptionMenu(self, self.event_type, *["AERATE", "WATER"]).grid(row=self.current_row, column=1)
        self.current_row += 1

    def _add_frequency_widget(self):
        ttk.Label(self, text='Frequency:').grid(row=self.current_row, column=0)
        self.frequency = tk.StringVar(self)
        self.frequency.set("n/a")
        tk.OptionMenu(self, self.frequency, *["n/a", "hourly", "daily", "weekly"]).grid(row=self.current_row, column=1)
        self.current_row += 1

    def scheduleEvent(self):
        print(
            f"Scheduling {self.event_type.get()} event on " +
            f"{self.calendar_widget.selection_get()} at {self.event_time.get()}")
        if self.frequency.get() != "n/a":
            print(f"Will repeat {self.frequency.get()}")

if __name__ == "__main__":
    gui = GrowOrganicGUI()
    gui.mainloop()