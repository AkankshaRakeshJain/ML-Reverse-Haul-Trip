import pandas as pd
import warnings
warnings.filterwarnings('ignore')


def get_data(path):
    df1 = pd.read_excel(path)
    df2 = df1.copy()

    df1 = df1.rename(
        columns={
            'Trip Id': 'trip_id1',
            'Dispatch_Date': 'Dispatch_Date1',
            'Delivery_Date': 'Delivery_Date1',
            'Dispatch_cluster': 'Dispatch_cluster1',
            'Delivery_cluster': 'Delivery_cluster1',
            'Dispatch_cluster Latitude Longitude': 'Dispatch_lat_long1',
            'Delivery_cluster Latitude Longitude': 'center_station'
            }
        )

    df2 = df2.rename(
        columns={
            'Trip Id': 'trip_id2',
            'Dispatch_Date': 'Dispatch_Date2',
            'Delivery_Date': 'Delivery_Date2',
            'Dispatch_cluster': 'Dispatch_cluster2',
            'Delivery_cluster': 'Delivery_cluster2',
            'Dispatch_cluster Latitude Longitude': 'center_station',
            'Delivery_cluster Latitude Longitude': 'Dispatch_lat_long2'
            }
        )

    df = pd.merge(df1, df2, on=['center_station'])

    df_new = df[(df.Delivery_Date1 <= df.Dispatch_Date2) & (df.Dispatch_lat_long1 == df.Dispatch_lat_long2)]
    df_new['time_gap'] = df_new['Dispatch_Date2'] - df_new['Delivery_Date1']
    df_new = df_new.sort_values('time_gap')
    df_temp = df_new.copy()

    reverse_haul_trips = []

    while True:
        if len(df_temp) > 0:
            df_temp = df_temp.sort_values('time_gap')
            trip = (df_temp.iloc[0].trip_id1, df_temp.iloc[0].trip_id2)
            reverse_haul_trips.append(trip)
            df_temp = df_temp[
                (df_temp.trip_id1 != trip[0]) &
                (df_temp.trip_id2 != trip[0]) &
                (df_temp.trip_id1 != trip[1]) &
                (df_temp.trip_id2 != trip[1])
            ]
        else:
            break


    print('Length of Reverse Haul Trip: ',len(reverse_haul_trips))  
    df_map = pd.DataFrame(reverse_haul_trips,columns = ["trip_id1", "trip_id2"])
    df_new1 = df_new.reset_index()
    mergedStuff = pd.merge(df_new1, df_map, on=['trip_id1','trip_id2'], how='inner')
    return (mergedStuff)

path = 'Trip Data.xlsx'
print(get_data(path))
