from flask import Flask, request

store = [
    {
        "name" : "London",
        "age" : 23,
        "nationality": "Angola"
    }, 
    {
        "name": "Eunice",
        "age" : 21,
        "nationality": "Mozambique"
    }
]

app = Flask(__name__)


@app.post("/")
def setInfo():
    request_data = request.get_json()
    new_element = {"name" : request_data["name"], 
                   "age": request_data["age"], 
                   "nationality" : request_data["nationality"]}
    
    store.append(new_element)
    return new_element

@app.get("/get")
def getInfo():
    return { "store" : store }

if __name__ == "__main__":
    app.run(debug=True)