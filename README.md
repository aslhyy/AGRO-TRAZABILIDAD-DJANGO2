# 🪏🌱 Sistema de Trazabilidad Agrícola – Django REST Framework 🌱🪏

Proyecto académico desarrollado en Django REST Framework que implementa un sistema modular para gestionar la trazabilidad completa de productos agrícolas desde su producción hasta su entrega.
Incluye 3 aplicaciones independientes y totalmente integradas: Lotes, Procesos y Transporte.

## 1. 🎯 Objetivo del Proyecto
Crear una API profesional, documentada y modular que permita gestionar los datos clave del proceso agrícola y visualizar la trazabilidad completa de cada lote.

## 2. 🖥️ Tecnologías

* Python 3.15 <br>
* Django 5 <br>
* Django REST Framework <br>
* django-environ <br>
* drf-spectacular (Swagger/OpenAPI) <br>
* Git / GitHub <br>

## 3. 📂 Estructura General del Proyecto
``` bash
proyecto/
│── proyecto/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
│── lotes/           (Aslhy)
│   ├── mod_lotes.py
│   ├── mod_trazabilidad.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── tests.py
│
│── procesos/        (Dayana)
│   ├── mod_procesos.py
│   ├── mod_detalles.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── tests.py
│
│── transporte/      (Riveros)
│   ├── mod_transporte.py
│   ├── mod_destinos.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── tests.py
│
│── .env.example
│── manage.py
│── README.md
```

## 4. 💿 Variables de Entorno (.env)

**Archivo .env requerido:**

``` python
DB_NAME=agro_trazabilidad
DB_USER=root
DB_PASSWORD=""
DB_HOST=localhost
DB_PORT=3306
DEBUG=True
SECRET_KEY="aaaa"
```

**Archivo .env.example incluido en el repositorio.**

## 5. 🛠️ Instalación y Ejecución
  
  * Clonar repositorio
    ```bash 
    git clone <url-del-repo>
    cd proyecto
    ```

  * Crear entorno virtual
    ```bash
    python -m venv venv
    source venv/Scripts/activate
    ```

  * Instalar dependencias
    ``` bash
    pip install -r requirements.txt
    ```

  * Configurar variables de entorno
    ``` bash
    cp .env.example .env
    ```
      Modificar valores según tu máquina.

  * Migraciones
    ```bash
    python manage.py migrate
    ```

  * Ejecutar servidor
    ``` bash
    python manage.py runserver
    ```

## 6. ⚙️ Aplicaciones del Proyecto

### -> LOTES – (Aslhy) 🌱
#### Funciones:
* CRUD de Lotes
* Filtro por cultivo y estado
* Validación: fecha de siembra no futura
* Módulo de trazabilidad por lote
* Endpoint maestro:
  **_GET /lotes/<id>/trazabilidad/_**

#### Modelos principales:
* Lote
* HistorialLote

### -> PROCESOS – (Dayana) 📋
#### Funciones:
* CRUD de Procesos
* CRUD de Detalles de Proceso
* Validación:
  **_si tipo = lavado → duración mínima 5 min_**
* Filtros por tipo y fecha
* Endpoint especial:
  **_GET /procesos/<id>/resumen/_**

#### Modelos principales:
* Proceso
* DetalleProceso

### -> TRANSPORTE – (Riveros) 🚜
#### Funciones:
* CRUD de Transporte
* **Filtros:** placa, fecha, temperatura
* CRUD de Destinos
* Validación: temperatura ≤ 10 °C
* Endpoint especial:
  **_GET /transporte/rutas/activas/_**

#### Modelos principales:
* Transporte
* Destino

## 7. 📍 Endpoint Global de Trazabilidad
**_GET /trazabilidad/completa/<lote_id>/_**

#### Entrega:
* Información del lote
* Historial
* Procesos aplicados
* Transporte asociado
* Destino final o ruta activa

## 8. 📄 Documentación Swagger/OpenAPI 

Una vez levantado el servidor:

```swift
/api/schema/swagger-ui/
/api/schema/redoc/
```

## 9. 💼 Flujo de Trabajo con Git
### Ramas utilizadas:
```bash
feature-lotes
feature-procesos
feature-transporte
```

### Proceso:
1. Cada miembro desarrolla en su rama.
2. Crea un Pull Request hacia main.
3. El líder (Aslhy) revisa y aprueba.
4. Se asegura que main esté siempre funcional.

## 10. ✔️ Roles del Equipo
| Integrante  | Rol         | App        | Responsabilidades                                                      |
| ----------- | ----------- | ---------- | ---------------------------------------------------------------------- |
| **Aslhy**   | Líder       | Lotes      | Módulo de lotes, trazabilidad por lote, integración general, PR review |
| **Dayana** | Dev Backend | Procesos   | Procesos, validaciones, estadísticas, detalle de procesos              |
| **Riveros**  | Dev Backend | Transporte | Vehículos, rutas activas, destinos, validaciones                       |
