import matplotlib.pyplot as plt

frequency=[4,12,16,8]
bin_edges=[135,140,145,150,155]
plt.hist(bin_edges[:-1],bins=bin_edges,weights=frequency,edgecolor='purple',color='pink',alpha=1)
plt.xlabel('Height')
plt.ylabel('Frequency')
plt.title('histogram of students heights')
plt.show()