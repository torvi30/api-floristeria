# Manual de Software

## Introducción

### Propósito del Manual
Este manual tiene como objetivo guiar al usuario en la instalación, configuración y uso del sistema de gestión para la floristería. Incluye información sobre los módulos principales, diagramas de flujo y estructura de datos, facilitando la comprensión y el mantenimiento del software. Es fundamental para asegurar el correcto funcionamiento y evolución del sistema.

### Audiencia Objetivo
El manual está dirigido a desarrolladores, administradores de sistemas y usuarios técnicos con conocimientos básicos de Python, bases de datos y APIs REST. Se recomienda experiencia previa en el uso de FastAPI y manejo de entornos virtuales en Python.

### Alcance
Este documento cubre la instalación, configuración y uso de los módulos principales: gestión de productos, pedidos y usuarios. No incluye detalles sobre la infraestructura de producción, integración con sistemas externos ni personalización avanzada fuera del alcance del código fuente proporcionado.

## Descripción General del Software

### Visión General
El software es una API REST desarrollada en Python usando FastAPI y SQLAlchemy, diseñada para gestionar productos, pedidos y usuarios en una floristería. Permite la administración eficiente de inventario, registro de ventas y control de usuarios. El desarrollo surge de la necesidad de digitalizar y automatizar procesos internos.

### Características Principales
- **Gestión de productos:** Alta, consulta, actualización y eliminación de productos.
- **Gestión de pedidos:** Creación, consulta, actualización y eliminación de pedidos, con control de stock automático.
- **Gestión de usuarios:** Registro, recuperación y actualización de contraseñas.
- **Control de stock:** Actualización automática al realizar pedidos.
- **API REST:** Endpoints claros y documentados para integración con otros sistemas.

#### Diagramas de referencia
- [Flujo de productos](./puml/products.puml)
- [Flujo de pedidos](./puml/orders.puml)
- [Flujo de login/usuarios](./puml/login.puml)
- [Modelo de datos](./puml/db.puml)

### Requisitos del Sistema
- **Hardware:** PC con al menos 2GB de RAM y 100MB de espacio libre.
- **Software:**  
  - Python 3.10 o superior  
  - pip  
  - Sistema operativo: Windows 10/11, Linux o macOS  
  - Acceso a una base de datos SQLite (por defecto) o PostgreSQL/MySQL (opcional)

## Instalación

### Requisitos Previos
- Tener instalado Python 3.10 o superior.
- Instalar `pip` (gestor de paquetes de Python).
- Acceso a la terminal o consola de comandos.
- (Opcional) Editor de código como Visual Studio Code.

### Pasos de Instalación

1. **Clonar el repositorio:**
   ```sh
   git clone <URL_DEL_REPOSITORIO>
   cd api-floristeria
   ```

2. **Crear y activar un entorno virtual:**
   ```sh
   python -m venv venv
   venv\Scripts\activate   # En Windows
   # source venv/bin/activate   # En Linux/Mac
   ```

3. **Instalar dependencias:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Configurar la base de datos:**
   - Por defecto se usa SQLite. Para otros motores, editar la cadena de conexión en `db.py`.

5. **Inicializar la base de datos:**
   ```sh
   python db.py
   ```

6. **Ejecutar el servidor:**
   ```sh
   uvicorn main:app --reload
   ```

7. **Acceder a la documentación interactiva:**
   - Abrir [http://localhost:8000/docs](http://localhost:8000/docs) en el navegador.

---

*Continúa con la configuración y uso de los módulos en las siguientes secciones del manual.*

## Configuración y Uso de los Módulos

### Gestión de Productos

#### Crear Producto
Para crear un producto, realiza una petición POST al endpoint `/products` con los datos requeridos (nombre, tipo, precio, stock, etc.).  
Consulta el diagrama [Flujo de productos](./puml/products.puml) para visualizar el proceso.

#### Consultar Productos
Utiliza el endpoint GET `/products` para obtener la lista de productos registrados.

#### Actualizar Producto
Envía una petición PUT a `/products/{id}` con los campos a modificar.

#### Eliminar Producto
Realiza una petición DELETE a `/products/{id}` para eliminar el producto seleccionado.

---

### Gestión de Pedidos

#### Crear Pedido
Envía una petición POST a `/orders` con los datos del cliente y los detalles del pedido. El sistema verifica el stock y descuenta automáticamente las unidades.  
Consulta el diagrama [Flujo de pedidos](./puml/orders.puml).

#### Consultar Pedidos
Utiliza el endpoint GET `/orders` para obtener todos los pedidos.

#### Consultar Pedido por ID
Envía una petición GET a `/orders/{id}` para obtener los detalles de un pedido específico.

#### Actualizar Pedido
Realiza una petición PUT a `/orders/{id}` para modificar los detalles del pedido. El sistema ajusta el stock según los cambios realizados.

#### Eliminar Pedido
Envía una petición DELETE a `/orders/{id}` para eliminar el pedido y revertir el stock de los productos involucrados.

---

### Gestión de Usuarios

#### Recuperación de Contraseña
Envía una petición POST a `/password-recovery` con el email del usuario. El sistema enviará un correo con el enlace de recuperación.  
Consulta el diagrama [Flujo de login/usuarios](./puml/login.puml).

#### Restablecer Contraseña
Envía una petición POST a `/reset-password` con el token recibido y la nueva contraseña.

---

## Modelo de Datos

Consulta el diagrama [Modelo de datos](./puml/db.puml) para entender las relaciones entre las entidades principales: Producto, Pedido, Detalle de Pedido y Usuario.

---

## Soporte y Contacto

Para dudas, soporte o reportes de errores, contacta al equipo de desarrollo o consulta la documentación técnica incluida en el repositorio.