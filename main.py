from tkinter import *
screen=Tk();

def obter():
	lbl["text"]=txt.get();
	

def label(text, up_down, left_right):	
	Label(

			screen,
			text=f"({text}) in tkinter",
			font=("Helvetica", 16)
		
			).place(

			x=up_down,
			y=left_right
		
			);
				
				
txt=Entry(

		screen,
		bd=10
		
		);
		
		
txt.place(

		x=110,
		y=200
		
		);


lbl=Label(
	
				  screen,
				  text=""
			
				  );
				  
				  
lbl.place(
			
			  	x=0,
			  	y=0
			
			  	);
			  	

def button(up_down,  left_right):
		Button(

				screen,
				text="submit",
				fg='blue',
				command=obter
		
				).place(

				x=up_down,
				y=left_right
		
				);

label("hello, world", up_down=58,  left_right=50);
button(up_down=470,  left_right=199);

screen.mainloop();
