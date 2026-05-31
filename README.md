# ai_boot_camp
 
* spacy model download under virtual environment
> python -m spacy download en_core_web_sm

* Proper compatible torch and transformer pip version install command.
> pip install "transformers[torch]"

If you faces any issue to load specific model then downgrade the transformer
> pip install "transformers<4.44.0"