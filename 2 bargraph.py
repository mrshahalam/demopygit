import  matplotlib.pyplot as plt
import  numpy as np
y_view = [545,678,532,798,643,697,724,564,857,709,619,766,567]
f_view = [545,678,532,798,643,487,834,364,657,789,619,766,567]
x = range(1,14)
plt.bar([a-0.25 for  a in x], y_view,width=0.25, label = 'Youtube Views', align='edge')
plt.bar([a+0.25 for  a in x], y_view,width=-0.25, label = 'Youtube Views',align='edge')
plt.xlabel('day')
plt.ylabel('Views')
plt.legend(loc='upper right')
plt.grid(True,linewidth=1,linestyle='-.')
plt.xticks(x)
plt.title('Daily views for marketing channels')
plt.show()
