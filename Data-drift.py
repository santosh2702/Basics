Train model on Dataset A (past data)
Deploy model
Start receiving live data (Dataset B)
Compare distribution of A vs. B:
    If same → model stable
    If different:
        - User behavior changed
        - External event occurred
        - Policy/business updated
        - Data collection pipeline changed
        - Demographic/domain shifted
        - Sampling bias revealed
    → Data Drift detected

Start ML experiment
Train model with parameters
Log:
    - Parameters (learning_rate, epochs, etc.)
    - Metrics (accuracy, F1 score, etc.)
    - Artifacts (plots, confusion matrix, etc.)
    - Model itself
Store everything in MLflow Tracking server
Optionally:
    Register best model in Model Registry
    Deploy model to Production
