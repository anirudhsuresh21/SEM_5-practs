from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random

data = pd.read_csv('C:\\Users\\aniru\\Desktop\\Practical\\AI\\ld.csv')

features = data.columns[0:8]
features = list(features)
print(features)
data['Alternate'], _ = pd.factorize(data['Alternate'])
data['Bench'], _ = pd.factorize(data['Bench'])
data['Hungry'], _ = pd.factorize(data['Hungry'])
data['Waiting'], _ = pd.factorize(data['Waiting'])
data['Patrons'], _ = pd.factorize(data['Patrons'])
data['Costly'], _ = pd.factorize(data['Costly'])
data['Rain'], _ = pd.factorize(data['Rain'])
data['Decision'], _ = pd.factorize(data['Decision'])
data['Reservation'], _ = pd.factorize(data['Reservation'])
x = data[features]
y = data['Decision']


tree_clf = DecisionTreeClassifier(max_depth=None, random_state=42)

tree_clf.fit(x, y)
alternate = int(input("Alternate: (1 = Yes, 0 = No): "))
bar = int(input("Bench: (1 = Yes, 0 = No): "))
hungry = int(input("Hungry: (1 = Yes, 0 = No): "))
waiting = int(input("Is There Waiting: (1 = Yes, 0 = No): "))
costly = int(input("Is It Costly: (1 = Yes, 0 = No): "))
rain = int(input("Is It Raining: (1 = Yes, 0 = No): "))
reservation = int(input("Do you have a Reservation: (1 = Yes, 0 = No): "))
patrons = int(input("How many Patrons: "))

prediction = tree_clf.predict([[alternate, bar, hungry, waiting, patrons, costly, rain, reservation]])

print("Prediction: ", 'Go' if prediction[0] ==1 else 'No Go')


export_graphviz(tree_clf, out_file=None,
                feature_names=features, class_names=["Don't Go", 'Go'],
                filled=True, rounded=True, special_characters=True)


graph = export_graphviz(tree_clf, out_file='tree.dot',
                        feature_names=features, class_names=['Don’t Go', 'Go'],
                        filled=True, rounded=True, special_characters=True)


# Convert to PNG
from subprocess import call
call(['dot', '-Tpng', 'tree.dot', '-o', 'C:\\Users\\aniru\\Desktop\\Practical\\AI\\output-tree.png'])


# Display the image
img = Image.open('C:\\Users\\aniru\\Desktop\\Practical\\AI\\output-tree.png')
img.show()