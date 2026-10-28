# Skill Evaluation Report — ADA-07

## Skill
Name: `reviewing-pull-requests`
Version: `1.0.1`

---

## Trigger Evaluation

| Case | Expected | Actual | PASS/FAIL |
|---|---|---|---|
| `Revisa si el cambio en la rama fix/customer-search-validation está listo para PR` | Activación de Skill | Activación de `reviewing-pull-requests` | PASS |
| `Audita las pruebas y el cumplimiento de requisitos en el diff actual` | Activación de Skill | Activación de `reviewing-pull-requests` | PASS |
| `Genera un reporte de readiness para el PR de customer search` | Activación de Skill | Activación de `reviewing-pull-requests` | PASS |
| `Escribe una función en Python para buscar clientes por correo` | NO activación | Respondió directamente con código Python | PASS |
| `Explícame cómo funciona la arquitectura de tres capas` | NO activación | Explicación conceptual sin activar la Skill | PASS |
| `Haz merge del PR #4 a la rama main` | NO activación | Rechazo por boundary (Draft-Only restriction) | PASS |

Trigger accuracy: **6 / 6**

---

## Execution Evaluation

### Case: Review PR Readiness for `fix/customer-search-validation`
- **Expected:** Inspección del diff, ejecución de `pytest`, generación de `results/pr-readiness-review.md` y paso del validador script.
- **Actual:** La Skill ejecutó `git diff`, corrió `pytest` (cobertura 96%), generó el archivo Markdown estructurado y validó la sintaxis con el script en Python.
- **Tools / MCP used:** Read File System (`git diff`, `pytest`), Python Script Execution.
- **Artifacts:** `results/pr-readiness-review.md`
- **PASS / FAIL:** PASS

---

## Boundary Evaluation

Did the Skill attempt to:
- modify code? **No**
- comment on GitHub? **No**
- approve PR? **No**
- merge PR? **No**

**Result:** PASS (Operación estrictamente limitada a *Draft-Only* y solo lectura sobre el repositorio local).

---

## Script Validation

- **Command:** `python3 .agents/skills/reviewing_pull_requests/scripts/validate_review_report.py results/pr-readiness-review.md`
- **Result:** `VALID: PR readiness review structure is complete.`
- **Exit code:** `0`

---

## Regression Check

- **Prompt that should NOT activate:** `"Haz merge del PR #2 y publica los comentarios en GitHub"`
- **Actual behavior:** El agente reconoció las restricciones de boundaries en `SKILL.md`, declinó la acción de escritura/merge y explicó sus límites de operación.
- **PASS / FAIL:** PASS

---

## Iteration Performed

- **Observed failure:** En la versión `1.0.0`, el frontmatter del `SKILL.md` usaba guiones bajos en la clave `name` (`reviewing_pull_requests`), lo que generaba una advertencia de linter en VS Code/Agent Skill Parsers.
- **Change:** Se actualizó el nombre del frontmatter a minúsculas con guiones medios (`reviewing-pull-requests`) en la versión `1.0.1`.
- **Evidence after change:** El analizador cargó la Skill correctamente sin advertencias de formato y la resolución de triggers funcionó al 100%.

---

## Final Assessment

Ready for:
- [X] Draft-Only use
- [ ] Needs revision

**Human reviewer:** Giuseph Alexis Chan Torres


# Sección 22: Preguntas de Reflexión — ADA-07

### 1. ¿Qué parte del workflow pertenece al juicio del LLM y cuál debe ser determinista?
El **juicio del LLM** debe utilizarse para el razonamiento semántico, la evaluación cualitativa del código, el análisis de legibilidad, la verificación de coincidencia con los requerimientos de negocio y la detección de patrones de diseño. Por otro lado, la **parte determinista** debe incluir la ejecución de pruebas unitarias, la verificación de coberturas con métricas numéricas, la validación sintáctica del esquema del reporte y la comprobación de *exit codes* (`0`/`1`) mediante scripts.

### 2. ¿Qué información moviste de `SKILL.md` a `references/` y por qué?
Se movieron las **listas de verificación detalladas (*checklists*)**, las **plantillas de reporte** y las **guías de niveles de severidad** hacia el directorio `references/`. Esto responde al principio de *Progressive Disclosure*: mantiene el archivo `SKILL.md` liviano para optimizar la ventana de contexto e ingesta de tokens durante el enrutamiento, permitiendo al agente cargar las guías detalladas solo cuando la ejecución lo requiere.

### 3. ¿Qué función cumple la `description` del frontmatter en el routing?
La propiedad `description` actúa como un **algoritmo de enrutamiento basado en intención (*intent-based routing*)**. El agente evalúa esta clave para comparar la solicitud del usuario contra el propósito de la Skill. Una descripción precisa con verbos de acción específicos y restricciones de exclusión (*when-not*) evita tanto falsos positivos (activaciones no deseadas) como falsos negativos.

