import matplotlib.pyplot as plt
activity_data={"sleeping":8,"classes":6,"studying":3.5,"TV":2,"music":1,"other":3.5} #create a directory include the related values
plt.figure()
plt.pie(activity_data.values(), labels=activity_data.keys(), startangle=90
        )
plt.title("the average day of a university student")
plt.show()
plt.clf()       #make a chart

a=input("please write an activity     ") #input the activity 
print(activity_data[a])   #print the number of hours
