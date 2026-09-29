# Populate your site

## Identity and biography

Set `first_name`, `middle_name`, and `last_name` in `_config.yml`. Keep `title: blank` to use your name as the site title. Add your own `description` and optional `keywords`.

Edit the prose and `subtitle` in `_pages/about.md`. Add a portrait at `assets/img/portrait.jpg` and set `profile.image: portrait.jpg`. With no image, the homepage shows the intentional photo placeholder.

Remove the `selected_note` line from `_pages/about.md` when the publication placeholders have been replaced. You can turn homepage sections off with `selected_papers: false`, `announcements.enabled: false`, or `latest_posts.enabled: false`.

Add real contact details to `_data/socials.yml`. Leave unused fields absent or commented out so that no dummy links are published. A `contact_note` in `_config.yml` adds a short contact paragraph to the homepage.

## CV: one source, two outputs

Edit `_data/cv.yml`. The `cv:` object supplies the native al-folio web CV and RenderCV's PDF generator. The workflow renders the PDF at `assets/pdf/cv.pdf` before the site build. The generated PDF is ignored by Git and published as part of the Pages artifact.

Use RenderCV-compatible entries and keep the section names `Education`, `Experience`, and `Projects` for their rich al-folio renderers. This starter uses `Technical skills` and `Research interests` with `label` / `details` entries, which both renderers understand. Generic sections can also contain `bullet` entries.

Replace `date: Dates to add` with real `start_date` and `end_date` fields, or a single real `date`. For a current role, use `end_date: present`. Avoid keeping both a date range and the placeholder date.

```yaml
Education:
  - institution: Your university
    area: Your field
    degree: Your degree
    start_date: 2020-09
    end_date: 2024-06
    highlights:
      - Your actual thesis topic or relevant achievement.
```

The dates above are examples of syntax, not personal data. The formatting options live in `assets/rendercv/design.yaml`, `locale.yaml`, and `settings.yaml`.

To use JSONResume instead, supply `assets/json/resume.json`, configure `jekyll_get_json` in `_config.yml`, and change `cv_format` to `jsonresume` in `_pages/cv.md`. The included PDF generator reads RenderCV YAML; it would need a conversion step if you switch the web CV to JSONResume.

## Publications

Replace the two placeholder records in `_bibliography/papers.bib` with your real BibTeX entries. Keep the opening two `---` lines. Set `selected = {true}` for records that should also appear on the homepage.

Supported fields include `abstract`, `bibtex_show`, `doi`, `arxiv`, `pdf`, `code`, `slides`, `poster`, `blog`, and `website`. Only add a link field when you have a real destination. Relative PDFs belong in `assets/pdf/`; for example, `pdf = {paper.pdf}`.

Update `scholar.first_name` and `scholar.last_name` in `_config.yml` so your author name is highlighted. Optional coauthor and venue metadata belong in `_data/coauthors.yml` and `_data/venues.yml`.

## News, projects, and writing

- News: add a Markdown file in `_news/` with a `date`, `title`, and `inline: true` for a short homepage announcement.
- Projects: copy a file from `_projects/`, change its title and description, and write the project body. `importance` controls order. The starter index uses a text list; the native al-folio project card includes are still available.
- Posts: create `_posts/YYYY-MM-DD-short-title.md` with `layout: post`, `title`, `date`, and `description`. Posts appear in the blog, homepage writing list, search, RSS, and archives. Future-dated posts remain hidden until their date.

The sample post and projects can be edited directly or deleted. The corresponding lists update during the next build.

## Optional al-folio features

The pinned al-folio gems and their configuration remain in place. Consult the [al-folio customization guide](https://github.com/alshedivat/al-folio/blob/v1.2/docs/CUSTOMIZE.md) for the full feature set and page front matter.

| Feature                                    | How it is enabled                                                                           |
| ------------------------------------------ | ------------------------------------------------------------------------------------------- |
| Search                                     | `search_enabled: true` in `_config.yml`; works with the search button and keyboard shortcut |
| Theme switching                            | `enable_darkmode: true`; uses the native system/light/dark control                          |
| Math                                       | `enable_math: true` is set; use standard MathJax delimiters in Markdown                     |
| Charts, diagrams, notebooks, Distill posts | Their native plugins are installed; add the appropriate page front matter and content       |
| Notebook conversion                        | `nbconvert` is installed by the build workflow                                              |
| Responsive WebP conversion                 | Install ImageMagick locally and in the build workflow, then set `imagemagick.enabled: true` |
| Publication thumbnails                     | Set `enable_publication_thumbnails: true` and add real `preview` assets                     |
| Citation metrics                           | Configure real identifiers and enable the desired publication badge providers               |
| Comments, analytics, newsletter            | Add your real provider configuration before enabling them                                   |

Optional features have not all been exercised by the starter content. Their native implementation remains available; validate the specific feature when you add it.

## Appearance

Edit `_sass/_personal.scss` for the blue links, system font, compact navigation, news panel, publication pills, light/dark tokens, and mobile spacing. The main content area is approximately 800 pixels wide, with responsive side padding.

The rest of the theme comes from `al_folio_core`, and the CV renderer comes from `al_folio_cv`. Keeping the local overrides small helps with future upgrades. Do not replace the framework with a generated static HTML copy if you want to retain its content features.
