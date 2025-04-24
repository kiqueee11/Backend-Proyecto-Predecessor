## 📦 Endpoints - Equipos

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
- **Ruta:** `PUT /equipos/update/<slug:slug>`
- **Descripción:** Actualiza los datos de un equipo específico usando su `slug`.
- **Parámetros requeridos:**
  - `slug` en la URL
  - Datos a actualizar (nombre, victorias, derrotas, imagen)

---

## 🧙 Endpoints - Personajes

### 📥 Obtener Todos los Personajes
- **Ruta:** `GET /personajes/getAll`
- **Descripción:** Recupera todos los personajes disponibles.

---

## ⚽ Endpoints - Jugadores

### 📥 Obtener todos los jugadores
- **Ruta:**  `GET /jugadores/info/<slug:slug>`
- **Descripción:** Recupera toda la información de los jugadores de un equipo específico con sus respesctivas redes sociales y sus links.
- **Parámetros requeridos:**
  - `slug` del equipo en la URL
 
---

> 💡 Todos los endpoints devuelven respuestas en formato JSON.
