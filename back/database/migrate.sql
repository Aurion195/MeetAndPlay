CREATE TABLE events (
        id INTEGER PRIMARY KEY,
        link TEXT NOT NULL,
        title  TEXT NOT NULL,
        Img TEXT NOT NULL,
        description TEXT NOT NULL
);
CREATE TABLE Users (
        id INTEGER PRIMARY KEY,
        Pseudo TEXT NOT NULL,
        Email  TEXT NOT NULL,
        Style TEXT NOT NULL,
        description TEXT NOT NULL
);

