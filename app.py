import pickle
from fuzzywuzzy import fuzz,process
with open("model.pkl","rb") as model_file:
  model=pickle.load(model_file)
with open("vectors.pkl","rb") as vector_file: 
  vectors=pickle.load(vector_file)  
with open("data.pkl","rb") as data_file:
  data=pickle.load(data_file)
inpu1="Little women"
titles=data["title"].tolist()
best_match = process.extractOne(inpu1, titles, scorer=fuzz.partial_ratio)
index=titles.index(best_match[0])
distances, indices = model.kneighbors(vectors[index].reshape(1, -1))
for i in indices.flatten():
  print(titles[i])
