import matplotlib.pyplot as plt
activity_data={"Sleeping":8,"Classes":6,"Studying":3.5,"TV":2,"Music":1,"Other":3.5}
plt.figure()
plt.pie(activity_data.values(), labels=activity_data.keys(), startangle=90
        )
plt.title("the average day of a university student")
plt.show()
plt.clf()
