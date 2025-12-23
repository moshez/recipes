# Repository Structure

This is a recipe collection using Sphinx documentation to generate a website hosted on ReadTheDocs.

## Directory Layout

- `doc/` - All recipe files in reStructuredText (.rst) format
  - `index.rst` - Main index page linking to all recipes
  - `conf.py` - Sphinx configuration
  - `jewish-holidays/` - Recipes specific to Jewish holidays (Passover, Rosh Hashanah, etc.)
- `.readthedocs.yaml` - ReadTheDocs build configuration
- `requirements.txt` / `requirements.in` - Python dependencies for building docs
- `noxfile.py` - Nox automation for local development

## Recipe Format

Recipes are written in reStructuredText with the following structure:
- Title with underline
- Ingredients section
- Method section
- Optional Notes section

## Building Locally

Use nox to build the documentation locally.
