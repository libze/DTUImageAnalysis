import matplotlib.pyplot as plt
import os

print(os.listdir('exercises/Ex7-GeometricTransformationsAndRegistration/data'))

img = plt.imread('exercises/Ex7-GeometricTransformationsAndRegistration/data/Hand2.jpg')
plt.imshow(img)
plt.show()