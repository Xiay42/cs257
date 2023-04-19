/*       databse-schema    */
/*    Written by Yiming Xia   */
/*    A list of CREATE TABLE statements    */

CREATE TABLE modelTable(
    id SERIAL,
    modle text,
    make text,
    vehicle_class text,
    engine_size float,
    cyliners float
);
CREATE TABLE fuelTable(
    id SERIAL,
    fuel_type text,
    consumption_city float,
    consumption_hwy float,
    consumption_comb float
);
CREATE TABLE co2Table(
    id SERIAL,
    co2_emission float,
    co2_rating int,
    smog_rating int
);
CREATE TABLE linksTable(
    modelID integer,
    fuelID integer,
    co2ID integer
);