# Proq Consultants — Website

A marketing site for **Proq Consultants** (domain: `proqconsultants.com.au`), covering:

- Cloud & Infrastructure
- AI & Cybersecurity
- Data Engineering & SI
- Quality & Automation

It's plain **HTML / CSS / JS** — no build step, no framework. That means it can be hosted almost anywhere for free.

## Files

```
proq-consultants-website/
├── index.html              # homepage
├── privacy-policy.html      # starter privacy policy (see legal note below)
├── terms.html                # starter terms of service (see legal note below)
├── styles.css
├── script.js                 # nav, scroll-reveal animations, contact form logic
├── site.webmanifest          # PWA/app icon manifest
├── robots.txt
├── sitemap.xml
├── README.md
└── assets/
    ├── logo.png                        # full logo (header/footer)
    ├── favicon.ico / favicon-16x16.png / favicon-32x32.png
    ├── apple-touch-icon.png
    ├── android-chrome-192x192.png / android-chrome-512x512.png
    ├── og-image.jpg                    # 1200x630 social share image
    └── generate_icons.py               # regenerates all the above from logo.png
```

## Preview locally

```bash
cd proq-consultants-website
python3 -m http.server 8000
# then visit http://localhost:8000
```

## Contact form — how it actually works

There's no backend at all. On submit, the form just opens the visitor's own email app with a `mailto:` link, pre-filled with their name, email, subject, and message addressed to `Business@proqconsultants.com.au`. Nothing is sent over the network, stored, or processed by any third party — it works identically on every host (Netlify, Vercel, GitHub Pages, Cloudflare Pages, or just opening the file locally). A hidden honeypot field is kept to silently swallow bot submissions.

## Easiest hosting options (pick one)

### 1. Netlify (drag & drop — easiest)
1. Go to https://app.netlify.com/drop
2. Drag the whole `proq-consultants-website` folder onto the page.
3. It deploys instantly with a free `*.netlify.app` URL.
4. In Site settings → Domain management, add your custom domain `proqconsultants.com.au` and follow the DNS instructions.

### 2. Vercel
```bash
npm i -g vercel
cd proq-consultants-website
vercel
```
Follow the prompts, then add `proqconsultants.com.au` under Project Settings → Domains.

### 3. GitHub Pages
```bash
cd proq-consultants-website
git init
git add .
git commit -m "Initial Proq Consultants website"
git branch -M main
git remote add origin <your-repo-url>
git push -u origin main
```
Settings → Pages → Deploy from branch `main` / root. Add a `CNAME` file containing `proqconsultants.com.au` for the custom domain.

### 4. Cloudflare Pages
Connect your GitHub repo at https://pages.cloudflare.com, or drag-and-drop the folder.

All four hosts work identically for the contact form since it's pure client-side `mailto:` — no backend to configure anywhere.

## Connecting the `proqconsultants.com.au` domain

1. Confirm the domain is registered (`.com.au` requires an active ABN).
2. In your host's dashboard, add `proqconsultants.com.au` as a custom domain.
3. Update DNS records at your registrar per the host's instructions.
4. Wait for propagation and enable HTTPS (automatic on Netlify/Vercel/Cloudflare Pages).

Once the domain is live, double-check these files still reference the right URL (they currently hardcode `https://www.proqconsultants.com.au/`): `index.html` (`<link rel="canonical">`, Open Graph/Twitter tags, JSON-LD), `robots.txt`, `sitemap.xml`.

## SEO / sharing already wired in

- Open Graph + Twitter Card tags (uses `assets/og-image.jpg`)
- `sitemap.xml` + `robots.txt`
- JSON-LD `ProfessionalService` structured data (name, address, phone, email) for Google
- Full favicon/app-icon set (light/dark, iOS, Android, PWA manifest)

To regenerate any of the icon/OG assets after changing the logo: `cd assets && python3 generate_icons.py` (requires Pillow: `pip3 install pillow`).

## Analytics (optional)

A commented-out Google Analytics 4 snippet is in `index.html`'s `<head>` — drop in your GA4 Measurement ID and uncomment to enable. A privacy-friendlier alternative is [Plausible](https://plausible.io) or [Fathom](https://usefathom.com).

## Legal pages

`privacy-policy.html` and `terms.html` are standard templates used by many small business sites (not custom legal advice, per the HTML comment at the top of each file). The contact form has no backend — it only opens the visitor's own email client — so there's no server-side storage or third-party processing of enquiry data to worry about. The site does embed Google Fonts and a Google Maps location, which are disclosed in the Privacy Policy.

## "Technologies We Work With" section — safe default, can be upgraded later

This section currently reads "Microsoft Azure" / "Oracle Cloud" (technologies used), not "Microsoft Partner" / "Oracle Partner" (a certified partner status). This was a deliberate choice: claiming official partner status without being a currently verified partner risks a complaint from Microsoft/Oracle directly, or a misleading-conduct issue under the Australian Consumer Law. Once you've confirmed your actual verified partner tier with each program, this can be changed back to "Partner" badges using their official assets.

## Editing content

- **Text/sections** → `index.html`
- **Colors/spacing/fonts** → `styles.css` (brand colors as CSS variables at the top: `--teal`, `--sky`, `--navy`)

## Contact details used on the site

- Email: Business@proqconsultants.com.au
- Phone: +61 449 192 016
- Address: 63 Casino St, Glenwood NSW 2768, Australia
