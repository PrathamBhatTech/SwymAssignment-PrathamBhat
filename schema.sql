-- Create Stations table
CREATE TABLE Stations (
    StationCode VARCHAR(10) PRIMARY KEY,
    StationName VARCHAR(255)
);

-- Create Trains table
CREATE TABLE Trains (
    TrainNo INT PRIMARY KEY,
    TrainName VARCHAR(255),
    SourceStation VARCHAR(10),
    SourceStationName VARCHAR(255),
    DestinationStation VARCHAR(10),
    DestinationStationName VARCHAR(255)
);

-- Create TrainStops table
-- Create TrainStops table with TrainName
CREATE TABLE TrainStops (
    TrainNo INT,
    TrainName VARCHAR(255), -- Added column
    SEQ INT,
    StationCode VARCHAR(10),
    ArrivalTime TIME,
    DepartureTime TIME,
    Distance INT,
    PRIMARY KEY (TrainNo, SEQ),
    FOREIGN KEY (TrainNo) REFERENCES Trains(TrainNo),
    FOREIGN KEY (StationCode) REFERENCES Stations(StationCode)
);


-- Create indexes for better performance
CREATE INDEX idx_train_stops_station ON TrainStops (StationCode);
