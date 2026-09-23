# npcooley.github.io (Quarto)

Personal site, built with [Quarto](https://quarto.org) and deployed to GitHub
Pages by GitHub Actions.

## Layout: what each file is for

| Path | Purpose |
| --- | --- |
| `_quarto.yml` | Site-wide config: navbar, footer, theme, **and the explicit list of pages to render**. |
| `index.qmd` | Home page. Uses Quarto's `about:` template (photo, links, bio). |
| `projects.qmd` | A *listing page*: automatically builds a card list from the project files below. |
| `projects/*.qmd` | One file per project. Each file's `title`, `description`, `categories` feed the listing. |
| `publications.qmd` | Plain hand-written page. |
| `styles.css` | Your CSS overrides (currently empty). |
| `images/`, `files/` | Static assets. Anything you link to from a page is copied into the output. |
| `tools/strip_exif.py` | Removes GPS/camera metadata from photos before you publish them. |
| `.github/workflows/publish.yml` | Build-and-deploy automation. |

Generated, never edited, never committed: `_site/` (the built site) and `.quarto/`.

## Day-to-day workflow

```bash
quarto preview     # live-reloading local server; edit a .qmd, browser updates
quarto render      # full build into _site/ (what CI runs)
```

Developed and tested with Quarto 1.10.18 (`quarto --version`). Nothing else is needed while the
pages contain no R/Python code cells.

## Adding a page

1. Create `newpage.qmd` with a `title:` in its front matter.
2. **Add it to the `render:` list in `_quarto.yml`.** (If a page is missing from
   the built site, this is almost always why.)
3. Optionally add it to `navbar:` in `_quarto.yml`.

## Adding a project

Copy `projects/synextend.qmd`, edit it, then add the new file to **both** the
`render:` list in `_quarto.yml` and the `contents:` list in `projects.qmd`.

## Deploying

One-time: repo **Settings -> Pages -> Source: GitHub Actions**.
After that, every push to `master` triggers `publish.yml`. Watch progress in the
repo's **Actions** tab.

## Photos: strip location data first

Phone photos embed GPS coordinates. Before adding any photo:

```bash
pip install pillow
python3 tools/strip_exif.py original.jpg images/clean.jpg
```

## Adding executable code later (R / Python)

Code cells will make CI fail until the workflow installs R or Python
(`r-lib/actions/setup-r`, `actions/setup-python`) and any packages. Alternatively,
render locally with `execute: freeze: auto` and commit the `_freeze/` directory
so CI never has to execute code.
