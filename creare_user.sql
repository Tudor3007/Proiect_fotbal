-- rulat conectat ca postgres
CREATE DATABASE goal_gear;

-- rulat in baza goal_gear
CREATE USER tudor_django WITH ENCRYPTED PASSWORD 'qwerty';
GRANT ALL ON DATABASE goal_gear TO tudor_django;
CREATE SCHEMA django AUTHORIZATION tudor_django;
ALTER ROLE tudor_django SET search_path = django, public;
GRANT ALL ON SCHEMA django TO tudor_django;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA django TO tudor_django;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA django TO tudor_django;
GRANT ALL PRIVILEGES ON ALL FUNCTIONS IN SCHEMA django TO tudor_django;