import numpy as np
study_duration1=np.array([4,5,2,3,5,4,6])
study_duration2=np.array([1,2,5,3,2,2,1])
total_duration1=study_duration1+study_duration2
print("total study duration using + operator",total_duration1)
total_duration2=np.add(study_duration1,study_duration2)
print("total study duration using add() function",total_duration2)
