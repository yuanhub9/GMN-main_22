# author: wang Zhiyaun:2022/10/15
import pickle
F = open("aspirin_split.pkl", 'rb')
content = pickle.load(F)
print(content)
content.close()
