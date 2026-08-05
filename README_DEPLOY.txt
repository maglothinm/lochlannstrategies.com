LOCHLANN STRATEGIES v17.0.3 — NAME-SEARCH OVERLAY
==================================================

Purpose
-------
This package updates the existing Lochlann Strategies v17.0.2 website so
search engines can associate Michael Maglothin more clearly with Lochlann
Strategies. It preserves the current v17 visual system, navigation, imagery,
CSS, JavaScript, page URLs, and all unmodified content.

This is an OVERLAY, not a complete website replacement.
Do not delete the existing repository or assets directory.

Files to replace in the repository root
---------------------------------------
1. index.html
2. about.html
3. sitemap.xml

The other files in this ZIP are deployment and verification notes only.

Deployment through GitHub
-------------------------
1. Extract this ZIP.
2. Open the existing maglothinm/lochlannstrategies.com repository.
3. Upload index.html, about.html, and sitemap.xml to the repository root.
4. Allow GitHub to replace the three existing files.
5. Preserve all existing assets, other HTML pages, robots.txt, and CNAME.
6. Commit the three replacements together.
7. After GitHub Pages publishes, verify:
   https://lochlannstrategies.com/
   https://lochlannstrategies.com/about.html

Search-engine follow-through
----------------------------
After publication, inspect and request indexing for both URLs in Google
Search Console. Resubmit https://lochlannstrategies.com/sitemap.xml.
The same sitemap can be submitted through Bing Webmaster Tools.

No build process is required.
