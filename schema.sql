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
    DestinationStation VARCHAR(10),
    FOREIGN KEY (SourceStation) REFERENCES Stations(StationCode),
    FOREIGN KEY (DestinationStation) REFERENCES Stations(StationCode)
);

-- Create TrainStops table
CREATE TABLE TrainStops (
    TrainNo INT,
    SEQ INT,
    StationCode VARCHAR(10),
    ArrivalTime TIME,
    DepartureTime TIME,
    Distance INT,
    FOREIGN KEY (TrainNo) REFERENCES Trains(TrainNo),
    FOREIGN KEY (StationCode) REFERENCES Stations(StationCode)
);


-- Create indexes for better performance
CREATE INDEX idx_train_stops_station ON TrainStops (StationCode);
