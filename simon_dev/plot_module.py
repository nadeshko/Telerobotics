import matplotlib.pyplot as plt
import numpy as np

class plot():
    def __init__(self):
        pass

    def calibrate(self, mx, my, avg_mx, avg_my):
        rec_win = plt.figure(1)
        rec_win.winName('Recorded Data')
        # x-axis value
        plt.plot(mx,my,'o', color = 'blue')
        # naming the x axis
        plt.xlabel('mx')
        # naming the y axis
        plt.ylabel('my')
        # giving a title to my graph
        plt.title('All Recorded Data')
        # function to show the plot

        avg_win = plt.figure(2)
        avg_win.winName('Average Data')
        plt.plot(avg_mx, avg_my, 'o', color='blue')
        plt.xlabel('mx')
        plt.ylabel('my')
        plt.title('Averaged Data')

        # Printing values to normalize values for [-1, 1]
        print(f"min-mx:{min(avg_mx)}, max-mx:{max(avg_mx)}")
        print(f"min-my:{min(avg_my)}, max-my:{max(avg_my)}")

        normalized_mx = 2*((avg_mx - np.min(avg_mx)) / (np.max(avg_mx) - np.min(avg_mx))) - 1
        normalized_my = 2*((avg_my - np.min(avg_my)) / (np.max(avg_my) - np.min(avg_my))) - 1

        cal_win = plt.figure(3)
        cal_win.winName('Calibrated Data')
        plt.plot(normalized_mx, normalized_my, 'o', color='blue')
        plt.xlabel('mx')
        plt.ylabel('my')
        plt.title('Calibrated Data')

        plt.show()