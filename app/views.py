from django.shortcuts import render
import pickle
from fuzzywuzzy import fuzz,process
# Create your views here.
def home(request):
    if request.method == "POST":
        book_input = request.POST["song_name"]
        reccomendations=[]
        searched1=[]
        with open("D:\\Django Projects\\application\\model.pkl", "rb") as model1:
            model = pickle.load(model1)
        with open("D:\\Django Projects\\application\\vectors.pkl", "rb") as vector1:
            vectors = pickle.load(vector1)
        with open("D:\\Django Projects\\application\\data.pkl", "rb") as data1:
            data = pickle.load(data1)
        titles = data["title"].tolist()
        best_match = process.extractOne(book_input, titles, scorer=fuzz.partial_ratio)
        if fuzz.ratio(best_match[0], book_input) > 30:
            index = titles.index(best_match[0])
            searched1.append([data["title"].iloc[index],data["author"].iloc[index], data["imgUrl"].iloc[index],data["productURL"].iloc[index],data["stars"].iloc[index]])
            print(searched1)

            distances, indices = model.kneighbors(vectors[index].reshape(1, -1))
            for i in indices.flatten():
                reccomendations.append([data["title"].iloc[i], data["author"].iloc[i], data["imgUrl"].iloc[i],data["productURL"].iloc[i],data["stars"].iloc[i]])
            return render(request,"home.html",{"reccomendations":reccomendations,"searched":searched1})
        else:
            msg = "Sorry!!! We Cannot Find the songs That are similar to the song.. Kindly check the spelling of the song You have entered or try another song"
            return render(request, "home.html", {"msg": msg})
    else:
        return render(request, "home.html")