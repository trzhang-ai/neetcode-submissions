CREATE TABLE scores (
    id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    score INTEGER,
    region TEXT
);

INSERT INTO scores (score, region) VALUES
    (60, 'EU'),
    (88, 'EU'),
    (75, 'NA'),
    (95, 'NA'),
    (60, 'AS'),
    (75, 'EU'),
    (45, 'NA'),
    (100, 'EU');
-- Do not modify above this line. --


select
    round(min(score), 0) as min_score,
    round(max(score), 0) as max_score,
    round(avg(score), 0) as avg_score
from scores
where region = 'EU';


