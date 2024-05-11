# CATY_Management
All in one place to keep track of home life

# Strcture
1. Utilities Data
   - Record Data
   - Data Analysis
   - Data Forecast
2. Home Spending
3. Vehicle management

# what is inside
1. Utilities data:

**Table**: 
__meters__ (this table structure and define the data that is being used in other tables)
_Fields_
1. id_meter(PK): int4, format: 0000. Unique, sequential, autoincrease
2. date_creation_meter: date, auto: now() format yyyy-mm-dd hh:mm (UTC?)
3. meter_serial: serial number/EAN number of physical meter
4. consumption_meter: boolean True (consumption/injection)
5. consumption_type: (gas, water, electricity, ?)
6. date_start_serv: when the meter start to record info date mandatory format: yyyy-mm-dd hh:mm
7. date_end_serv: when the meter stop to record info format:yyyy-mm-dd hh:mm
8. meter_dependant: from where this meter depends: id_meter of the correponding meter (if its main so itslef) eg: if is the meter that register consumption in a specific machine is dependant of the main meter
9. id_site: FK related to adress
10. name_meter: to made easier identification
11. unit: kwh, m3, ...
12. time_granurality ??? is it necesary???
13. source: (if measure is not local?) ??? is it necesary???


__site__ descrpition: This table contains the info necessary to identify the place where the follow is made
1. id_site PK
2. name_site
3. lat
4. lon
5. adress (street and number)
6. town
7. postal_code
8. country
9. start_tracking
10. end_tracking
11. type (in case you are following several places eg: main residence, vacations, rental)
12. date_creation
13. type_building

__meter_data__
1. id_md PK
2. date_utc datetime
3. id_meter FK
4. value


**set reminder to control**
**introduce the meassure from qr_code**




__weather__
1. id_weather
2. date_time (1h/3h? forecast)
3. code_weather
4. temperature
5. pressure
6. humidity
7. solar_exposure
8. clouds
9. 