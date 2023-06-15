/*
Create the various views that are fundamental to our project
June 14, 2023
*/


-- Create view with 2017 crashes
CREATE VIEW boston_crash_reports_2017 as
SELECT *
FROM boston_crash_reports
WHERE dispatch_ts like '2017%';


-- Create view with 2020 crashes
CREATE VIEW boston_crash_reports_2022 as
SELECT *
FROM boston_crash_reports
WHERE dispatch_ts like '2022%';


-- Create view with 2017 fatalities
CREATE VIEW boston_fatality_report_2017 as
SELECT *
FROM boston_fatality_report
WHERE date_time like '2017%';


-- Create view with 2020 fatalities
CREATE VIEW boston_fatality_report_2022 as
SELECT *
FROM boston_fatality_report
WHERE date_time like '2022%';



-- Find a bike that Zack rode
SELECT * 
FROM bluebike_trips2022
WHERE start_station_name = "Stony Brook T Stop" 
	and end_station_name = "Beacon St at Tappan St"
	and starttime like '2022-07-17 00:35%';  -- convert to UTC time

	
-- Select one bike to follow
CREATE VIEW bike_5001 as
SELECT *
FROM bluebike_trips2022
WHERE bikeid = 5001;
