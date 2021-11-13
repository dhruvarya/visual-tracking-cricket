import json

f = open("data1.json", "rb")

c = json.loads(f.read())

k = {}
k['nodedata'] = list()

for i in c['nodedata']:
	temp = {}
	temp['nodes'] = []
	z = int(0)
	for xx in i['nodes']:
		yy = {}
		yy['id'] = z
		yy['x'] = xx['x']
		yy['y'] = xx['y']
		temp['nodes'].append(yy)
		z += 1
	k['nodedata'].append(temp)

res = json.dumps(k)
f2 = open("data.json", "w")
f2.write(res)