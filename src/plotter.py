from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk)

class Plotter:
    """
    Contains the Plotter class which is used to plot data using Matplotlib
    and embed the plot in a Tkinter window.
    """

    def __init__(self, data1, data2, master):
        self.data1 = data1
        self.data2 = data2
        self.master = master

        self._canvas: FigureCanvasTkAgg = None
        self._toolbar: NavigationToolbar2Tk = None

    def plot(self):
        """
        Plots the data using Matplotlib and embeds the plot in the Tkinter window.
        """
  
        fig = Figure(figsize = (5, 5), dpi = 100) 
    
        plot1 = fig.add_subplot(111) 
    
        plot1.plot(self.data1, label='Dataset 1') 
        plot1.plot(self.data2, label='Dataset 2') 

        plot1.legend()
    
        self._canvas = FigureCanvasTkAgg(fig, master=self.master)
          
        self._canvas.draw() 
    
        self._canvas.get_tk_widget().pack(side="top", fill="both", expand=True) 
    
        self._toolbar = NavigationToolbar2Tk(self._canvas, self.master) 
        self._toolbar.update() 
    
        self._canvas.get_tk_widget().pack() 

    def dispose(self) -> None:
        """
        Destroys the plot chart and its UI components.
        """
        if self._canvas is not None:
            self._canvas.get_tk_widget().destroy()
            self._canvas = None
        if self._toolbar is not None:
            self._toolbar.destroy()
            self._toolbar = None
