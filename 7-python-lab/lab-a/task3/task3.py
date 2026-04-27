import matplotlib.pyplot as plt

labels = ['Film1', 'Film2', 'Film3']
sizes = [45, 40, 15]
explode1 = (0, 0., 0)
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode1, labels=labels, autopct='%1.1f%%', shadow=True, startangle=45)
ax1.axis('equal')
plt.show()