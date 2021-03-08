
import matplotlib.pyplot as plt
import numpy as np

class plot():
 def __init__(self, mx, my, avg_mx, avg_my):

  plot1 = plt.figure(1)
  # x-axis value
  plt.plot(mx,my,'o', color = 'blue')
  # naming the x axis
  plt.xlabel('mx')
  # naming the y axis
  plt.ylabel('my')
  # giving a title to my graph
  plt.title('All Recorded Data')
  # function to show the plot

  plot2 = plt.figure(2)
  plt.plot(avg_mx, avg_my, 'o', color='blue')
  plt.xlabel('mx')
  plt.ylabel('my')
  plt.title('Averaged Data')

  normalized_mx = (avg_mx - np.min(avg_mx))/(np.max(avg_mx)-np.min(avg_mx))
  normalized_my = (avg_my - np.min(avg_my)) / (np.max(avg_my) - np.min(avg_my))
  '''
  normalized_mx = preprocessing.normalize(avg_mx)
  normalized_my = preprocessing.normalize(avg_my)'''
  plot3 = plt.figure(3)
  plt.plot(normalized_mx, normalized_my, 'o', color='blue')
  plt.xlabel('mx')
  plt.ylabel('my')
  plt.title('Calibrated Data')

  plt.show()



