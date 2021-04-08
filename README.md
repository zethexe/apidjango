# apidjango
Api de peliculas construido con Django

CLASIFICACION
	GET: /clasificacion/
	GET por ID: /clasificacion/id/
	POST:/clasificacion/, parametros (name,description)
	PUT:/clasificacion/id/, parametros (name,description)
	DELETE: /clasificacion/id/




GENERO
	GET: /genero/
	GET por ID: /genero/id/
	POST:/genero/, parametros (description)
	PUT:/genero/id/, parametros (description)
	DELETE: /genero/id/


ACTOR
	GET: /actor/
	GET por ID: /actor/id/
	POST:/actor/, parametros (name,nationality)
	PUT:/actor/id/, parametros (name,nationality)
	DELETE: /actor/id/


DIRECTOR
	GET: /director/
	GET por ID: /director/id/
	POST:/director/, parametros (name,nationality)
	PUT:/director/id/, parametros (name,nationality)
	DELETE: /director/id/


PELICULAS
	GET: /peliculas/
	GET por ID: /peliculas/id/
	POST:/peliculas/, parametros (title,duration,sinopsis,datelauch,clasification(id),genre(id),director(id))
	PUT:/peliculas/id/, parametros (title,duration,sinopsis,datelauch,clasification(id),genre(id),director(id))
	DELETE: /peliculas/id/


REPARTO
	GET: /reparto/
	GET por ID: /reparto/id/
	POST:/reparto/, parametros (character, actor(id),movie(id))
	PUT:/reparto/id/, parametros (character, actor(id),movie(id))
	DELETE: /reparto/id/
