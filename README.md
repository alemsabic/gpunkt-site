# nekontam.com - Display Repository

Präsentationsschicht für [nekontam.com](https://nekontam.com) - Bosnisch-Deutsches Wörterbuch.

## Architektur

- **Engine:** Quartz v4.5.1
- **Content Sync:** Auto-sync von [nekontam-woerter](https://github.com/alemsabic/nekontam-woerter)
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

Live: [nekontam.com](https://nekontam.com)
