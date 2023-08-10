LOAD DATA LOCAL INFILE '/mnt/DATA/Documents-PES/Placements/Swym/datasets/Train_details_22122017.csv'
INTO TABLE Stations
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(StationCode, StationName);

LOAD DATA LOCAL INFILE '/mnt/DATA/Documents-PES/Placements/Swym/datasets/Train_details_22122017.csv'
INTO TABLE Trains
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(TrainNo, TrainName, @dummy1, @dummy2, @dummy3, @dummy4, @dummy5, @dummy6, SourceStation, SourceStationName, DestinationStation, DestinationStationName);

LOAD DATA INFILE '/mnt/DATA/Documents-PES/Placements/Swym/datasets/Train_details_22122017.csv'
INTO TABLE TrainStops
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(TrainNo, @TrainName, SEQ, StationCode, ArrivalTime, DepartureTime, Distance, @dummy7, @dummy8, @dummy9, @dummy10, @dummy11, @dummy12)
SET ArrivalTime = STR_TO_DATE(@dummy7, '%H:%i:%s'),
    DepartureTime = STR_TO_DATE(@dummy8, '%H:%i:%s'),
    TrainName = @TrainName;

