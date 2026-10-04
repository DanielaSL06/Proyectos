# 04. Procesamiento Simultáneo (Concurrente) y Conexión a Bases de Datos

## Especificaciones Técnicas
* **Lenguaje de programación:** C# (.NET / .NET Framework)
* **Entorno de Desarrollo (IDE):** Microsoft Visual Studio (`ProyectoDesa3.sln`)
* **Base de Datos:** Microsoft SQL Server / SQL Server Express
* **Tecnologías de Acceso a Datos:** ADO.NET (`SqlConnection`, `SqlCommand`) / Entity Framework
* **Manejo de Concurrencia:** Hilos y Tareas Asíncronas (`System.Threading`, `System.Threading.Tasks`, `async/await`)
* **Estructura:** Solución de Visual Studio (`.sln`) y archivo de proyecto (`.csproj`)

---

## Descripción del Proyecto
Este proyecto aborda la transición del procesamiento de datos secuencial hacia arquitecturas concurrentes y multi-hilo, integrando un motor de base de datos relacional para la gestión y persistencia segura de información en tiempo real.

El desarrollo abarca los siguientes componentes clave:

1. **Gestión de Concurrencia e Hilos Asíncronos:**
   * **Programación Multihilo:** Uso de tareas asíncronas (`Task`) e hilos de ejecución en paralelo para atender múltiples entradas de información simultáneamente sin congelar el hilo principal (*Main Thread*).
   * **Control de Flujo:** Manejo de bloques de ejecución asíncrona para evitar congelamientos del sistema ante ráfagas de datos.

2. **Integración y Persistencia en SQL Server:**
   * **Arquitectura Relacional:** Sustitución del almacenamiento en archivos de texto plano por un modelo relacional en SQL Server.
   * **Operaciones DML Seguras:** Ejecución de consultas SQL parametrizadas para la inserción y actualización de registros garantizando la integridad de los datos.

---

## Instrucciones de Ejecución

1. Abrir la solución **`ProyectoDesa3.sln`** en **Microsoft Visual Studio**.
2. Configurar la cadena de conexión (*ConnectionString*) en el archivo de configuración (`App.config` o `appsettings.json`) hacia la instancia de SQL Server local o remota.
3. Asegurarse de que la base de datos y las tablas relacionales correspondientes estén creadas en el servidor SQL.
4. Compilar la solución en Visual Studio (`Ctrl + Shift + B`).
5. Ejecutar la aplicación pulsando **F5** o mediante el botón de inicio.

---
