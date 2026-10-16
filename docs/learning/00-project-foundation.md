# 00 — Fundamentos del proyecto

## Objetivo

Antes de integrar un LLM necesitamos una aplicación que podamos cambiar sin
perder control. Este hito crea el esqueleto sobre el cual mediremos cada avance.

## Por qué usamos `src/`

El paquete vive en `src/document_support` y no en la raíz. Esto evita que Python
importe accidentalmente el código del directorio actual aunque el paquete no se
haya instalado. Una prueba exitosa confirma así que el empaquetado funciona.

## Fábrica de aplicación

`create_app()` construye FastAPI explícitamente. Más adelante podremos crear una
aplicación de prueba con dependencias sustituidas, sin conectarnos a PostgreSQL,
Redis o un proveedor de LLM real durante cada prueba.

## Configuración mediante entorno

Los valores operativos no se escriben directamente en el código. `Settings`
lee variables con prefijo `APP_` y permite validar sus tipos. `.env.example`
documenta nombres seguros, mientras `.env` permanece ignorado porque puede
contener secretos.

## Liveness no es readiness

`GET /api/v1/health` es una señal de **liveness**: confirma que el proceso HTTP
responde. No comprueba todavía la base de datos ni otros servicios. Una futura
señal de **readiness** responderá si la instancia está preparada para recibir
tráfico. Mezclar ambas puede provocar reinicios innecesarios durante una caída
temporal de una dependencia.

## Las cuatro barreras de calidad

1. Ruff detecta errores simples y mantiene un estilo consistente.
2. El formateador elimina discusiones manuales sobre formato.
3. Mypy verifica contratos de tipos antes de ejecutar el programa.
4. Pytest verifica el comportamiento observable de la API.

CI repite estas verificaciones con varias versiones de Python. La meta no es
tener una insignia verde: es encontrar diferencias antes de integrar código.

## Preguntas de entrevista relacionadas

- ¿Qué diferencia existe entre liveness y readiness?
- ¿Por qué usar una fábrica de aplicación?
- ¿Qué información pertenece en variables de entorno?
- ¿Qué detecta un type checker que una prueba podría no detectar?
- ¿Cuándo separarías el monolito en servicios independientes?
