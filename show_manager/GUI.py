from tkinter import *
from PIL import ImageTk

class GUI:

	
	def	__init__(self):
	
		def myfunction(event):
			canvas.configure(scrollregion=canvas.bbox("all"),width=830,height=415)
			
		def data():
			for i in range(50):
				Label(frame,text=i).grid(row=i,column=0)
				Label(frame,text="my text"+str(i)).grid(row=i,column=1)
				Label(frame,text="..........").grid(row=i,column=2)

		root = Tk()
		root.geometry("850x450")
		root.configure(background='white')
		root.title("Show Tracker")
		
		banner = Frame(root,  width = 850, height = 30, background= '#260712')
		scrolling_shows = Frame(root,  width = 850, height = 420, background= 'white')
		
		banner.grid(row=0, column=0, sticky='news')
		scrolling_shows.place(x = 0, y= 30)
		
		join_button = Button(banner, text="Settings",highlightbackground='#260712',command=lambda: settings())
		join_button.place(x=700, y=5)
		
		
		#set up scrolling show viewing area
		canvas = Canvas(scrolling_shows, background= 'white')
		frame = Frame(canvas, background = 'white')
		
		scrollbar = Scrollbar(scrolling_shows,orient ="vertical", command = canvas.yview)
		canvas.configure(yscrollcommand=scrollbar.set)
		canvas.pack(side="left")
		scrollbar.pack(side = "right", fill="y")
		
		
		
		
		
		
		
		
		def raise_frame(frame):
			frame.tkraise()
		
		def settings():
			return None
	
		raise_frame(banner)
		canvas.create_window((0,0),window=frame,anchor='nw')
		frame.bind("<Configure>",myfunction)
		data()
		root.mainloop()
if __name__ == "__main__":

	guwee = GUI()