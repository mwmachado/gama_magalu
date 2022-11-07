CREATE VIEW view_avaliacoes AS
SELECT
    a.id AS id_avaliacao,
    u.usuario,
    u.sexo,
    f.filme,
    a.nota
FROM avaliacoes AS a
  LEFT JOIN filmes AS f
    ON f.id = a.filme
  LEFT JOIN usuarios AS u
    ON u.id = a.usuario
;