import pandas as pd
calories={"day1":420,"day2":380,"day3":390}
myvar=pd.Series(calories,index=["day1","day2"])
print(myvar)