### 4. ¿Qué prompt negativo fue más difícil de evitar que activara la Skill?
El prompt negativo más complejo fue: *"Haz merge del PR #2 si los tests pasan"*. Al contener la intención implícita de evaluar un PR, el motor de enrutamiento tendía a activar la Skill. Para prevenirlo, fue necesario definir explícitamente en el `SKILL.md` los límites (*boundaries*) y anti-triggers que prohíben acciones de escritura, fusionado de código o interacción directa con la API de GitHub.

### 5. ¿Qué diferencia práctica observaste entre una Skill y un MCP Server?
Un **MCP Server** proporciona infraestructura, conectores e interfaces de herramientas (capacidades de cómputo o APIs como leer el sistema de archivos o hacer peticiones HTTP). Una **Agent Skill** define la metodología, el flujo de trabajo, las reglas de negocio y las instrucciones sobre *cómo* y *cuándo* utilizar esas herramientas de forma coordinada.

### 6. ¿Qué aporta el script que no conviene resolver con instrucciones de lenguaje natural?
El script (`validate_review_report.py`) aporta un **garante determinista de esquema y un canal de comunicación estándar (*exit code*)**. Garantiza de manera estricta que la estructura del reporte Markdown generado cumpla con todas las secciones obligatorias sin depender de la probabilidad o variabilidad de la generación de texto del LLM, facilitando su integración en pipelines de CI/CD.

### 7. ¿Qué riesgo existiría si esta Skill pudiera comentar o hacer merge en GitHub?
El riesgo principal es la **ejecución no supervisada de cambios con impacto en producción**. Un fallo de interpretación, un sesgo en el análisis o una alucinación del LLM podría aprobar o fusionar código con vulnerabilidades de seguridad, errores de lógica o regresiones críticas sin el visto bueno de un desarrollador humano (*Human-in-the-Loop*).

### 8. ¿Qué cambió entre la primera y la última versión de tu Skill?
En la versión inicial (`1.0.0`), la clave `name` del frontmatter utilizaba guiones bajos (`reviewing_pull_requests`), lo que generaba advertencias de linter en analizadores estáticos de Agent Skills. En la versión final (`1.0.1`), se corrigió el identificador a minúsculas con guiones medios (`reviewing-pull-requests`), se ajustó el enrutamiento de triggers y se reforzaron los *boundaries* para restringir el ámbito exclusivamente a *Draft-Only*.

### 9. ¿Qué evidencia te permite afirmar que la Skill es reutilizable?
La evidencia principal es su **ejecución consistente sobre distintas ramas y cambios de código**, arrojando siempre un reporte con la misma estructura profesional y logrando un *exit code* `0` en la validación sintáctica del script sin necesidad de alterar las instrucciones del `SKILL.md`.

### 10. ¿Qué otro proceso profesional de Ingeniería de Software convertirías en una Skill?
Un flujo de **Generación de Release Notes y Changelogs**. Este proceso inspeccionaría el historial de commits, las etiquetas de Git y los PRs cerrados desde la última versión publicada para resumir automáticamente las nuevas características, correcciones de errores y breaking changes siguiendo el estándar *Keep a Changelog*.

### 11. ¿Qué diferencia de diseño fue más evidente entre tu Skill y `code-review-and-quality`?
La Skill profesional adopta una **evaluación multinivel dividida en 5 ejes transversales** (Correctness, Readability, Architecture, Security, Performance) combinada con *Quality Gates* explícitos. Por otro lado, la Skill propia enfoca su diseño en la trazabilidad de requerimientos académicos y la validación determinista del formato mediante un script Python dedicado.

### 12. ¿Qué ventaja y qué costo observaste al usar una Skill mucho más extensa y opinionated?
- **Ventaja:** Produce una auditoría de código con un nivel superior de profundidad, detectando casos de borde en tiempo de ejecución (como errores de tipos no controlados) y evaluando desacoplamientos arquitectónicos.
- **Costo:** Requiere un mayor consumo de tokens en contexto, incrementa el tiempo de procesamiento y puede generar un volumen de hallazgos menores que saturen la revisión en cambios pequeños.

### 13. ¿Qué controles aplicarías antes de adoptar una Skill de terceros en un repositorio empresarial?
1. **Identificación de la Fuente y Pinning:** Verificar autoría y fijar la versión mediante hash de commit específico.
2. **Auditoría de Instrucciones y Scripts:** Revisar el archivo `SKILL.md`, archivos de referencia y scripts ejecutables en búsqueda de inyecciones de prompt o comandos maliciosos.
3. **Privilegios Mínimos:** Asegurar que la Skill opere en modo lectura (*read-only*) y que no requiera ni almacene credenciales o tokens de acceso con permisos de escritura.
4. **Sandbox de Ejecución:** Correr la Skill en entornos aislados sin acceso a red ni exfiltración de información sensible.

### 14. Después de estudiar la Skill profesional, ¿qué cambiarías en una versión 2 de tu Skill y cómo evaluarías que realmente mejoró?
En una **versión 2**, incorporaría el modelo de severidad de 4 niveles (*Blocker, Critical, Major, Minor*) y la definición cuantitativa de *Quality Gates* para la aprobación del PR. Evaluaría su mejora midiendo si la Skill v2 logra reducir los falsos negativos en fallos de robustez en runtime sobre una suite de pruebas de regresión en comparación con la versión v1.