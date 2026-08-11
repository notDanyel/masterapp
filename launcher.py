import tkinter as tk
import subprocess

root = tk.Tk()
root.title("Danyel's Project Launcher")

# buttons go here
def dodge_clicked():
    print("Dodge Forever Clicked")
    subprocess.run(["python", "C:/Users/danye/PycharmProjects/PythonProject3/main.py"], cwd="C:/Users/danye/PycharmProjects/PythonProject3")
def csvtool_clicked():
    print("CSV Tool Clicked")
    subprocess.run(["python", "C:/Users/danye/PycharmProjects/24R07PythonExpert/lesson3/csv_file_manager.py"], cwd="C:/Users/danye/PycharmProjects/24R07PythonExpert/lesson3")
def scraper_clicked():
    print("Scraper Clicked")
    subprocess.run(["python", "C:/Users/danye/PycharmProjects/24R07PythonExpert/lesson6/parse_welcome_page.py"], cwd="C:/Users/danye/PycharmProjects/24R07PythonExpert/lesson6")
dodgeForever = tk.Button(root, text="Dodge Forever", command=dodge_clicked)
dodgeForever.pack()

csvTool = tk.Button(root, text="TXT to CSV", command=csvtool_clicked)
csvTool.pack()

scraper = tk.Button(root, text="Web Scraper", command=scraper_clicked)
scraper.pack()


root.mainloop()