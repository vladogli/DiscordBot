def getCommand(command):
	command = command[1:]
	returnValue = ['',[]]
	for i in range(len(command)):
		if command[i] == " ":
			for j in range(i, len(command)):
				if command[j] != " ":
					returnValue[0] = command[:i]
					command = command[j:]
					break;
			break;
	buf = ""
	x = False
	for i in range(len(command)):
		if(command[i]==" "):
			x = True
		elif x and command[i] != " ":
			returnValue[1].append(buf)
			buf = command[i]
			x = False
		else:
			buf += command[i]
	if(len(buf)!=0):
		returnValue[1].append(buf)
	return returnValue
