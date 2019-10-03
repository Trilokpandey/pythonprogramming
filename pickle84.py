import pickle

#pickling a python obj
#cars=["suzuki","audi","ferrari","hundai","inova"]
#file="mycar.pkl"
#fileobj=open(file,"wb")
#pickle.dump(cars,fileobj)
#fileobj.close()

file="mycar.pkl"
fileobj=open(file,"rb")
mycar=pickle.load(fileobj)
print(mycar)
print(type(mycar))