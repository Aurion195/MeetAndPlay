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
        prenom TEXT NOT NULL,
        age INTEGER NOT NULL,
        jeu_favoris TEXT NOT NULL,
        activité_recente TEXT NOT NULL,
        nombre_victoire INTEGER NOT NULL,
        note INTEGER NOT NULL,
        niveau INTEGER NOT NULL
);

CREATE TABLE jeu (
        id INTEGER PRIMARY KEY,
        img TEXT NOT NULL,
        link  TEXT NOT NULL

);

