import json

data='{"var1":"sonu","var2":"monu"}'
print(data) #cant access data by variable

parsed=json.loads(data)
print(parsed)
print(parsed["var1"])
print(type(parsed))

#task1 -json.load()?
#task2 -what is sort_key parameter in dump

data2={
    "channel":"ztv",
    "names":["var12","sonu","var2","monu"],
    "fridge":('roti','dal'),
    "isbad":False
}

jscomp=json.dumps(data2)
print(jscomp)
