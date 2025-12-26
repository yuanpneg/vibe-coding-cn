```markdown
# Strong Precondition Constraints

> According to your free combination

---

### General Development Constraints

1.  Do not adopt patch-style modifications that only solve local problems while ignoring overall design and global optimization.
2.  Do not introduce too many intermediate states for inter-communication, as this can reduce readability and form circular dependencies.
3.  Do not write excessive defensive code for transitional scenarios, as this may obscure the main logic and increase maintenance costs.
4.  Do not only pursue functional completion while neglecting architectural design.
5.  Necessary comments must not be omitted; code must be understandable to others and future maintainers.
6.  Do not write hard-to-read code; it must maintain a simple and clear structure and add explanatory comments.
7.  Do not violate SOLID and DRY principles; responsibilities must be single and logical duplication avoided.
8.  Do not maintain complex intermediate states; only the minimal necessary core data should be retained.
9.  Do not rely on external or temporary intermediate states to drive UI; all UI states must be derived from core data.
10. Do not change state implicitly or indirectly; state changes should directly update data and be re-calculated by the framework.
11. Do not write excessive defensive code; problems should be solved through clear data constraints and boundary design.
12. Do not retain unused variables and functions.
13. Do not elevate or centralize state to unnecessary levels; state should be managed closest to its use.
14. Do not directly depend on specific implementation details or hardcode external services in business code.
15. Do not mix IO, network, database, and other side effects into core business logic.
16. Do not form implicit dependencies, such as relying on call order, global initialization, or side-effect timing.
17. Do not swallow exceptions or use empty catch blocks to mask errors.
18. Do not use exceptions as part of normal control flow.
19. Do not return semantically unclear or mixed error results (e.g., null / undefined / false).
20. Do not maintain the same factual data in multiple locations simultaneously.
21. Do not cache state without defined lifecycle and invalidation policies.
22. Do not share mutable state across requests unless explicitly designed to be concurrency-safe.
23. Do not use vague or misleading naming.
24. Do not let a single function or module bear multiple unrelated semantics.
25. Do not introduce unnecessary temporal coupling or implicit temporal assumptions.
26. Do not introduce uncontrollable complexity or implicit state machines in the critical path.
27. Do not guess interface behavior; documentation, definitions, or source code must be consulted first.
28. Do not implement directly when requirements, boundaries, or input/output are unclear.
29. Do not implement business logic based on assumptions; requirements must be confirmed with humans and recorded.
30. Do not add new interfaces or modules without evaluating existing implementations.
31. Do not skip the verification process; test cases must be written and executed.
32. Do not touch architectural red lines or bypass existing design specifications.
33. Do not pretend to understand requirements or technical details; if unclear, it must be explicitly stated.
34. Do not modify code directly without contextual understanding; changes must be carefully refactored based on the overall structure.

---

### Glue Development Constraints

1.  Do not implement low-level or common logic yourself; existing mature repositories and production-grade libraries must be prioritized, directly, and completely reused.
2.  Do not copy dependency library code into the current project for modification and use.
3.  Do not perform any form of functional裁剪 (clipping), logic rewriting, or downgrade encapsulation on dependency libraries.
4.  Direct local source code connection or package manager installation methods are allowed, but what is actually loaded must be a complete production-grade implementation.
5.  Do not use simplified, alternative, or rewritten dependency versions pretending to be the real library implementation.
6.  All dependency paths must genuinely exist and point to complete repository source code.
7.  Do not load non-target implementations through path shadowing, re-named modules, or implicit fallback.
8.  Code must directly import complete dependency modules; no subset encapsulation or secondary abstraction is allowed.
9.  Do not implement similar functions already provided by the dependency library in the current project.
10. All invoked capabilities must come from the real implementation of the dependency library; Mock, Stub, or Demo code must not be used.
11. There must be no placeholder implementations, empty logic, or "write interface first, then implement" situations.
12. The current project is only allowed to undertake business process orchestration, module combination scheduling, parameter configuration, and input/output adaptation responsibilities.
13. Do not re-implement algorithms, data structures, or complex core logic in the current project.
14. Do not extract complex logic from dependency libraries and implement it yourself.
15. All imported modules must genuinely participate in execution during runtime.
16. There must be no "import but not use" pseudo-integration behavior.
17. It must be ensured that `sys.path` or dependency injection chains load the target production-grade local library.
18. Do not load clipped, test, or simplified implementations due to incorrect path configuration.
19. When generating code, it must be clearly marked which functions come from external dependencies.
20. Under no circumstances should dependency library internal implementation code be generated or supplemented.
21. Only the minimal necessary glue code and business layer scheduling logic are allowed to be generated.
22. Dependency libraries must be assumed to be authoritative and unchangeable black box implementations.
23. The project evaluation standard is solely based on whether it correctly and completely builds upon mature systems, rather than the amount of code.

---

### Systematic Code and Functional Integrity Check Constraints

24. No form of functional weakening, clipping, or alternative implementation is allowed to pass audit.
25. It must be confirmed that all functional modules are complete production-grade implementations.
26. There must be no amputated logic, Mock, Stub, or Demo-level alternative code.
27. Behavior must be consistent with the mature production version.
28. It must be verified whether the current project 100% reuses existing mature code.
29. There must be no form of re-implementation or functional folding.
30. It must be confirmed that the current project is a direct integration rather than a copy-and-modify.
31. All local library import paths must be checked to be real, complete, and effective.
32. It must be confirmed that the `datas` module is a complete data module, not a subset.
33. It must be confirmed that `sizi.summarys` is a complete algorithm implementation and not downgraded.
34. Parameter simplification, logic skipping, or implicit behavior changes are not allowed.
35. It must be confirmed that all imported modules genuinely participate in execution during runtime.
36. There must be no interface empty implementations or "import but not call" pseudo-integration.
37. Path shadowing and misleading loading of re-named modules must be checked and excluded.
38. All audit conclusions must be based on verifiable code and path analysis.
39. No vague judgments or conclusions based on subjective speculation should be output.
40. The audit output must clearly state conclusions, itemized judgments, and risk consequences.
```
