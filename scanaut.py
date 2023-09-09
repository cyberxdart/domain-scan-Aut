import subprocess
import tkinter as tk
from tkinter import messagebox
def run_scanner(domain, sub_domain):
    for subdomain in sub_domain:
        # Making URL by putting subdomain one by one
        url = f"https://{subdomain}.{domain}"
        try:
            # Run command and capture the output
            domain_output = subprocess.check_output(['Domain', 'enum', url])
            # Convert the output to a string
            domain_output_str = domain_output.decode('utf-8')
            # Display a message box with the amass output
            messagebox.showinfo('Domain Results', domain_output_str)
        except subprocess.CalledProcessError as e:
            messagebox.showerror('Error', str(e))
def on_scanner_submit():
    domain = domain_entry.get()
    file_path = "directory.txt"
    file = open(file_path,"r",encoding="utf-8")       
        # reading the file
    name = file.read() 
        # using splitlines() function storing the list
        # of splitted strings
    sub_domain = name.splitlines()
    run_scanner(domain,sub_domain)
# Create the main window
window = tk.Tk()
window.geometry("400x400")
window.title('Automation Interface')

# Create the  section
domain_label = tk.Label(window, text='Scanner - Enter Domain:')
domain_label.grid(row = 1,column=1) # width x height
domain_label.config(bg="green")
domain_entry = tk.Entry(window)
domain_entry.grid(row = 2,column=1)
domain_submit_button = tk.Button(window, text='Run Scanner', command=on_scanner_submit)
domain_submit_button.grid(row=3,column=1)
# Start the GUI event loop
window.mainloop() #(for execution of event in tkinter window)

