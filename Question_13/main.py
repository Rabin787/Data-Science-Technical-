from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
 
# Train the model 
iris = load_iris()
model = RandomForestClassifier()
model.fit(iris.data, iris.target)
 
SPECIES = ["setosa", "versicolor", "virginica"]
 
#  Create the app 
app = FastAPI()
 
# Define what the user sends 
class FlowerInput(BaseModel):
    sepal_length: float 
    sepal_width: float   
    petal_length: float  
    petal_width: float   
 
# Create the routes 
 
@app.get("/")
def home():
    return {"message": "Iris API is running!"}
 
@app.post("/predict")
def predict(flower: FlowerInput):
    # Put the values into a list the model understands
    data = [[
        flower.sepal_length,
        flower.sepal_width,
        flower.petal_length,
        flower.petal_width
    ]]
 
    prediction = model.predict(data)[0]          
    species = SPECIES[prediction]                  
    return {
        "species": species,
        "message": f"This flower is most likely a {species}!"
    }