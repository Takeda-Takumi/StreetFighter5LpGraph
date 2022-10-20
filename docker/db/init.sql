create table online_match
(
    access_date datetime not NULL,
    fighters_id VARCHAR(16) not NULL,
    league_point MEDIUMINT UNSIGNED not NULL,
    wins MEDIUMINT UNSIGNED not NULL,
    loses MEDIUMINT UNSIGNED not NULL
);

INSERT INTO online_match VALUES (cast('3000-01-01 00:00:00' as datetime), 'test', 100, 50, 25);
INSERT INTO online_match VALUES (cast('3000-01-01 01:00:00' as datetime), 'test', 200, 50, 25);
INSERT INTO online_match VALUES (cast('3000-01-01 02:00:00' as datetime), 'test', 300, 50, 25);

