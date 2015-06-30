from pandas import *
from ggplot import *

def plot_weather_data(turnstile_weather):
    '''
    You are passed in a dataframe called turnstile_weather. 
    Use turnstile_weather along with ggplot to make a data visualization
    focused on the MTA and weather data we used in assignment #3.  
    You should feel free to implement something that we discussed in class 
    (e.g., scatterplots, line plots, or histograms) or attempt to implement
    something more advanced if you'd like.  

    Here are some suggestions for things to investigate and illustrate:
     * Ridership by time of day or day of week
     * How ridership varies based on Subway station
     * Which stations have more exits or entries at different times of day
       (You can use UNIT as a proxy for subway station.)

    If you'd like to learn more about ggplot and its capabilities, take
    a look at the documentation at:
    https://pypi.python.org/pypi/ggplot/
     
    You can check out:
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv
     
    To see all the columns and data points included in the turnstile_weather 
    dataframe. 
     
    However, due to the limitation of our Amazon EC2 server, we are giving you a random
    subset, about 1/3 of the actual data in the turnstile_weather dataframe.
    '''
    Date = turnstile_weather['DATEn'].apply(pandas.to_datetime)
    Date = Date.map(lambda x:x.strftime('%w'))
    #for x in range(len(Date)):
    #    Date[x] = datetime.datetime.strptime(Date[x], "%Y-%m-%d").strftime("%A")
    
    df = turnstile_weather.join(pandas.DataFrame({'Day of week': Date}))
              
    #plot = ggplot(df, aes('Day of week', 'ENTRIESn_hourly' )) + geom_histogram() + scale_x_discrete('Days of Week - Sunday till Saturday') + ggtitle('Ridership by day of week starting from Sunday -0 till Saturday -6  ') + scale_y_discrete('Number of hourly entries')
    #plot = ggplot(df, aes('Day of week', 'ENTRIESn_hourly', fill= 'rain')) + geom_histogram( color= 'Blue') + scale_x_discrete('Days of Week', labels = c('0' = "Sunday", '1' = "Monday", '2' = "Tuesday" , '3' = "Wednesday", '4' = "Thursday", '5' = "Friday", '6' = "Saturday")) + ggtitle('Ridership by day of week alongwith variable rain as color') + scale_y_discrete('Number of hourly entries')
    plot = ggplot(df, aes( x='ENTRIESn_hourly' , fill='rain')) + facet_wrap('rain') + geom_histogram(stat= 'bin', binwidth=500) + ggtitle('Subway Ridership by Not raining Vs raining') + labs('Number of Hourly entries','Frequency' ) + xlim(0,8000)
    pandas.options.mode.chained_assignment = None
    #return plot

    return plot
