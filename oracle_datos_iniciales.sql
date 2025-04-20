
-- Script para insertar datos iniciales en Oracle
-- Categorías base para RetroPlay

INSERT INTO retrostore_categoria (id, nombre)
VALUES (1, 'Nintendo');

INSERT INTO retrostore_categoria (id, nombre)
VALUES (2, 'Sega');

INSERT INTO retrostore_categoria (id, nombre)
VALUES (3, 'PlayStation');

INSERT INTO retrostore_categoria (id, nombre)
VALUES (4, 'Atari');

INSERT INTO retrostore_categoria (id, nombre)
VALUES (5, 'Dreamcast');

COMMIT;
