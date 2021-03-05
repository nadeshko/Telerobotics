import matplotlib.pylot as plt
import numpy as np
import pandas as pd

class plot():
 def __init__(self, mx, my):
 
  # x-axis values
  x = []

  # y-axis values
  y = []

  # the average values
  x1 = 
  y1 = 
  
  x2 = 
  y2 = 
  
  plot1 = plt.figure(1)
  # ploting the points
  plt.plot(x,y)
  # naming the x axis
  plt.xlabel(m_x)
  # naming the y axis
  plt.ylabel(m_y)
  # giving a title to my graph
  plt.title('All Recorded Data')
  
  plot2 = plt.figure(2)
  plt.plot(x1,y1)
  plt.xlabel(m_x)
  plt.ylabel(m_y)
  plt.title('Average Data')
  
  plot3 = plt.figure(3)
  plt.plot(x2,y2)
  plt.xlabel(m_x)
  plt.ylabel(m_y)
  plt.title('Calibrated Data')

  # function to show the plot
  plt.show()

