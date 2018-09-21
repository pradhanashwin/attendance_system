csv_file = FILES['Falgun.csv']
file_data = csv_file.read().decode("utf-8")
lines = file_data.split("\n")
for line in lines:
	fields = line.split(",")
	print(line)
       
