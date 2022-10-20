from scipy.stats import skewnorm
import matplotlib.pyplot as plt

numValues = 3
maxValue = 5
skewness = 1  #Negative values are left skewed, positive values are right skewed.

random = skewnorm.rvs(a = skewness, loc=195, scale = 2, size = 1000)  #Skewnorm function

#random = random - min(random)      #Shift the set so the minimum value is equal to zero.
#random = random / max(random)      #Standadize all the vlues between 0 and 1. 
#random = random * maxValue         #Multiply the standardized values by the maximum value.

#Plot histogram to check skewness
#plt.hist(random,30,density=True, color = 'red', alpha=0.1)
plt.hist(random,30)
more_count=0
less_count=0
for i in range(len(random)):
    if i < 195:
        less_count+=1
    elif i>195:
        more_count+=1
print('more count'+str(more_count))
print('less_count'+str(less_count))
plt.show()

#print(random)