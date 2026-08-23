from plotter import *
import numpy as np
import serial
import keyboard


app = QtWidgets.QApplication(sys.argv)
app.setStyle('Fusion')

pg.setConfigOptions(antialias=True, useOpenGL=True)

plotter = LivePlotter(
    max_points=1000,
    port=None,  # No auto-connect
    baudrate=115200
)

# Run ------------------------------------------
plotter.show()
sys.exit(app.exec_())

m = plotter.motor

def read_error_comp():
    for i in range(1, 1024):
        error_comp = m.get_abs_encoder_error_comp(i)['error_comp']
        print(f'{i} {error_comp}')

