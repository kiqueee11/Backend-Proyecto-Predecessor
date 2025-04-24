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
- **Ruta:** `Post /equipos/update/<slug:slug>`
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

> 💡 Todos los endpoints devuelven respuestas en formato JSON.
