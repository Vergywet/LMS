import pandas as pd
data = pd.read_csv("C:\\Users\\User\Downloads\\motor_insure.csv\\motor_data11-14lats.csv")
filter = data[data["SEATS_NUM"]>40],[['make'],['usage']]
print(filter)
