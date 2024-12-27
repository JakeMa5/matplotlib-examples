from plotter import Plotter

import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("MatPlotLib Test")
        self.geometry("1200x1000")

        self._button_panel = tk.Frame(self, padx=4, pady=4)
        self._button_panel.pack(side=tk.BOTTOM, fill=tk.X)

        self._label_data1 = tk.Label(self._button_panel, text="Input Dataset 1:", padx=4)
        self._entry_data1 = tk.Entry(self._button_panel)

        self._label_data2 = tk.Label(self._button_panel, text="Input Dataset 2:", padx=4)
        self._entry_data2 = tk.Entry(self._button_panel)

        self._btn_chart = tk.Button(self._button_panel, text="Generate Chart", command=self.create_plotter, padx=4)
        self._btn_quit = tk.Button(self._button_panel, text="Quit", command=self.quit, padx=4)

        self._label_data1.pack(side=tk.LEFT)
        self._entry_data1.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self._label_data2.pack(side=tk.LEFT)
        self._entry_data2.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self._btn_chart.pack(side=tk.LEFT)
        self._btn_quit.pack(side=tk.RIGHT)

        self.plotter = None

        tk.Message(self, text="Enter comma-separated lists of numbers for Dataset 1 and Dataset 2, then click 'Generate Chart'.", width=1000).pack()

        # create a 'dummy' plotter to display when the app is first opened.
        self.plotter = Plotter(data1=[0], data2=[0], master=self)
        self.plotter.plot()

    def create_plotter(self) -> None:
        if self.plotter is not None:
            self.plotter.dispose()
            self.plotter = None

        data1_str = self._entry_data1.get()
        data2_str = self._entry_data2.get()
        try:
            data1 = [float(i) for i in data1_str.split(',')]
            data2 = [float(i) for i in data2_str.split(',')]
        except ValueError:
            tk.messagebox.showerror("Invalid input", "Please enter valid comma-separated lists of numbers.")

            # create an empty plotter if the input is invalid.
            self.plotter = Plotter(data1=[0], data2=[0], master=self)
            self.plotter.plot()

            return

        self.plotter = Plotter(data1=data1, data2=data2, master=self)
        self.plotter.plot()