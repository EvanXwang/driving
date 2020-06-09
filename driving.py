country = input ('請問你是那國人？？') 
age = input ('請問你的年紀是？？')
age = int(age)

if country == "Taiwan":
	if age >= 18 :
		print ("你可以考駕照")
	else :
		print ("你還不能考駕照唷")

