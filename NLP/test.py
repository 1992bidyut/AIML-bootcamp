import sys

try:
    import torch
except ImportError as exc:
    raise RuntimeError(
        "torch is not installed in this environment. Install it with `pip install torch` "
        "or activate the correct virtual environment."
    ) from exc

try:
    import transformers
    from transformers import pipeline
except ImportError as exc:
    raise RuntimeError(
        "transformers is not installed in this environment. Install it with `pip install transformers` "
        "or activate the correct virtual environment."
    ) from exc

if tuple(map(int, torch.__version__.split('.')[:2])) < (2, 4):
    raise RuntimeError(
        f"Detected torch {torch.__version__}, which is too old for the installed transformers "
        f"version {transformers.__version__}. Upgrade torch to >=2.4 or install a compatible "
        "transformers version."
    )

sentiment_pipeline = pipeline("sentiment-analysis")