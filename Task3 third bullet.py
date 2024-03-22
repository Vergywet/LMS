
import pandas as pd
dataFrame =pd.read_csv("C:\\Users\\User\\Downloads\\motor_insure.csv\\motor_data11-14lats.csv")
filter=dataFrame[dataFrame["SEATS_NUM"]>40]
print(filter)