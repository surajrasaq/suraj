########################################################################################################
# Data Analysis on World Development Indicators (Surajudeen Abdulrasaq MLDM M1) 
# It presents the most current and accurate global development data available,
# and includes national, regional and global estimates.
# Quesions :  What are the factors affecting global developments?
#             What country or region are developing faster?
#             What years are the country or region develop most
#             Is it possible to predict global development in 2018 using this data?
# Data Available at https://data.worldbank.org/data-catalog/world-development-indicators (World Bank)
#########################################################################################################


#SET PATH & Clear Space
path = ("~/R-Projects/world_devel")
setwd(path)
rm(list=ls(all = TRUE))


# READ ALL DATASET PROVIDED AND EXAMINE THEM
library(dplyr)
library(readr)
world_dev <- read.csv('WDIData.csv', check.names = FALSE)
summary(world_dev)


# png of my table

#library(gridExtra)
#png("wdata.png", height = 50*nrow(world_dev), width = 200*ncol(world_dev))
#grid.table(world_dev[1:20])
#dev.off()

# Check Structure & Rename Column for easy analysis 

str(world_dev)   #415800 obs. of  63 variables:

world_dev <- rename(world_dev, Indicator_Code = "Indicator Code", Indicator_Name = "Indicator Name", 
      Country_Code = "Country Code", Country_Name = "Country Name")

#################################################################################
# The Year Column (1960 1961 1962.....) is spread Across Rows.
# This will be difficults to deal with So i will Combine Multiple Columns 
# of Data into a Single Column to create the "Year" Necesary for efficent analysis
##################################################################################
# install.packages("tidyr")
library(tidyr)
world_dev <- gather(world_dev, Year, Values, -Country_Name, -Country_Code, -Indicator_Name, -Indicator_Code)

head(world_dev)
# Remove NA data and check statiscs with the structure
world_dev <- na.omit(world_dev)
#summary(world_dev)
str(world_dev)
head(world_dev)
tail(world_dev)


########################################################################################
# I regroup dataset using the Indicator_Code & Idicator_Name as an 
# important factor so we can easily visualise countries
# affected by this indicatos and the affected years the no of years
world_indi <- world_dev %>%
  group_by(Indicator_Code, Indicator_Name) %>%
  summarise(Num_of_Countries = n_distinct(Country_Code),
            Num_of_Years     = n_distinct(Year),
            FirstYear    = min(Year),
            LastYear     = max(Year))
world_indi$Indicator_Name <- sub("\\$", "dollar", world_indi$Indicator_Name)# replace $ symbol with dollar
str(world_indi)
summary(world_indi)
#write.csv(world_indi, file = 'world_indi.csv')

############################################################################################
# Now we have a set of new set of analyse data(world_indi) which tell us the NO. of countries affected by particular indicators
# The Number of years it affect them and from what year to what year this are spread out.
# Lets examine Maximum Number of countries and the Maximum Num of years Afected
# to know some very importants indicators
############################################################################################

max(world_indi$Num_of_Countries) # Maximum No of country afected by A OR some particular indicator = 263.
max(world_indi$Num_of_Years)# Maximum No or years this indicator has affected the country = 58 YEARS

# lETS DO SOME VISUALISATION WITH TOP 5 
library(plotrix)
library(ggplot2)

#X11(display = 'Impotant Indicator', 8,4)
#dev.copy(device = png, filename= 'plot1.png', width =1000, height = 500);
qplot(Indicator_Name,  Num_of_Countries, data = world_indi[1:5,], color= Num_of_Years)
#dev.off();

# lets do pie plot
#dev.copy(device = png, filename= 'plot2.png', width =1000, height = 500);
pie(world_indi$Num_of_Countries[1:5], labels = world_indi$Indicator_Code, explode = 0.1,main="Pie Chart of Important indicators ")
#dev.off();


# Agriculral land(both in land area and sq. meter.),seem to be very important Indicators 
# But we can explore further to be certain by extracting more information from our data-set
# Since we know the biggest number's of affected countries is 263
# i take a sample of this affect between 200 and 263 countiries to get to know how this indicator affected
# i create a new data-frame called Important_Indicators to take the list of most inportant indicators

Important_indicators <- world_indi[which(world_indi$Num_of_Countries > 200),]
#warning()
summary(Important_indicators)

# From the results Agriculral land is still the prevaling 
#lets visualise with a subset of this Important Indicators using ggplot
library(ggplot2)

#dev.copy(device = png, filename= 'plot3.png', width =1000, height = 500);
qplot(Indicator_Name, Num_of_Countries, data = Important_indicators[1:5,], color = Num_of_Years)
#dev.off();

# visualise using ggplot
#dev.copy(device = png, filename= 'plot4.png', width =1000, height = 500);
ggplot(data=Important_indicators[1:5,], aes(x=Indicator_Name, y=Num_of_Countries, fill=Num_of_Years)) +
  geom_bar(stat="identity", position=position_dodge())
#dev.off()
############################################################################################

# NOW I HAVE TWO DIFFRENT DATASET (world_dev and world_indi) WITH DIFFRENT USEFUL INFORMATION
# Now Combine the two dataset(world_indi and world_dev) in to single dataframe, this is 
# neccesary to see if there can be any surprise discovery,  i will analyse further before
# finally try to predict the 2018 outcome

#world_indi <- world_indi[,-(1:2), drop = FALSE] # Drop the first two col, which are already in world_dev
#str(world_indi)

# Now Combine the data-frame
data.combine <- merge(world_dev, world_indi)
summary(data.combine)

write.csv(data.combine, file = 'final.csv')

# Now i have a new data-frame let me check the importance of values.
table(data.combine$Values) # Values is a very impotant facor

#Check the correlation of values and year by visualisation
# the visualisation shows that most countries improove in Access to clean fuels and technologies for cooking
# through the years
dev.copy(device = png, filename= 'plot8.png', width =1200, height = 700);
ggplot(data=data.combine[1200:1211,], aes(x=Indicator_Name, y=Values, fill=Year)) +
  geom_bar(stat="identity", position=position_dodge())+
  facet_wrap(~Country_Name)+
  ggtitle(' Indicators Performance per Nation')
dev.off()


#lets visualise using MAP


#library(readr)
#library(rworldmap)

# Update these to plot different indicators
#indicatorName <- "Life expectancy at birth, total (years)"
#indicatorYear <- 2013

#indicators <- read_csv("../input/Indicators.csv")

#filtered <- indicators[indicators$IndicatorName==indicatorName & indicators$Year==indicatorYear,]
#write_csv(filtered, "filtered.csv")

#sPDF <- joinCountryData2Map(filtered,
 #                           joinCode = "ISO3",
  #                          nameJoinColumn = "CountryCode",
   #                         verbose = TRUE)

#png("map.png", width=900, height=550)
#mapCountryData(sPDF, nameColumnToPlot='Value', mapTitle=indicatorName)
#dev.off()

library(readr)
library(rworldmap)

# Update these to plot different indicators
indicator <- "Agricultural machinery, tractors"
year <- 2017

visual <- data.combine[data.combine$Indicator_Name==indicator & data.combine$Year==year,]
write_csv(visual, "visual.csv")

sPDF <- joinCountryData2Map(visual,
                            joinCode = "ISO3",
                            nameJoinColumn = "Country_Code",
                            verbose = TRUE)

png("map1.png", width=900, height=550)
mapCountryData(sPDF, nameColumnToPlot='Value', mapTitle=Indicator)
dev.off()

###########################################################################
# End of Data Analysis Now lets start Exploratory Modelling
###########################################################################


