from pandas import *
from ggplot import *

def plot_weather_data(turnstile_weather):
    ''' 
    plot_weather_data is passed a dataframe called turnstile_weather. 
    Use turnstile_weather along with ggplot to make another data visualization
    focused on the MTA and weather data we used in Project 3.
    
    Make a type of visualization different than what you did in the previous exercise.
    Try to use the data in a different way (e.g., if you made a lineplot concerning 
    ridership and time of day in exercise #1, maybe look at weather and try to make a 
    histogram in this exercise). Or try to use multiple encodings in your graph if 
    you didn't in the previous exercise.
    
    You should feel free to implement something that we discussed in class 
    (e.g., scatterplots, line plots, or histograms) or attempt to implement
    something more advanced if you'd like.

    Here are some suggestions for things to investigate and illustrate:
     * Ridership by time-of-day or day-of-week
     * How ridership varies by subway station
     * Which stations have more exits or entries at different times of day
       (You can use UNIT as a proxy for subway station.)

    If you'd like to learn more about ggplot and its capabilities, take
    a look at the documentation at:
    https://pypi.python.org/pypi/ggplot/
     
    You can check out the link 
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv
    to see all the columns and data points included in the turnstile_weather 
    dataframe.
     
   However, due to the limitation of our Amazon EC2 server, we are giving you a random
    subset, about 1/3 of the actual data in the turnstile_weather dataframe.
    '''
    #dummy_units = pandas.get_dummies(turnstile_weather['UNIT'])
    #turnstile_weather.UNIT = pandas.get_dummies(turnstile_weather['UNIT'])
    #turnstile_weather.UNIT = turnstile_weather.UNIT.astype(float).fillna(0)
    #Unit.UNIT = Unit.UNIT.astype(float).fillna(0.0)
    Date = turnstile_weather['DATEn'].apply(pandas.to_datetime)
    Date = Date.map(lambda x:x.strftime('%A'))
    #for x in range(len(Date)):
    #    Date[x] = datetime.datetime.strptime(Date[x], "%Y-%m-%d").strftime("%A")
    
    #df = turnstile_weather.join(pandas.DataFrame({'unit': dummy_units}))
    #df = turnstile_weather.join(dummy_units)[turnstile_weather.Hour >= 7]
    #df = df.join(pandas.DataFrame({'Day of week': Date}))
    #df =  turnstile_weather[turnstile_weather.UNIT == 'R008']
    df = turnstile_weather
    plot = ggplot(df, aes('Hour', 'ENTRIESn_hourly' , fill='rain')) + geom_histogram(stat='bin',binwidth= 1) + ggtitle('Ridership by Hour of the day') + labs('Hour of the day', 'Number of hourly entries')
    #plot = ggplot(df, aes( 'Hour', 'ENTRIESn_hourly' )) + geom_line(color='Blue') + stat_smooth(span=.15, color='black', se=True) + ggtitle ('Ridership by Hour of the day- lineplot') + xlab('Hour of the Day') + ylab('Hourly Entries')
    #plot = ggplot(df, aes( 'Hour', 'ENTRIESn_hourly' )) + geom_point(color= 'Blue') + geom_line(color='green') + ggtitle ('Ridership by Hour of the day- lineplot') + xlab('Hour of the Day') + ylab('Hourly Entries')
    pandas.options.mode.chained_assignment = None
    return plot
