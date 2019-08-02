import matplotlib
import matplotlib.pyplot as mlt
channel=['youtube','facebook','linkedin','instagram','twitter']
views=[456,406,354,546,743]
explode=[0,0,0.3,0,0]
matplotlib.rcParams["font.family"]='fantasy'
mlt.pie(views,labels=channel, explode=explode,shadow=True,autopct='%1.1f%%',wedgeprops={'width':1})
mlt.show()
