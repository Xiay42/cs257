CREATE TABLE gamesTable(
    id SERIAL,
    game_name text,
    city text
);


CREATE TABLE athletesTable(
    id SERIAL,
    name text
);


CREATE TABLE eventsTable(
    id SERIAL,
    sport text,
    event_name text
);


CREATE TABLE nocsTable(
    id SERIAL,
    noc text,
    region text
);


CREATE TABLE linksTable(
    gameID integer,
    eventID integer,
    nocID integer,
    athleteID integer,
    medal text
);


CREATE TABLE GMTable(
    nocID integer,
    gm integer
);