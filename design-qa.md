# Design and feature QA

**Final result: passed**

The requested scope is a real al-folio site with placeholder personal content and a compact appearance inspired by Ben Shi's homepage. It is not a reproduction of his identity, writing, or complete React interaction model.

## Visual evidence

- Source: <https://benshi34.github.io/#/>.
- Source capture: `/workspace/scratch/48d5ddd73579/benshi34-reference/benshi34-01-home.jpg`.
- Final implementation: [light homepage](docs/qa/home-light.jpg), [dark homepage](docs/qa/home-dark.jpg), [mobile CV](docs/qa/cv-mobile.jpg), and [rendered PDF](docs/qa/cv-pdf.png).
- Browser preview: Jekyll's generated `_site`, served for browser inspection.
- Source and implementation homepage captures both measure **1348 × 926 pixels**. They were compared together without resampling. The browser reported a CSS viewport of **1363 × 936**; no device-scale override was available or applied. Exact comparison was based on the equally sized captured content regions rather than assuming a device pixel ratio.
- Full-view comparison: `/workspace/scratch/48d5ddd73579/home-comparison.jpg`.
- Focused profile, typography, and news comparison: `/workspace/scratch/48d5ddd73579/home-comparison-detail.jpg`.
- Mobile verification used a **390 × 844 CSS-pixel iframe viewport** in the same browser. Its document width and scroll width both measured **375 pixels**, with the remaining width occupied by the scrollbar. This checks responsive CSS and navigation; it is not physical-device emulation.
- States reviewed: light homepage, dark homepage, expanded publication abstract, CV, mobile menu, mobile CV, project detail, blog index, and post.

The reference and combined comparison images are session evidence and are not copied into this public repository; they contain Ben's portrait and content. Only this site's own screenshots are stored here.

## Findings and comparison history

1. The initial render had an unnecessarily narrow content area and extra top spacing from a native spacing utility. The content width was adjusted to approximately 800 pixels, and the spacing override was applied in the appropriate CSS layer. The final full-view and focused comparisons show aligned page proportions and a compact profile header.
2. The initial CV showed list markers above structured entries and an empty date column. The list styling was corrected and the sample dates explicitly labeled `Dates to add`. The final mobile CV has readable content without horizontal overflow.
3. The initial PDF wrapped the generic degree label awkwardly and did not apply the separate design file. The placeholder was shortened to `TBD`, and the PDF command now explicitly supplies the design and locale files. The final PDF is one A4 page with clean alignment and no clipping.
4. Publication toggles were made keyboard reachable, with expanded state and closed-panel accessibility state synchronized to the native al-folio behavior. The final expanded abstract rendered visibly; Enter and mouse activation were checked.

The final full-view and focused visual comparison found no remaining actionable P0/P1/P2 differences within the agreed scope.

## Required visual surfaces

| Surface            | Assessment                                                                                                                                                                                                 |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Typography         | System sans-serif, 16px body text, compact 24px profile title, and semibold publication titles closely follow the reference hierarchy.                                                                     |
| Spacing and layout | Approximately 800px content column, thin navigation rule, 80px portrait area, restrained section gaps, flat news panel, and separated publication rows. Fewer news items intentionally shorten that panel. |
| Colors             | White background, charcoal text, muted secondary text, blue links, subtle gray panels and pills. Dark mode uses corresponding readable tokens.                                                             |
| Image quality      | The user specifically requested placeholders; the photo marker is intentional. No borrowed portrait or fabricated personal image is used. UI icons come from al-folio's icon library.                      |
| Copy and content   | Identity, biography, CV, projects, and publications are explicitly placeholders. Only the supplied GitHub account and site URL are real account details.                                                   |

Expected differences: additional navigation for native al-folio pages; search and theme controls; native abstract/BibTeX controls; a single initial announcement; no fabricated contact details; placeholder photo and content; a writing section and framework attribution.

## Functional verification

- Native Jekyll production build succeeded.
- RenderCV generated the downloadable PDF from `_data/cv.yml`; all pages of the one-page result were visually inspected.
- The integration check verified 14 generated HTML pages, required feature containers, PDF, RSS, sitemap, and local link targets.
- Native search opened, filtered to CV, and navigated to the CV page.
- Publication filtering with `Another` hid the first entry and retained the matching entry.
- Abstract and BibTeX controls opened; keyboard activation and expanded state were checked. Closed panels were removed from the accessibility tree.
- Theme switching reached the dark state and returned to system/light.
- Mobile navigation expanded and opened the CV page.
- Project index-to-detail and blog index-to-post navigation succeeded.
- No site-origin console errors were observed. Browser-extension metadata errors were excluded from site findings.
- al-folio upgrade audit reported zero blocking and zero non-blocking findings after acknowledging the three intentional overrides.

## Remaining limits

Optional external integrations, specialized charts, notebooks, and Distill content are available through the native pinned plugins but are not exhaustively tested by this placeholder content. Test the relevant feature when adding it. The mobile check does not replace testing on a physical phone. GitHub Actions and public deployment are checked separately after the upload.

## Implementation checklist

- Completed: compact presentation, native content features, accessible publication controls, placeholders, build workflow, editing guide, visual review, and local integration checks.
- Next content pass: replace the explicit personal placeholders and remove the homepage placeholder note.
- Optional follow-up: test the populated content on additional browsers and a physical phone.
