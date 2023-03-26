import tkinter as tk

class DVD:
    def __init__(self, title, director, genre, year, id):
        self.title = title
        self.director = director
        self.genre = genre
        self.year = year
        self.id = id

def read_dvds_from_file(filename):
    dvds = []
    with open(filename, 'r') as f:
        for line in f:
            dvd_data = line.strip().split(',')
            dvd = DVD(dvd_data[0], dvd_data[1], dvd_data[2], int(dvd_data[3]), int(dvd_data[4]))
            dvds.append(dvd)
    return dvds

def save_dvds_to_file(filename, dvds):
    with open(filename, 'w') as f:
        for dvd in dvds:
            f.write(f"{dvd.title},{dvd.director},{dvd.genre},{dvd.year},{dvd.id}\n")

def sort_dvds(dvds):
    dvds.sort(key=lambda x: (x.director, x.genre, x.year))



class DVDGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("DVD Organizer")
        
        tk.Label(self.window, text="Title").grid(row=0, column=0)
        self.title_entry = tk.Entry(self.window)
        self.title_entry.grid(row=0, column=1)
        
        tk.Label(self.window, text="Director").grid(row=1, column=0)
        self.director_entry = tk.Entry(self.window)
        self.director_entry.grid(row=1, column=1)
        
        tk.Label(self.window, text="Genre").grid(row=2, column=0)
        self.genre_entry = tk.Entry(self.window)
        self.genre_entry.grid(row=2, column=1)
        
        tk.Label(self.window, text="Year").grid(row=3, column=0)
        self.year_entry = tk.Entry(self.window)
        self.year_entry.grid(row=3, column=1)
        
        tk.Button(self.window, text="Add DVD", command=self.add_dvd).grid(row=4, column=0)
        tk.Button(self.window, text="Show DVDs", command=self.show_dvds).grid(row=4, column=1)
        
        self.dvds = []
        try:
            self.dvds = read_dvds_from_file("dvds.txt")
            last_id = max([dvd.id for dvd in self.dvds])
            next_id = last_id + 1
        except:
            next_id = 1
        
        self.next_id = next_id
        
    def add_dvd(self):
        title = self.title_entry.get()
        director = self.director_entry.get()
        genre = self.genre_entry.get()
        year = int(self.year_entry.get())
        id = self.next_id
        dvd = DVD(title, director, genre, year, id)
        self.dvds.append(dvd)
        sort_dvds(self.dvds)
        save_dvds_to_file("dvds.txt", self.dvds)
        self.title_entry.delete(0, tk.END)
        self.director_entry.delete(0, tk.END)
        self.genre_entry.delete(0, tk.END)
        self.year_entry.delete(0, tk.END)
        self.next_id += 1
        
    def show_dvds(self):
        dvds_window = tk.Toplevel(self.window)
        dvds_window.title("DVDs")
        
        tk.Label(dvds_window, text="ID").grid(row=0, column=0)
        tk.Label(dvds_window, text="Name").grid(row=0, column=1)
        tk.Label(dvds_window, text="Director").grid(row=0, column=2)
        tk.Label(dvds_window, text="Genre").grid(row=0, column=3)
        tk.Label(dvds_window, text="Year").grid(row=0, column=4)
        
        for i, dvd in enumerate(self.dvds):
            tk.Label(dvds_window, text=dvd.id).grid(row=i+1, column=0)
            tk.Label(dvds_window, text=dvd.title).grid(row=i+1, column=1)
            tk.Label(dvds_window, text=dvd.director).grid(row=i+1, column=2)
            tk.Label(dvds_window, text=dvd.genre).grid(row=i+1, column=3)
            tk.Label(dvds_window, text=dvd.year).grid(row=i+1, column=4)
            
DVDGUI().window.mainloop()

