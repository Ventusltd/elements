# elements
We have every line of code mapped now we need to map complete elements to stop a jumble of code galaxies
We need to be able to visualise how bodies of codes assemble that form functions, features, maps, engines, and we need to visualize them in action 
We need to ask how can this or that solve the next Grid Challenge? 
Be Upanishadic in questions, be Gita like in actions, be Mahabharata like in detailed implementation! 

## The catalogue

Every element, app and function with more than 10 lines of code has a unique key. Each key is one the estate already uses and never reuses. None is invented here.

| what | key | where it comes from |
|---|---|---|
| element | `block:<Sym>` | the live block register, one per block |
| app | `block:<Sym>` | register blocks whose kind is app |
| served surface | `surface:<url>` | the folders of the live addresses the register records |
| function | `family:<n>` | the numbered database: the permanent function number, catalogued when it holds more than 10 numbered lines |
| numbered line | `line:<n>` | the permanent line key; each function lists its first and last |

Start at [CATALOGUE.md](CATALOGUE.md). Then read [APPS.md](APPS.md), [ELEMENTS.md](ELEMENTS.md), [SURFACES.md](SURFACES.md) and the functions by category in [functions/](functions/). The same data is in `catalogue/*.json`.

Titles and descriptions are the sources' own words. Where a source has none, the entry states what is measured and says the description is not yet written.

- Rebuild with `python build/build_catalogue.py`.
- Check with `python tests/check_catalogue.py`. The check refuses a duplicated key, a function of 10 lines or fewer, and a line key the database does not hold. It is first shown failing on a broken copy.
- Inputs are pinned by sha256 in `catalogue/provenance.json`.
