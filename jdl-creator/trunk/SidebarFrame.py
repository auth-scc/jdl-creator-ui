__author__ = 'Steve'

from Tkinter import *
from bcolours import *


class SidebarFrame(Frame):
    """ sidebar frame containing basic functionality of the application"""
    def __init__(self, master=None, myGuiHandler=None):
        Frame.__init__(self, master)
        print "Master state: "+master.state()
        self.myGuiHandler = myGuiHandler # has to know the gui handler object to call methods
        self.buttonTags = ["New File", "Help", "About"]
        self.buttons = []
        for i in xrange(0,3):
            self.buttons.append(Button(master=self))
        # self.dictButtons = {"New File":Button(master=self), "Help":Button(master=self), "About":Button(master=self)}
        self.populateFrame()
        self.bindButtonCommands()



    def populateFrame(self):
        """ inserts the containing elements inside the frame
        """
        i=0
        # you may need to change that for the correct order of buttons
        for button in self.buttons:
            button.config(text=self.buttonTags[i], width=8)
            i=i+1
            button.grid(row=i+1, column=0, pady=10, padx=3)

        self.titleLabel = Label(master=self, text="My Actions", justify=CENTER, font=('Arial', 32), pady=10,
                                padx=3)
        self.titleLabel.grid(row=0, column=0)


    # commands when buttons are pressed
    def newFile(self):
        """ run when "New File" button is pressed
        """
        try:
            # code here
            # here you should reset all the checkboxes
            raise NotImplementedError
        except AttributeError as ae:
            print bcolors.FAIL + "ERROR:"
            print "\nmyGuiHandler is None\n\t%s"%ae

    def showHelp(self):
        """ run when "Show Examples" button is pressed
        """
        # try:
            # code here
        self.myGuiHandler.showHelpWindow()
        # except AttributeError as ae:
        #     print bcolors.FAIL + "ERROR:"
        #     print "\nmyGuiHandler is None\n\t%s"%ae

    def showAbout(self):
        """ run when the "About" button is pressed
        """
        try:
            self.myGuiHandler.showAboutWindow()
        except AttributeError as ae:
            print bcolors.FAIL + "ERROR:"
            print "\nmyGuiHandler is None\n\t%s"%ae

    def bindButtonCommands(self):
        """ binds the buttons' functionality with the respective callabacks
        """
        # dictCommands = {}
        for button in self.buttons:
            if button.config('text')[-1] == "New File":
                button.config(command=self.newFile)
            elif button.config('text')[-1] == "Help":
                button.config(command=self.showHelp)
            elif button.config('text')[-1] == "About":
                button.config(command=self.showAbout)


if __name__=="__main__":
    root = Toplevel()
    mySidebarFrame = SidebarFrame(root)
    mySidebarFrame.pack(side=LEFT, expand=YES, fill=Y)

    root.mainloop()
