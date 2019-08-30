from iptcinfo3 import IPTCInfo


info = IPTCInfo('man.jpg')


print(info['keywords'])



newKeywords = {'key2', 'key2', 'key3'}

for key in newKeywords:
	info['keywords'].append(key)


info.save()
print(info['keywords'])