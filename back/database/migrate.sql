CREATE TABLE events (
        id INTEGER PRIMARY KEY,
        Description TEXT NOT NULL,
        Requierement TEXT NOT NULL,
        Prix INTEGER,
        Placerestante INTEGER,
        Lieux TEXT NOT NULL,
        Date TEXT NOT NULL,
        titre  TEXT NOT NULL,
        Img TEXT NOT NULL
       
);

CREATE TABLE Users (
        id INTEGER PRIMARY KEY,
        Pseudo TEXT NOT NULL,
        Email  TEXT NOT NULL,
        Style TEXT NOT NULL,
        Description TEXT NOT NULL,
        Avatar TEXT NOT NULL,
        Password TEXT
);

