import pandas as pd
import datetime, time
#
# activity = pd.read_csv('./datas/novin.csv', sep = ',')

def convertTime(t):
    x = time.strptime(t,'%H:%M')
    return str(int(datetime.timedelta(hours=x.tm_hour,minutes=x.tm_min,seconds=x.tm_sec).total_seconds()))

activity = pd.read_csv('./datas/novin.csv', sep=',',converters={'activity_end(s)': convertTime,
                                                                'activity_begin(s)': convertTime})

#activity = pd.read_csv('./datas/novin.csv', sep=',')

activity['activity_length(s)'] = activity['activity_end(s)'].subtract(activity['activity_begin(s)'])
activity['walk_duration(s)'] = activity['activity_length(s)'].subtract(activity['pause(s)'])
activity['tiredness(s)'] = activity['pause(s)'].divide(activity['walk_duration(s)'])
activity['speed(s)'] = activity['step_count'].divide(activity['walk_duration(s)'])

activity.to_csv('./datas/novins_final', index= False)

print(activity.head())