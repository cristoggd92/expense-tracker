https://roadmap.sh/projects/expense-tracker

# Expense Tracker CLI

## Descripción
Este es un **rastreador de gastos** basado en línea de comandos (CLI) que permite a los usuarios agregar, eliminar, listar y resumir sus gastos de manera sencilla. Los datos se almacenan en un archivo JSON para facilitar su manejo.

## Características
✅ Agregar un gasto con descripción y monto.
✅ Eliminar un gasto por su ID.
✅ Listar todos los gastos registrados.
✅ Mostrar un resumen total de los gastos.
✅ Filtrar el resumen por mes del año actual.

## Requisitos
- Python 3.7+

## Instalación
Clona este repositorio y accede a la carpeta del proyecto:
```sh
git clone https://github.com/tu-usuario/expense-tracker.git
cd expense-tracker
```

## Uso
Ejecuta el script con los siguientes comandos:

### 1️⃣ Agregar un gasto
```sh
python expense_tracker.py add --description "Almuerzo" --amount 15
```

### 2️⃣ Listar todos los gastos
```sh
python expense_tracker.py list
```

### 3️⃣ Eliminar un gasto por ID
```sh
python expense_tracker.py delete --id 1
```

### 4️⃣ Ver resumen total de gastos
```sh
python expense_tracker.py summary
```

### 5️⃣ Ver resumen por mes específico
```sh
python expense_tracker.py summary --month 8
```

## Almacenamiento de Datos
El programa almacena los datos en un archivo `expenses.json` en el mismo directorio del script.

## Contribuciones
¡Las contribuciones son bienvenidas! Si deseas mejorar el proyecto, abre un *pull request* o reporta un problema en la sección de *issues*.

## Licencia
Este proyecto está bajo la licencia MIT.
