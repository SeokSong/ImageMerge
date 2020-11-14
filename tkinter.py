from Tkinter import * 
from PIL import Image

def box():
    #print("Select the RBG values of your image ")
    #R = input("Select a value for Red ")
    #G = input("Select a value for Green ")
    #B = input("Select a value for Blue ")
    img = Image.new('RGB', (600, 300), color = (29, 100, 200))
    img.save('image.ppm')
    image = "image.ppm" #these two must stay the same
    app = Tk()
    canvas = Canvas(app, width = 300, height = 300)
    canvas.pack()
    img = PhotoImage(file = image)
    canvas.create_image(20,20, anchor=NW, image=img)
    app.mainloop()
    
def main():
    box()



if __name__ == "__main__":
    main()
