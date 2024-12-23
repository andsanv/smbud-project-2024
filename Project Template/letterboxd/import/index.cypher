CREATE INDEX index_on_movie_id FOR (m:Movie) ON m.id;
CREATE INDEX index_on_actor FOR (a:ACTOR) ON a.name;
CREATE INDEX index_on_crew FOR (c:Crew) ON c.name;
CREATE INDEX index_on_languages FOR (l:Language) ON l.name;
CREATE INDEX index_on_studio FOR (s:Studio) ON s.name;
CREATE INDEX index_on_countries FOR (c:Country) ON c.name;
CREATE INDEX index_on_genres FOR (g:Genre) ON g.name;
CREATE INDEX index_on_themes FOR (t:Theme) ON t.name;
