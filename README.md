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
| function | `family:<n>` | the numbered database: the permanent function number, catalogued when its line occurrences exceed 10 (distinct lines are reported beside it) |
| numbered line | `line:<n>` | the permanent line key; each function lists the first and last key of its line sequence, which are endpoints, not a numeric range |

Start at [CATALOGUE.md](CATALOGUE.md). Then read [APPS.md](APPS.md), [ELEMENTS.md](ELEMENTS.md), [SURFACES.md](SURFACES.md) and the functions by category in [functions/](functions/). The same data is in `catalogue/*.json`.

Titles and descriptions are the sources' own words. Where a source has none, the entry states what is measured and says the description is not yet written.

- Rebuild with `python build/build_catalogue.py`. Add `--register inputs/<file>` to rebuild from a committed register copy.

Check with `python tests/check_catalogue.py`. It recomputes every field of every entry independently from the pinned inputs, and fails on any missing, extra or changed entry. Before the real catalogue may pass, 20 deliberately broken copies must each fail. It does not prove that the sources are right, that descriptions are complete, or that a function runs. Inputs are pinned by sha256 in `catalogue/provenance.json`.
