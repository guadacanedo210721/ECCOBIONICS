# ECCOBIONICS — Sistema Web de Control de Asistencia

## 🎯 Descripción

Sistema empresarial profesional de control de asistencia con reconocimiento facial, escaneo QR y dashboard en tiempo real.

## 🏗️ Stack Tecnológico

### Frontend
- React 18 + Vite
- Tailwind CSS
- React Router DOM
- Axios
- Zustand
- React QR Scanner
- React Webcam
- Lucide React

### Backend
- FastAPI
- PostgreSQL
- SQLAlchemy
- JWT Authentication
- Redis
- InsightFace
- OpenCV

### Infraestructura
- Docker
- Docker Compose
- Nginx

## 📁 Estructura del Proyecto

```
ECCOBIONICS/
├── frontend/
│   ├── src/
│   │   ├── api/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── store/
│   │   ├── hooks/
│   │   ├── layouts/
│   │   ├── routes/
│   │   ├── styles/
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── public/
│   ├── package.json
│   └── vite.config.js
├── backend/
│   ├── app/
│   │   ├── core/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── routes/
│   │   ├── services/
│   │   ├── utils/
│   │   └── main.py
│   ├── requirements.txt
│   └── Dockerfile
├── ai-service/
│   ├── face_engine.py
│   └── embeddings/
├── nginx/
│   └── default.conf
├── docker-compose.yml
└── .env.example
```

## 🚀 Inicio Rápido

### Con Docker
```bash
docker-compose up --build
```

### Desarrollo Local

**Frontend:**
```bash
cd frontend
npm install
npm run dev
```

**Backend:**
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## 🎨 Diseño

- **Color Primario:** Azul Marino (#1e3a5f, #0f172a)
- **Color Secundario:** Blanco (#ffffff)
- **Acentos:** Azul Claro, Verde (éxito), Rojo (error)

## 📋 Funcionalidades

### Empleados
- ✅ Registro de empleados
- ✅ Generación QR
- ✅ Captura facial
- ✅ Roles y permisos

### Asistencia
- ✅ Registro de entrada/salida
- ✅ Validación QR
- ✅ Reconocimiento facial
- ✅ Historial en tiempo real

### Dashboard
- ✅ Estadísticas
- ✅ Reportes
- ✅ Gráficos
- ✅ Tiempo real

## 🔒 Seguridad

- JWT Authentication
- Roles y permisos
- CORS protegido
- Redis cache
- Auditoría de eventos

## 📝 Licencia

Propietario - ECCOBIONICS
