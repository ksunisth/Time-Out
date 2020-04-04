import os
import time
import tkinter
from tkinter import *
from tkinter import messagebox

def notification(title, subtitle, mssg):

    t = '-title {!r}'.format(title)
    s = '-subtitle {!r}'.format(subtitle)
    m = '-mss {!r}'.format(mssg)

    os.system('terminal-notifier {}'.format(' '.join([m,t,s])))

root = tkinter.Tk()
root.withdraw()
lst = []

def sleep():

    root.withdraw()
    for image in lst:
        image.pack_forget()
    os.system("pmset displaysleepnow -t 20; sleep 10; caffeinate -u -t 1")

def show_image(i):

    images = {1:"",2:"Images/1.gif", 3:"Images/2.gif", 4:"Images/3.gif", 5:"Images/4.gif", 6:"Images/5.gif", 7:"Images/6.gif"}
    img= PhotoImage(file=images[i])
    img_context = Label(image=img)
    img_context.image = img
    img_context.pack()
    lst.append(img_context)

def main():

    latent_time = 1800
    time_btw_reminders = 600
    prompt_mssg = "Don't watcha screen?"
    
    messages = { 1: "It's been 30 minutes since your last break. Just look away. It's not that hard.",
                 2: "Spending hours on a computer can strain the eye muscles to cause headaches. " + 
                    "I spy a headache coming your way...",
                 3: "Bro.",
                 4: "Maybe you need some factual motivation: Your blink rate slows down when you look at things that are closer to your face (like your laptop), " + 
                    "exacerbating dry eyes and itchiness. Do you suffer from dry eyes? Now, you know why. Take a break.",
                 5: "You know.. it's been...70 minutes since your last break? What are you doing that's so time-sensitive? Or are you just lazy?",
                 6: "Wow, we've run out of sass to sass you with and that says something: You REALLY need to rest your eyes...",
                 'title': 'Screen Break!',
                 'subtitle': 'With Time-Out!',
                 'mssg_30': "It's been 30 min! Click on Yes to take a 20 sec break!",
                 'mssg_10': "It's been another 10 min! Click on Yes to take a 20 sec break!"
                 }

    number_mssgs = 6

    sass_factor = 0
    compiled = False
    while True:
        
        root.update()
        if compiled:
            notification(messages['title'], messages['subtitle'], messages['mssg_30'])
        
        if sass_factor < number_mssgs:
            show_image(sass_factor+1)
        
        root.update()
        root.deiconify()
        if tkinter.messagebox.askyesno("Time Out!!", prompt_mssg):
            compiled = True
            sleep()
            time.sleep(latent_time)
            sass_factor = 0
        else:
            compiled = False
            sass_factor +=1
            time.sleep(time_btw_reminders)
            if  sass_factor != 0:
                if sass_factor < number_mssgs:
                    notification(messages['title'], messages['subtitle'], messages['mssg_10'])
                    tkinter.messagebox.showinfo("fun FACT",  str(messages[sass_factor]))
                else:
                    notification(messages['title'], messages['subtitle'], messages['mssg_10'])
                    tkinter.messagebox.showinfo("fun FACT", str(messages[number_mssgs]))

main()


