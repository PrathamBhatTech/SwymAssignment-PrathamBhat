LOAD DATA LOCAL INFILE '/mnt/DATA/Documents-PES/Placements/Swym/datasets/Train_details_22122017.csv'
INTO TABLE Stations
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(@dummy1, @dummy2, @dummy3, StationCode, StationName, @dummy4, @dummy5, @dummy6, @dummy7, @dummy8, @dummy9, @dummy10);
SET StationCode = TRIM(StationCode),
    StationName = TRIM(StationName)
ON DUPLICATE KEY UPDATE StationName = StationName;


CREATE TEMPORARY TABLE TempTrains (
    TrainNo INT PRIMARY KEY,
    TrainName VARCHAR(255),
    SourceStation VARCHAR(255),
    DestinationStation VARCHAR(255)
);

LOAD DATA LOCAL INFILE '/mnt/DATA/Documents-PES/Placements/Swym/datasets/Train_details_22122017.csv'
INTO TABLE TempTrains
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(TrainNo, TrainName, @dummy1, @dummy2, @dummy3, @dummy4, @dummy5, @dummy6, SourceStation, @dummy7, DestinationStation, @dummy8);

INSERT IGNORE INTO Trains (TrainNo, TrainName, SourceStation, DestinationStation)
SELECT TrainNo, TrainName, SourceStation, DestinationStation FROM TempTrains;


LOAD DATA LOCAL INFILE '/mnt/DATA/Documents-PES/Placements/Swym/datasets/Train_details_22122017.csv'
INTO TABLE TrainStops
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(TrainNo, @TrainName, SEQ, StationCode, @dummy13, ArrivalTime, DepartureTime, Distance, @dummy7, @dummy8, @dummy9, @dummy10);

