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

## Recipe Conventions

New recipes and edits to existing ones follow these rules. Older recipes
that predate them are not required to be converted unless asked.

### Quantities in grams

- Every ingredient is measured in grams. Convert cups, tablespoons,
  teaspoons, pounds and ounces to grams; do not leave volume measures in
  the ingredient list.
- Ingredients that come in natural units (eggs, an onion, garlic cloves, a
  bottle of passata, a can of beans) show the gram weight first and the
  natural count in parentheses, for example `100 grams eggs (2 eggs)` or
  `15 grams garlic (5 cloves), crushed`.
- Spell out `grams`; do not abbreviate to `g`.
- When the method refers back to an ingredient that appears more than once
  (salt for the dough and salt for the filling), repeat the gram amount in
  the step so the reader does not have to cross-reference.
- If a source recipe leaves a quantity unstated, pick a sensible value,
  and say in the Notes section that it was assumed.

### Temperatures in Fahrenheit

- Oven temperatures are given in Fahrenheit, written with the degree sign:
  `350°F`. A Celsius equivalent may follow in parentheses, `350°F (180°C)`,
  but Fahrenheit comes first and is never omitted.
- Never give a temperature in Celsius alone.

### Stove top: induction dial temperatures

The stove is an induction cooktop whose dial is set in Fahrenheit. Stove-top
steps give a dial setting rather than only "medium" or "low". Typical
settings:

- Boil / high: `400°F`
- Medium (sauté, browning): `350°F`
- Medium-low: `300°F`
- Rice or beans after coming to a boil: `250°F`
- Simmer: `200-225°F`; start at `225°F` for a covered or lid-ajar pot and
  adjust from there.

The dial reads the pan bottom, not the liquid, so pair the setting with a
visual cue and tell the reader how to adjust: "small bubbles steadily
breaking the surface; if bubbling stops nudge up to 250°F, if it boils
hard drop to 200°F". A word like "medium heat" may accompany the number
but does not replace it.

## Building Locally

Use nox to build the documentation locally: `nox -s docs`.

Nox is the ONLY supported way to build the docs. Never improvise around a
missing nox (e.g. by invoking sphinx-build directly or hand-rolling a
virtualenv). If nox is not installed, install it first (`pip install nox` —
add the `[pbs]` extra if the pinned Python interpreter is not available on
the system), then run the build through nox.
