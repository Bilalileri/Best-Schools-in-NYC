import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 


schools = pd.read_csv("C:/Users/Bilal İLERİ/Desktop/Data Science/Repositories/NYC Public School/schools.csv")


math_above_schools = schools[schools["average_math"]>640]
best_math_schools = math_above_schools[["school_name","average_math"]].sort_values("average_math", ascending=False)
print(best_math_schools)

# best_math_schools.set_index("school_name").plot(kind="bar",title="Schools with the best math scores in NYC ",figsize=(10, 6),rot=70)



schools["total_SAT"] = schools["average_math"]+schools["average_reading"]+schools["average_writing"]

schools.sort_values("total_SAT" , ascending=False)





boroughs = schools.groupby("borough")["total_SAT"].agg(["count", "mean", "std"]).round(2).sort_values("mean",ascending=False)
print(boroughs)

boroughs["mean"].plot(kind='bar', title="NYC Boroughs by Average Total SAT Score" , rot= 20)
plt.show()




large_std_dev = boroughs[boroughs["std"] == boroughs["std"].max()]
large_std_dev = large_std_dev.rename(columns={"count":"num_schools","mean":"average_SAT", "std":"std_SAT"})
