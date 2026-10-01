# Registro y listado de productos (Django)

Aplicación web hecha con Django para registrar, listar, consultar y editar productos.

## Funcionalidades

- Listado de productos en la página principal (`/`)
- Registro de nuevos productos (`/productos/nuevo/`)
- Detalle de un producto (`/productos/<id>/`)
- Edición de un producto (`/productos/<id>/editar/`)

## Modelo

**Producto**

| Campo     | Tipo                              |
|-----------|-----------------------------------|
| nombre    | CharField (máx. 100)              |
| categoria | CharField (máx. 50)               |
| precio    | DecimalField (10 dígitos, 2 dec.) |
| cantidad  | IntegerField                      |

## Requisitos

- Python 3.11
- Django

## Instalación y ejecución

1. Clonar el repositorio:

   ```
   git clone https://github.com/franksmithhurtadohurtado-ai/Django_pagina_web.git
   cd Django_pagina_web
   
   ```

2. Crear y activar el entorno virtual (Windows):

   ```
   python -m venv .venv
   .venv\Scripts\activate.bat
   ```

3. Instalar Django:

   ```
   pip install django
   ```

4. Entrar a la carpeta del proyecto y aplicar las migraciones:

   ```
   cd tienda
   python manage.py migrate
   ```

5. Ejecutar el servidor:

   ```
   python manage.py runserver
   ```

6. Abrir en el navegador: http://127.0.0.1:8000/

## Estructura del proyecto

```
tienda/
├── manage.py
├── tienda/          # configuración del proyecto (settings.py, urls.py)
├── productos/       # app: models.py, forms.py, views.py, urls.py
└── templates/       # listado.html, formulario.html, detalle.html
```

## Autor

Frank