import tkinter as Tkinter
import tkinter.ttk as ttk
import datetime
import os
from time import sleep



# Creating Clock Main Class
class Clock(Tkinter.Tk):
 def __init__(self, *args, **kwargs):
  Tkinter.Tk.__init__(self, *args, **kwargs)
  self['padx'] = 20
  self['pady'] = 20
  # Creating Variables
  self.waiting_str_var = Tkinter.IntVar()
  self.show_alarm_time = Tkinter.StringVar()
  self.show_alarm_time.set(datetime.datetime.now().ctime())
  self.alarm_delta_time = None
  self.create_first_label()
  self.create_second_box()



 # creating 'set alarm time' Label
 def create_first_label(self):
  ttk.Label(self, textvariable=self.show_alarm_time, font=("arial 20 bold")).grid(row=0, column=1, columnspan=2, padx=10, pady=10)
  return



 # creates keypad
 def create_second_box(self):
  ttk.Label(self, text="Wait For Seconds : ").grid(row=1, column=1, padx=10, pady=10)
  ttk.Entry(self, textvariable=self.waiting_str_var).grid(row=1, column=2, padx=10, pady=10)
  ttk.Button(self, text="Exit", command=self.destroy).grid(row=3, column=1, padx=10, pady=10)
  ttk.Button(self, text="Set Alarm!", command=self.set_alarm_button).grid(row=3, column=2, padx=10, pady=10)
  return



 # Set alarm function
 def set_alarm_button(self):
  try:
   sec = self.waiting_str_var.get()
   self.alarm_delta_time = datetime.datetime.now()+datetime.timedelta(seconds=sec)
   self.show_alarm_time.set(self.alarm_delta_time.ctime().__str__())
  except:
   self.waiting_str_var.set(0)
  return



 # updates loop
 def regular_update(self):
  self.update()
  self.update_idletasks()
  if self.alarm_delta_time:
   if datetime.datetime.now() > self.alarm_delta_time:
    print("Wake up")
    for i in range(5):
        print(chr(7)),
        sleep(1)
  return



root = Clock(className=" Alarm Clock")
while True:
    root.regular_update()
