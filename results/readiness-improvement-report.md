# Readiness Improvement Report

## Analysis of Impact
The transition from a standard repository to an Agent-Ready repository demonstrated a clear shift from implicit tribal knowledge to explicit, verifiable contracts. 

In the BEFORE state, the repository was functionally complete but relied heavily on the developer's (or agent's) intuition regarding environment configuration (e.g., virtual environments) and testing commands. The agent experienced measurable friction when attempting to execute standard validation commands, leading to failed terminal executions.

By implementing the Agent-Ready enhancements, we achieved the following critical shifts:

1. **Context & Discoverability:** The introduction of `GEMINI.md` as an adapter and `docs/REPO_MAP.md` eliminated the need for the agent to scan the entire source tree to understand the architecture. It mapped directly to the CLI, Service, and Repository layers.
2. **Executable Knowledge:** Replacing natural language instructions like "run pytest" with a deterministic script (`scripts/verify_repo.sh`) completely removed environment friction. The agent no longer needed to guess how to activate the virtual environment or handle dependencies.
3. **Guardrails & Automation:** Introducing `check_repo_contract.py` and git hooks transformed "requests" into strict "rules". The agent is now physically blocked from completing a task if it breaks the repository structure or fails tests, shifting the burden of verification from human review to automated systems.

## Human-Agent Symmetry
These improvements do not solely benefit AI agents. A new human developer joining the project would experience the exact same reduction in friction. They would not need to ask senior engineers how to run the test suite or where the validation logic resides; the entry points are discoverable, and the execution is completely standardized. An agent-ready repository is, fundamentally, a developer-ready repository.


# Reflexión Individual - ADA-08

**1. ¿Cuál fue el principal obstáculo para el agente en la ejecución BEFORE?**
El manejo del entorno de ejecución. El agente intentó utilizar el comando global `pytest` y falló, obligándolo a deducir por ensayo y error que debía invocar directamente el binario dentro de `.venv/bin/`.

**2. ¿Qué información tuvo que inferir el agente que un desarrollador experimentado ya conocía?**
Que los tests de cobertura requerían parámetros específicos (`--cov=src`) y que cualquier script CLI de Python en este proyecto requería la activación previa del entorno virtual.

**3. ¿Qué mejora produjo el mayor impacto y por qué?**
La creación de `scripts/verify_repo.sh`. Convirtió conocimiento tribal operativo en un solo comando determinista, eliminando por completo la posibilidad de que el agente ejecute mal una validación, olvide activar el entorno virtual o se salte el chequeo de cobertura.

**4. ¿Qué información pertenece en AGENTS.md y qué información NO debería vivir ahí?**
- **SÍ pertenece:** Las referencias a dónde encontrar las fuentes de verdad, comandos estándar de ejecución, *Definition of Done* y condiciones de parada (stop conditions).
- **NO pertenece:** Lógica de negocio, detalles de implementación de la arquitectura, o duplicación de requisitos (para evitar desincronización).

**5. ¿Qué regla convertiste en software/hook/script en lugar de dejarla como instrucción?**
La regla de "Asegúrate de que la estructura del repositorio no sea alterada y que los tests pasen" se convirtió en `scripts/check_repo_contract.py` ejecutado dentro de un hook de `pre-commit`, bloqueando físicamente acciones destructivas antes de registrar un commit.

**6. ¿Qué diferencia observaste entre 'más contexto' y 'mejor contexto'?**
"Más contexto" habría sido pegar todo el código y la arquitectura en un megapront. "Mejor contexto" fue crear `docs/REPO_MAP.md`, un índice ligero que le indicó al agente exactamente qué archivo (`src/service.py`) tocar sin tener que procesar o leer inútilmente todo el repositorio.

**7. ¿Qué riesgo aparece cuando CLAUDE.md/GEMINI.md/copilot instructions duplican información del proyecto?**
El riesgo de desincronización (drift). Si `GEMINI.md` reescribe una regla de negocio y luego los requisitos reales (`SPEC.md`) cambian, el agente seguirá las instrucciones de la herramienta y romperá la lógica del dominio, creando una segunda (y falsa) fuente de verdad.

**8. ¿Qué checks comparten ahora el agente, el desarrollador humano y CI?**
Los tres actores ejecutan exactamente el mismo contrato: el script `./scripts/verify_repo.sh` (que unifica la configuración del entorno, las pruebas de pytest con coverage y el chequeo de integridad estructural del repositorio).

**9. ¿Qué parte del proceso sigue requiriendo decisión humana?**
La alteración de límites arquitectónicos o de dependencias, como decidir si cambiar la persistencia de datos (actualmente in-memory en `repository.py`) hacia una base de datos externa, o la resolución de conflictos entre requerimientos de negocio.

**10. ¿Qué evidencia demuestra que el AFTER es realmente mejor?**
El log de ejecución de Antigravity (Gemini), donde pasó de un estado de "ensayo y error" (comandos fallidos y reintentos) en el BEFORE, a una ejecución planificada, lineal y sin errores en el AFTER, donde utilizó el script de validación directamente sin fallos.

**11. ¿Qué mejora realizada para el agente también beneficia a un desarrollador que entra por primera vez al proyecto?**
La centralización de comandos operativos. Un desarrollador junior o un nuevo integrante ya no necesita memorizar banderas de *pytest* o rutas de entornos; simplemente ejecuta el script unificado de validación y sabe de inmediato si su cambio cumple con el Definition of Done.

**12. ¿Qué variable no controlada podría afectar tu comparación BEFORE/AFTER?**
La naturaleza estocástica del LLM y las posibles actualizaciones "silenciosas" del modelo Gemini Argon 4 Medium por parte de Google en el tiempo transcurrido entre la ejecución de la prueba BEFORE y la AFTER.

**13. ¿Qué elementos de este ADA conservarás como base para tu proyecto final?**
La mentalidad de "Guardrails as Code". Mantendré la separación estricta entre las reglas del proyecto (`AGENTS.md`) y las instrucciones adaptadoras de la herramienta específica (`GEMINI.md`), así como la implementación de *gates* automáticos en CI para prevenir que la IA degrade el código silenciosamente.