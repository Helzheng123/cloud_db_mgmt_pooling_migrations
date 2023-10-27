CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL, 
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

-- Running upgrade  -> 9ce609e5ef7e

INSERT INTO alembic_version (version_num) VALUES ('9ce609e5ef7e');

-- Running upgrade 9ce609e5ef7e -> d4eba5ccb934

ALTER TABLE laboratory_test ADD COLUMN suika_score INTEGER;

UPDATE alembic_version SET version_num='d4eba5ccb934' WHERE alembic_version.version_num = '9ce609e5ef7e';

