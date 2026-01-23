# gpunkt.org - Display Repository

Präsentationsschicht für [gpunkt.org](https://gpunkt.org) - Bosnisch-Deutsches Wörterbuch.

## Architektur

- **Engine:** Quartz v4.5.1
- **Content Sync:** Auto-sync von [gpunkt-woerter](https://github.com/alemsabic/gpunkt-woerter)
- **Deployment:** Cloudflare Pages
- **Branch:** v4 (production)

## Local Development

```bash
npm install
npx quartz build --serve
```

Visit: http://localhost:8080

## Deployment

Auto-deployed to Cloudflare Pages on push to `v4` branch.

Live: [gpunkt.org](https://gpunkt.org)
