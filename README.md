## Endpoints - Equipos

### ➕ Crear Equipo
- **Ruta:** `POST /equipos/create`
- **Descripción:** Crea un nuevo equipo.
- **Parámetros requeridos:**
  - `nombre` (string)
  - `victorias` (int)
  - `derrotas` (int)
  - `imagen` (opcional, archivo)

---

### 📥 Obtener Todos los Equipos
- **Ruta:** `GET /equipos/getAll`
- **Descripción:** Recupera todos los equipos disponibles.

---

### ✏️ Actualizar Equipo
- **Ruta:** `Post /equipos/update/<slug:slug>`
- **Descripción:** Actualiza los datos de un equipo específico usando su `slug`.
- **Parámetros requeridos:**
  - `slug` en la URL
  - Datos a actualizar (nombre, victorias, derrotas, imagen)

---

##  Endpoints - Personajes

### 📥 Obtener Todos los Personajes
- **Ruta:** `GET /personajes/getAll`
- **Descripción:** Recupera todos los personajes disponibles.

---

##  Endpoints - Jugadores

### 📥 Obtener todos los jugadores
- **Ruta:**  `GET /jugadores/info/<slug:slug>`
- **Descripción:** Recupera toda la información de los jugadores de un equipo específico con sus respesctivas redes sociales y sus links.
- **Parámetros requeridos:**
  - `slug` del equipo en la URL
 
---

##  Endpoints - Partidas

### 📥 Obtener todas las partidas
- **Ruta:** `GET /partidas`
- **Descripción:** Recupera todas las partidas registradas en el sistema.

---

### 🌀 Ruleta Eliminadora
- **Ruta:** `GET /partidas/ruleta-eliminadora/<str:slug>` (SLUG DE LA PARTIDA)
- **Descripción:** Devuelve los datos iniciales para iniciar el draft con la ruleta eliminadora.
- **Respuesta incluye:**
  - `primer_equipo_elegir`: El primer equipo que elige (determinado aleatoriamente con un cara o cruz).
  - `personajes_baneados`: Array de 10 personajes seleccionados aleatoriamente.
  - `personajes_restantes`: Array con los personajes restantes, que son los disponibles para la ruleta de selección.

---

##  Endpoints - Usuarios

### 🔐 Login de Usuario
- **Ruta:** `POST /usuarios/login`
- **Descripción:** Inicia sesión y devuelve los datos necesarios para la autenticación y control de acceso.
- **Respuesta incluye:**
  - `slug`: Identificador único del usuario.
  - `access_token`: Token de acceso para autenticación. `(NO LO USAMOS EN NINGUNA LLAMADA. POR AHORA NO SIRVE DE NADA)`
  - `is_staff`: Booleano que indica si el usuario tiene permisos de staff. `(RECOMENDACIÓN -> El rol de staff puede ser para los representantes de cada equipo)`
  - `is_superuser`: Booleano que indica si el usuario tiene permisos de superusuario. `(RECOMENDACIÓN -> El rol superuser puede ser para el admin de la app)`
 
---

> 💡 Todos los endpoints devuelven respuestas en formato JSON.
