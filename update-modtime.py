import os 

arr = os.listdir()
path=os.getcwd()



def read_dir(path):
	arr = os.listdir(path)
	times = [0]
	for i in arr:
		if os.path.isdir(i):
			newPath= path + "/" + i
			time = read_dir(newPath)
			os.utime(newPath, (time,time))
			times.append(time)
			
		else:
			time = os.path.getmtime(path+"/"+i)
			times.append(time)
	return max(times)
	

read_dir(path)

