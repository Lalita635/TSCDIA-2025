
# 🧠 Proyecto ABP: Detección de Neumonía en Imágenes Médicas usando ML y Fairlearn

Este proyecto tiene como objetivo desarrollar un modelo de aprendizaje automático capaz de **detectar neumonía** a partir de imágenes médicas, garantizando un enfoque **ético, reproducible y justo**. Se sigue la metodología **TDSP** e incorpora herramientas como **MLflow** y **Fairlearn**.

---

## 📁 Estructura del Repositorio
(en constante actualización hasta finalizar el proyecto)

```
├── evidencia_1_definicion_del_problema/
│   ├── README.md
│   └── ...
├── notebooks/
│   ├── 01_eda_fairlearn.ipynb
│   ├── 02_preprocesamiento.ipynb
│   ├── 03_modelado_mlflow.ipynb
│   └── ...
├── data/
│   ├── raw/
│   ├── processed/
│   └── ...
├── src/
│   ├── preprocessing.py
│   ├── train.py
│   ├── deploy.py
│   └── ...
├── reports/
│   ├── data_summary.pdf
│   ├── model_report.pdf
│   ├── fairlearn_report.pdf
│   └── ...
├── mlruns/
│   └── (MLflow tracking data)
├── README.md
└── requirements.txt
```

---

## 🔍 Evidencias

### 1. Definición del Problema
- Formulación del problema de negocio.
- Stakeholders y métricas de éxito.
- Creación del **Project Charter**.
- Asignación de roles y estructura de trabajo.
> Ver carpeta: `[evidencia_1_definicion_del_problema/](https://github.com/Lalita635/TSCDIA-2025/tree/main/Neumonet/Evidencia_1_%20Definici%C3%B3n_del_problema)`

### 2. Análisis Exploratorio (EDA) y Fairlearn
- Exploración inicial del dataset.
- Identificación de variables sensibles (edad, género, etc.).
- Visualizaciones interactivas y estadísticas descriptivas.
- Análisis de equidad con **Fairlearn** (disparidades, proxy variables).

### 3. Preparación de los Datos
- Limpieza de datos (faltantes, outliers, errores).
- Codificación y escalado de variables.
- Balanceo de clases para mitigar sesgos.
- Generación del dataset final para modelado.

### 4. Modelado Inicial y Experimentación con MLflow
- Entrenamiento de modelos básicos (e.g., Logistic Regression, Random Forest).
- Registro y comparación de experimentos con **MLflow**.
- Selección del mejor modelo según métricas y equidad.

### 5. Despliegue del Modelo
- Empaquetado del modelo con MLflow.
- Exposición como API REST con Flask/FastAPI.
- Pruebas funcionales (Postman/cURL).
- Documentación del proceso y lecciones aprendidas.

---

## 🛠️ Tecnologías y Librerías

- `Python`, `Jupyter Notebooks`
- `Scikit-learn`, `Pandas`, `Matplotlib`, `Seaborn`
- `Fairlearn`, `MLflow`, `Plotly`
- `Flask` o `FastAPI` para el despliegue
- `Git`, `GitHub`, `Jira` para gestión de proyecto

---

## 📑 Documentos Importantes

| Documento | Descripción |
|----------|-------------|
| `Project Charter` | Visión general del proyecto |
| `data_definition.md` | Definición de los datos |
| `data_summary.pdf` | Limpieza y transformación |
| `model_report.pdf` | Comparación de modelos |
| `fairlearn_report.pdf` | Equidad del modelo |
| `deploymentdoc.md` | Proceso de despliegue |
| `exitreport.md` | Informe final de aceptación |

---

## 👥 Equipo

- **Project Manager:** ...
- **Data Scientist:** ...
- **Data Engineer:** ...
- **Ethical Reviewer:** ...
