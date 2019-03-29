import matplotlib.pyplot as plt
plt.style.use('ggplot')
customers = ['ABC','DEF','GHI','JKL','MNO']
customers_index = range(len(customers))
sale_amounts=[127,90,201,111,232]

fig = plt.figure()
axl=fig.add_subplot(1,1,1)
axl.bar(customers_index,sale_amounts,align='center', color='darkblue')

axl.xaxis.set_ticks_position('bottom')
axl.yaxis.set_ticks_position('left')

plt.xticks(customers_index,customers,color='red',fontsize='large')

plt.xlabel('Customer Name')
plt.ylabel('Sale Amount')
plt.title('Sale Amount per Customer')

plt.savefig('bar_plot_tight.png',dpi=400, bbox_inches='tight')
plt.show()
