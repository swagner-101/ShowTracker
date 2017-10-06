from back_end import BackEnd
from tkinter import *
from PIL import ImageTk
import webbrowser

class GUI:

	
	def	__init__(self):
		self.backend = BackEnd()
		self.new_scan_speed = 750 #Milliseconds
		self.current_uptodate = 0
		
		#Reconfigures canvas on expansion
		def myfunction(event):
			canvas.configure(scrollregion=canvas.bbox("all"),width=830,height=415)
			
		#limit character to length N function
		def limit_entry_size(limited_text, N):
			if len(limited_text.get()) > N:
				limited_text.set(limited_text.get()[:N])
		
		#establish check boxes in addshow frame, changes upon add and delete of category
		def set_check_boxes():
			#Set up check boxes in add show fram
			check_boxes = Frame(add_frame,  width = 400, height = 100, background= 'white')
			check_boxes.place(x = 20, y = 180)
		
			cat_row =0
			cat_col =0
			check_dict = dict()
			for category in self.backend._category_list.keys():
				if category != "General" and category != "New":
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
					check_dict[category] = check_var
					if cat_col == 4:
						break
					
			return check_dict
			
		#function to set up indiviual frame in scrolling section for each category
		def set_display_widgets(method):
			for thing in display_widgets:
				thing.grid_forget()

			grid_x = 0
			grid_y = 0
			#for each category place a label and sequence of shows and buttons
			for category in self.backend._category_list.keys():
				label1 = Label(frame, text = category, font=("Courier", 18, 'bold'))
				display_widgets.append(label1)
				label1.grid(row = grid_x, column = grid_y)
				
				#add button to delete a category
				if method == "Delete" and category != "New" and category != "General":
					button2 = Button(frame, text = "Delete", command=lambda category = category: delete_item("Category", category, None))
					display_widgets.append(button2)
					button2.grid(row = grid_x, column = grid_y+1)
					
				#if no new shows have been added inform user with label
				if category == "New" and not self.backend._category_list[category]._shows:
					grid_x += 1
					label2 = Label(frame, text = "///No newly released episodes to watch///")
					display_widgets.append(label2)
					label2.grid(row = grid_x, column = grid_y)
					
		
				temp_x = grid_x
				flag_full = 0
				for show in self.backend._category_list[category]._shows:
					grid_x += 1
					label2 = Label(frame, text = show._title + " season " + str(show._season_num)\
					+ " episode " + str(show._episode_num))
					
					#place either play and back, delete buttons, or check button depending on method
					if method == "Play":
						button1 = Button(frame, text = "Play", command=lambda show = show: play_show(show))
						button2 = Button(frame, text = "Back", command=lambda show = show: back_show(show))
						display_widgets.append(button1)
						display_widgets.append(button2)
						button1.grid(row = grid_x, column = grid_y+1)
						button2.grid(row = grid_x, column = grid_y+2)
					elif method == "Delete":
						button1 = Button(frame, text = "Delete", command=lambda show = show, category = category: delete_item ("Show", show, category))
						display_widgets.append(button1)
						button1.grid(row = grid_x, column = grid_y+1)
					elif method == "AddCat" and category == "General":
						check_var = IntVar()
						check_button = Checkbutton(frame, \
						onvalue = 1, offvalue = 0, height=1, \
						width = 15, variable = check_var)
						display_widgets.append(check_button)
						check_button.grid(row = grid_x, column = grid_y+1)
						self.add_cat_dict[show] = check_var
						
						
					display_widgets.append(label2)
					label2.grid(row = grid_x, column = grid_y)
					
					#place below unless category is seven deep and then place to right
					#after 2 columns repeat on next level
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
		show_not_found_frame = Frame(root,  width = 600, height = 300, highlightbackground="black",\
		highlightcolor="black", highlightthickness=5, background= 'white')
		
		#place main frames
		banner.grid(row=0, column=0, sticky='news')
		scrolling_shows.place(x = 0, y= 30)
		settings_frame.place(x = 300, y = 40)
		add_frame.place(x = 110, y = 40)
		category_frame.place(x = 110, y = 30)
		show_not_found_frame.place(x = 110, y = 40)
		
		
		#create banner buttons
		settings_button = Button(banner, highlightbackground='#260712',command=lambda: settings())
		settings_button.place(x=800, y=0)
		settings_image = ImageTk.PhotoImage(file = "settings.png")
		settings_button.config(image = settings_image)
		
		garbage_button = Button(banner, highlightbackground='#260712',command=lambda: garbage_item())
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
		tag_label = Label(add_frame, text = "Title")
		tag_label.place(x = 20, y = 10)
		tag_label.config(font=("Courier", 21, 'bold'))
		
		tag = StringVar()
		tag_entry = Entry(add_frame,highlightbackground='black',width = 50, textvariable=tag)
		tag_entry.place(x=20, y=40)
		tag.trace('w', lambda *args: limit_entry_size(tag, 15))
		
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
		
		#categories show will entire and there respective checkboxes
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
		
		#shows that will be added and there checked boxes
		self.add_cat_dict = dict()
		
		#widgets inside show not found frame
		exit_not_found_button = Button(show_not_found_frame, highlightbackground='#260712',command=lambda: exit())
		exit_not_found_button.place(x=555, y=0)
		exit_not_found_button.config(image = exit_image)
		
		not_found_label = Label(show_not_found_frame,\
		text = "the next episode could not be located.\n"\
		+ "If you have just caught up with the show select up to date\n"\
		+ "and new episodes will show up in the new category.\n"\
		+ "If you're finished watching this show select delete.\n"
		+ "If there is more to watch it is possible you \n"
		+ "will have to enter the address of the next season.\n"
		+ "Remember to only include adresses of the\n"
		+ "format www.example.com/anything (Season X)? Episode Y anything")
		
		not_found_label.place(x = 20, y = 50)
		not_found_label.config(font=("Courier", 14, 'bold'))
				
		#set up scrolling show viewing area
		canvas = Canvas(scrolling_shows, background= 'white')
		frame = Frame(canvas, background = 'white')
		
		scrollbar = Scrollbar(scrolling_shows,orient ="vertical", command = canvas.yview)
		canvas.configure(yscrollcommand=scrollbar.set)
		canvas.pack(side="left")
		scrollbar.pack(side = "right", fill="y")
		
		self.backend.add_show("Adventure Time", "https://www.watchcartoononline.io/adventure-time-season-1-episode-1-slumber-party-panic", ["gggggg"])
		self.backend.add_show("Out There", "https://www.watchcartoononline.io/out-there-episode-2-quest-for-fantasy", ["gggggg"])
		self.backend.add_show("Exosquad", "https://www.watchcartoononline.io/exosquad-season-1-episode-12-betrayal", ["gggggg"])
		self.backend.add_show("Game of Thrones", "http://www4.fmovies.io/watch/game-of-thrones-season-3-episode-06-the-climb.html", ["gggggg"])
		self.backend.add_show("Rick and Morty", "https://www.watchcartoononline.io/rick-and-morty-season-3-episode-7-the-ricklantis-mixup", ["gggggg"])
		display_widgets = []
		set_display_widgets("Play")
		
		for show in self.backend._category_list["General"]._shows:
			self.backend._up_to_date.append(show)
		
		
		#raise frame
		def raise_frame(frame):
			#delete entered data from prior screen
			category_entry.delete(0, END)
			HTTP_entry.delete(0, END)
			tag_entry.delete(0, END)
			self.check_dict = set_check_boxes()
			
			frame.tkraise()
		
		#functions linked to buttons to raise specific frames 
		def settings():
			raise_frame(scrolling_shows)
			raise_frame(settings_frame)
		def add():
			raise_frame(scrolling_shows)
			raise_frame(add_frame)
		def category():
			raise_frame(scrolling_shows)
			raise_frame(category_frame)
			set_display_widgets("AddCat")
		def exit():
			raise_frame(scrolling_shows)
		
		#adds show to backend under correct categories
		def add_show():
			#create list categories from ticked boxes
			categories = []
			for category in self.check_dict.keys():
				if self.check_dict[category].get() == 1:
					categories.append(category)
			
			#add show to list of categories  ticked aswell as general
			self.backend.add_show(tag_entry.get(), HTTP_entry.get(), categories)
			set_display_widgets("Play")
			exit()
		
		#adds category to backend with correct shows
		def add_category():
			#create list from checked boxes and add to new category
			shows = []
			for show in self.add_cat_dict.keys():
				if self.add_cat_dict[show].get() == 1:
					shows.append(show)
					
			self.backend.add_category(category_entry.get(), shows)
			set_check_boxes()
			set_display_widgets("Play")
			exit()
		
		#adds show to list of up to date shows
		def up_to_date(show):
			self.backend._up_to_date.append(show)
			exit()
	
		#plays shows and finds next episode
		def play_show(show):
			webbrowser.open(show._curr_address, new = 2)
			found = self.backend.find_next(show)
			
			if not found and show in self.backend._category_list["New"]._shows:
				self.backend._up_to_date.append(show)
				delete_item("Show", show, "New")
			#if next episode is not found give options
			elif not found:
				raise_frame(scrolling_shows)
				uptodate_button = Button(show_not_found_frame, text = "Up To Date", command=lambda show = show: up_to_date(show))
				uptodate_button.place(x = 200, y = 180)
				not_found_delete_button = Button(show_not_found_frame, text = "Delete", command=lambda show = show: delete_item("Show", show, "General"))
				not_found_delete_button.place(x = 300, y = 180)
				raise_frame(show_not_found_frame)
				
			set_display_widgets("Play")
		
		#send show back and episode
		def back_show(show):
			self.backend.revert_show(show)
			set_display_widgets("Play")
			
		#initialize show display with option to delete not play
		def garbage_item():
			set_display_widgets("Delete")
		
		#based on method input get rid of show or category
		def delete_item(method, item, show_container):
			if method =="Category":
				self.backend.delete_category(item)
			elif method == "Show":
				self.backend.delete_show(item, show_container)
			set_display_widgets("Play")
			exit()
			
		def check_for_new():
			tot_index = len(self.backend._up_to_date) - 1
			print(tot_index)
			if self.current_uptodate <= tot_index:
				print("Short wait")
				show = self.backend._up_to_date[self.current_uptodate]
				found_new = self.backend.find_next(show)
				if found_new:
					self.backend._category_list["New"].to_category_add(show)
					self.backend._up_to_date.remove(show)
					set_display_widgets("Play")
				else:
					self.current_uptodate += 1
				root.after(self.new_scan_speed, check_for_new)
			else:
				print("Long wait")
				self.current_uptodate = 0
				root.after(240000, check_for_new)
	
		raise_frame(banner)
		raise_frame(scrolling_shows)
		canvas.create_window((0,0),window=frame,anchor='nw')
		frame.bind("<Configure>",myfunction)
		root.after(self.new_scan_speed, check_for_new)
		root.mainloop()
if __name__ == "__main__":

	guwee = GUI()