## Computational Perks

- **Low Overhead Execution**
  - Direct C-level execution using compiled code, avoiding Python interpreter overhead.

- **Faster for Small Feature Spaces**
  - Ideal when the number of features is low (e.g., 2–10); avoids the heavy abstractions of libraries like NumPy or Scikit-learn.

- **Tight Memory Control**
  - Manual control over memory layout using typed memoryviews reduces unnecessary allocations and copying.

- **No External Dependencies**
  - Runs without relying on large numerical libraries, keeping the compiled binary lean.

- **Deterministic Execution**
  - Without background threading or parallelism overhead (unless added manually), the timing is highly stable and predictable.

- **Custom Optimization Potential**
  - You can tailor linear algebra operations (e.g., use unrolled loops or fixed-size 2x2 matrix inversion) for specific tasks or hardware.

- **Lower Startup Time**
  - Doesn't import large Python modules, reducing cold-start latency in repeated small-batch runs (e.g., in embedded systems or microservices).
