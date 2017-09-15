from back_end import BackEnd
from tkinter import *
from PIL import ImageTk
import webbrowser

class GUI:

	
	def	__init__(self):
		self.backend = BackEnd()
	
		def myfunction(event):
			canvas.configure(scrollregion=canvas.bbox("all"),width=830,height=415)
		
		#establish check boxes in addshow frame, changes upon add and delete of category
		def set_check_boxes():
			#Set up check boxes in add show fram
			check_boxes = Frame(add_frame,  width = 400, height = 100, background= 'white')
			check_boxes.place(x = 20, y = 180)
		
			cat_row =0
			cat_col =0
			check_dict = dict()
			var_list = []
			for category in self.backend._category_list.keys():
				#if category != "General" and category != "New":
				check_var = IntVar()
				check_button = Checkbutton(check_boxes, text = category, \
					 onvalue = 1, offvalue = 0, height=1, \
					 width = 15, variable = check_var)
				check_button.grid(row = cat_row, column = cat_col)
				check_dict[category] = check_var
				
				cat_row += 1
				if cat_row == 4:
					cat_col+= 1
					cat_row = 0
				if cat_col == 4:
					break
					
				check_dict[category] = check_var
			return check_dict
			
		#function to set up indiviual frame in scrolling section for each category
		def set_display_widgets():
			for thing in display_widgets:
				thing.grid_forget()

			grid_x = 0
			grid_y = 0
			for category in self.backend._category_list.keys():
				label1 = Label(frame, text = category, font=("Courier", 18, 'bold'))
				display_widgets.append(label1)
				label1.grid(row = grid_x, column = grid_y)
				temp_x = grid_x
				flag_full = 0
				for show in self.backend._category_list[category]._shows:
					grid_x += 1
					label2 = Label(frame, text = show._title + " episode " + str(show._episode_num))
					button1 = Button(frame, text = "Play", command=lambda show = show: play_show(show))
					button2 = Button(frame, text = "Back", command=lambda show = show: back_show(show))
					
					display_widgets.append(label2)
					display_widgets.append(button1)
					display_widgets.append(button2)
					
					label2.grid(row = grid_x, column = grid_y)
					button1.grid(row = grid_x, column = grid_y+1)
					button2.grid(row = grid_x, column = grid_y+2)
					
					if (grid_x > (temp_x + 7)) and (grid_y == 3):
						grid_x += 1
						grid_y = 0
						temp_x = grid_x
						flag_full = 0
					elif (grid_x > (temp_x + 7)):
						flag_full = 1
						grid_y += 3
						grid_x = temp_x
					
				
				if flag_full == 1:
					grid_x = temp_x + 9
				else: 
					grid_x += 1
				grid_y = 0

			
		#set up window 
		root = Tk()
		root.geometry("850x450")
		root.configure(background='white')
		root.title("Show Tracker")
		
		#create main frames
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
		
		self.check_dict = set_check_boxes()
		
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
		
		#Idea is to add frame with widgets and delete
		"""frame2 = Frame(frame, background = 'white', width = 600, height = 300)
		frame2.pack()
		frame2.tkraise(frame2)"""
		
		scrollbar = Scrollbar(scrolling_shows,orient ="vertical", command = canvas.yview)
		canvas.configure(yscrollcommand=scrollbar.set)
		canvas.pack(side="left")
		scrollbar.pack(side = "right", fill="y")
		
		"""for i in range(0,4):
			self.backend.add_show("Adventure Time", "https://www.watchcartoononline.io/adventure-time-season-1-episode-1-slumber-party-panic", ["gggggg"])"""

		self.backend.add_show("Adventure Time", "https://www.watchcartoononline.io/adventure-time-season-1-episode-1-slumber-party-panic", ["gggggg"])
		self.backend.add_show("Out There", "https://www.watchcartoononline.io/out-there-episode-2-quest-for-fantasy", ["gggggg"])
		self.backend.add_show("Exosquad", "https://www.watchcartoononline.io/exosquad-season-1-episode-12-betrayal", ["gggggg"])
		
		display_widgets = []
		set_display_widgets()
		
		#raise selected fram and 
		def raise_frame(frame):
			#delete entered data from prior screen
			category_entry.delete(0, END)
			HTTP_entry.delete(0, END)
			tag_entry.delete(0, END)
			self.check_dict = set_check_boxes()
			
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
			#create list categories from ticked boxes
			categories = []
			for category in self.check_dict.keys():
				if self.check_dict[category].get() == 1:
					categories.append(category)
			
			#add show to list of categories  ticked aswell as general
			self.backend.add_show(tag_entry.get(), HTTP_entry.get(), categories)
			set_display_widgets()
			exit()
			
		def add_category():
			shows = None
			self.backend.add_category(category_entry.get(), shows)
			set_check_boxes()
			set_display_widgets()
			exit()
			
		def play_show(show):
			webbrowser.open(show._curr_address, new = 2)
			self.backend.find_next(show)
			set_display_widgets()
		
		#def back_show(show):
			
			
	
		raise_frame(banner)
		raise_frame(scrolling_shows)
		canvas.create_window((0,0),window=frame,anchor='nw')
		frame.bind("<Configure>",myfunction)
		root.mainloop()
if __name__ == "__main__":

	guwee = GUI()