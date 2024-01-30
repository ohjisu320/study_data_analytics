import pandas as pd
import SpineSurgeryList_apply as csv

df_SSL = pd.read_csv('./docs/quests/CSVs/SpineSurgeryList.csv')

def cal_bmi(params):
  result =params['체중']/(params['신장']*0.1)**2
  return round(result*100, 1)

df_SSL['bmi(%)']=df_SSL[["신장", "체중"]].apply(cal_bmi,  axis=1)
pass

print(df_SSL[['체중', '신장', 'bmi(%)']])

def surgery_hours(params):
    try : 
        hour =int(params//60)
        minute =int(params%60)
        result = pd.to_datetime(f"{hour},{minute}", format="%H,%M")
        return result
    except :
        pass

df_SSL['수술시간_datetime_hours']=df_SSL['수술시간'].apply(surgery_hours)
df_SSL['수술시간_datetime_hours']=df_SSL['수술시간_datetime_hours'].dt.time
pass
