from back_end import BackEnd
from tkinter import *
from PIL import ImageTk
import webbrowser

class GUI:

	
	def	__init__(self):
		self.backend = BackEnd()
	
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
		settings_frame = Frame(root,  width = 250, height = 300, highlightbackground="black",\
		highlightcolor="black", highlightthickness=5, background= 'white')
		add_frame = Frame(root,  width = 600, height = 300, highlightbackground="black",\
		highlightcolor="black", highlightthickness=5, background= 'white')

		category_frame = Frame(root,  width = 600, height = 60, highlightbackground="black",\
		highlightcolor="black", highlightthickness=5, background= 'white')
		
		#place main frames
		banner.grid(row=0, column=0, sticky='news')
		scrolling_shows.place(x = 0, y= 30)
		settings_frame.place(x = 300, y = 40)
		add_frame.place(x = 110, y = 40)
		category_frame.place(x = 110, y = 30)
		
		
		#create banner buttons
		settings_button = Button(banner, highlightbackground='#260712',command=lambda: settings())
		settings_button.place(x=800, y=0)
		settings_image = ImageTk.PhotoImage(file = "settings.png")
		settings_button.config(image = settings_image)
		
		garbage_button = Button(banner, highlightbackground='#260712',command=lambda: settings())
		garbage_button.place(x=760, y=0)
		garbage_image = ImageTk.PhotoImage(file = "garbage.png")
		garbage_button.config(image = garbage_image)
		
		category_button = Button(banner, highlightbackground='#260712',command=lambda: category())
		category_button.place(x=712, y=0)
		category_image = ImageTk.PhotoImage(file = "category.png")
		category_button.config(image = category_image)
		
		add_button = Button(banner, highlightbackground='#260712',command=lambda: add())
		add_button.place(x=670, y=0)
		add_image = ImageTk.PhotoImage(file = "add.png")
		add_button.config(image = add_image)
		
		#widgets inside frame to add new show
		tag_label = Label(add_frame, text = "Tag")
		tag_label.place(x = 20, y = 10)
		tag_label.config(font=("Courier", 21, 'bold'))
		
		tag = StringVar()
		tag_entry = Entry(add_frame,highlightbackground='black',width = 50, textvariable=tag)
		tag_entry.place(x=20, y=40)
		
		HTTP_label = Label(add_frame, text = "HTTP Address of Show You're Watching")
		HTTP_label.place(x = 20, y = 80)
		HTTP_label.config(font=("Courier", 21, 'bold'))
		
		HTTP = StringVar()
		HTTP_entry = Entry(add_frame,highlightbackground='black',width = 50, textvariable=HTTP)
		HTTP_entry.place(x=20, y=110)
		
		categories_label = Label(add_frame, text = "Add to Additional Categories")
		categories_label.place(x = 20, y = 150)
		categories_label.config(font=("Courier", 21, 'bold'))
		
		exit_add_button = Button(add_frame, highlightbackground='#260712',command=lambda: exit())
		exit_add_button.place(x=555, y=0)
		exit_image = ImageTk.PhotoImage(file = "exit.png")
		exit_add_button.config(image = exit_image)
		
		check_boxes = Frame(add_frame,  width = 400, height = 100, highlightbackground="black",\
		highlightcolor="black", highlightthickness=5, background= 'white')
		check_boxes.place(x = 20, y = 180)
		
		
		cat_row =0
		cat_col =0
		check_dict = dict()
		button_list = []
		var_list = []
		for category in self.backend._category_list.keys():
			#if category != "General" and category != "New":
			check_var = IntVar()
			check_button = Checkbutton(check_boxes, text = category, \
                 onvalue = 1, offvalue = 0, height=1, \
                 width = 15)
			check_button.grid(row = cat_row, column = cat_col)
			button_list.append(check_button)
			check_dict[category] = check_var
			cat_row += 1
			if cat_row == 4:
				cat_col+= 1
				cat_row = 0
			#var_list.append(check_var)
			check_dict[category] = check_var
		
		add_show_button = Button(add_frame,text = "Add Show",command=lambda: add_show())
		add_show_button.place(x=490, y=250)
		
		#widgets inside frame to add new category
		category_label = Label(category_frame, text = "Add New Category")
		category_label.place(x = 20, y = 0)
		category_label.config(font=("Courier", 18, 'bold'))
		
		new_category = StringVar()
		category_entry = Entry(category_frame, highlightbackground='black',width = 50, textvariable=new_category)
		category_entry.place(x=20, y=20)
		
		exit_category_button = Button(category_frame, highlightbackground='#260712',command=lambda: exit())
		exit_category_button.place(x=555, y=0)
		exit_category_button.config(image = exit_image)
		
		add_category_button = Button(category_frame,text = "Add",command=lambda: add_category())
		add_category_button.place(x=490, y=20)
		
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
			raise_frame(scrolling_shows)
			raise_frame(settings_frame)
			
		def add():
			raise_frame(scrolling_shows)
			raise_frame(add_frame)
		
		def category():
			raise_frame(scrolling_shows)
			raise_frame(category_frame)
			
		def exit():
			raise_frame(scrolling_shows)
			
		def add_show():
			return None
			
		def add_category():
			shows = None
			self.backend.add_category(category_entry.get(), shows)
			category_entry.delete(0, END)
			exit()
	
		raise_frame(banner)
		raise_frame(scrolling_shows)
		canvas.create_window((0,0),window=frame,anchor='nw')
		frame.bind("<Configure>",myfunction)
		data()
		root.mainloop()
if __name__ == "__main__":

	guwee = GUI()