import gpxpy
import gpxpy.gpx 
import pandas as pd
from distance import dist

#this will read and parse the input gpx file
#will then find the grade between each data point and then
#put this into a dataframe
#said dataframe is returned by this function
def read_gpx (filename):
    assert filename.endswith('.gpx')
    gpx_file = open("gpx/" + filename, 'r')

    gpx = gpxpy.parse(gpx_file)

    prevPoint = 0
    totalDistance = 0
    
    data = []
    
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                if (prevPoint != 0):
                    elevationChange = point.elevation-prevPoint.elevation
                    distanceChange = dist(prevPoint.latitude, prevPoint.longitude, point.latitude, point.longitude)
                    totalDistance += distanceChange
                    grade = (elevationChange/distanceChange)*100      
                    data.append([distanceChange, grade])
                prevPoint = point
    df = pd.DataFrame(data, columns=['distanceChange', 'grade'])
    return df