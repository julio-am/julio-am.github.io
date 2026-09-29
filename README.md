# Personal website

An [al-folio](https://github.com/alshedivat/al-folio) / Jekyll site hosted at **https://julio-am.github.io**.

Based on al-folio **v1.2**, with its versioned theme and feature gems pinned in `Gemfile.lock`.

## Add your details

| Content                                | Edit                                                                         |
| -------------------------------------- | ---------------------------------------------------------------------------- |
| Name, site description, settings       | `_config.yml`                                                                |
| Biography, subtitle, homepage sections | `_pages/about.md`                                                            |
| Portrait                               | Add an image to `assets/img/`, then set `profile.image` in `_pages/about.md` |
| Social and contact links               | `_data/socials.yml`                                                          |
| CV, including the generated PDF        | `_data/cv.yml`                                                               |
| Publications and selected works        | `_bibliography/papers.bib`                                                   |
| News                                   | `_news/`                                                                     |
| Projects                               | `_projects/`                                                                 |
| Blog posts                             | `_posts/`                                                                    |
| Colors, fonts, spacing                 | `_sass/_personal.scss`                                                       |

The [customization guide](docs/CUSTOMIZE.md) explains how to replace each type of content and enable optional features.

## GitHub Pages

1. In this repository, open **Settings → Pages**.
2. Under **Build and deployment**, select **GitHub Actions** as the source.
3. A push to `main` runs **Build and deploy al-folio**. You can also run it from the Actions tab.

The workflow checks formatting, generates the CV PDF, builds Jekyll, checks the generated pages and local links, and deploys to GitHub Pages. Pull requests run the build and checks without deploying.

The site uses `url: https://julio-am.github.io` and an empty `baseurl`. No purchased domain, `CNAME`, paid service, or secret is required for this public repository. Do not use GitHub's built-in Jekyll branch build: the al-folio plugins need the included Actions workflow.

## Run locally

Install Ruby **3.3.9**, Bundler **4.0.6**, Node **22**, and Python **3.12**.

```sh
gem install bundler -v 4.0.6
bundle install
npm ci
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
python3 scripts/render_cv.py
bundle exec jekyll serve --livereload
```

Open the address printed by Jekyll. Changes to `_config.yml` require restarting the server. Re-run the RenderCV command after changing CV data to refresh the PDF.

For a static preview after building, `npm run dev` serves `_site` on port 4173.

## Verify changes

```sh
npm run lint:prettier
python3 scripts/render_cv.py
JEKYLL_ENV=production bundle exec jekyll build
python3 scripts/check_site.py
bundle exec al-folio upgrade audit --no-fail
```

Run `npm run format` to format content and templates.

## Features and maintenance

Native al-folio CV rendering, BibTeX publications, abstract/BibTeX controls, publication filtering, search, dark mode, Markdown posts, archives, RSS, projects, math, charts, and notebook support remain available. Optional external integrations require your own configuration; analytics, comments, newsletters, remote post imports, and citation metrics are not configured with sample accounts.

The compact presentation uses three intentional theme overrides: `_layouts/about.liquid`, `_includes/header.liquid`, and `assets/css/main.scss`. The header retains upstream navigation and adds a small accessibility enhancement script. The stylesheet retains all upstream imports and adds `_sass/_personal.scss`.

`.al-folio-overrides.yml` records the upstream versions of those files. After updating gems, run `bundle exec al-folio upgrade overrides audit`, review any changed upstream files, and only then acknowledge them with `bundle exec al-folio upgrade overrides accept --all`.

The upstream MIT license is retained in [LICENSE](LICENSE). The visual styling is inspired by Ben Shi's compact academic homepage; his content, portrait, and React code are not included.
