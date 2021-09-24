pun = 'Eating a clock is very time consuming!!!'
pun[23:] # 'time consuming!!!'
pun = pun.rstrip('!') # 'Eating a clock is very time consuming'
pun.count('!') # 0
punWords = pun.lower().split()
punWords # ['eating', 'a', 'clock', 'is', 'very', 'time', 'consuming']


scores = {'Mary': [22, 23, 36], 'Fred': [20, 21, 29]}
scores['Mary'] # [22, 23, 36]
scores['Fred'][1] # 21
scoreKeys = scores.keys()
scoreKeys # dict_keys(['Mary', 'Fred'])
scores['Jane'] = [21, 24, 30]
scores['Fred'][2] = 39
scores # {'Mary': [22, 23, 36], 'Fred': [20, 21, 39], 'Jane': [21, 24, 30]}
