CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL, 
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

-- Running upgrade  -> fc5709aa7470

INSERT INTO alembic_version (version_num) VALUES ('fc5709aa7470');

-- Running upgrade fc5709aa7470 -> 84b94b697e8b

ALTER TABLE laboratory_test ADD COLUMN tetris_score INTEGER;

UPDATE alembic_version SET version_num='84b94b697e8b' WHERE alembic_version.version_num = 'fc5709aa7470';

