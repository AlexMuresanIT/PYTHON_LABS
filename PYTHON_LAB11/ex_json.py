import json

#din json in python
x='{"name":"John","age":30,"city":"New York"}'
y=json.loads(x)
for i in y:
    print(i,":",y[i])

#din python in json
x={"name":"Alex",
   "age":22,
   "city":"Medias"}

y=json.dumps(x)
print(y)

print(json.dumps(["Pozitie","Meteo"]))
print(json.dumps(("Pozitie","Meteo")))