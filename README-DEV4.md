# dev4 source portal

This copy references unnamespaced source components and permission sets. Deploy the prepared fitness source first and enable Digital Experiences. From this directory run:

```bash
python3 configure_portal.py --admin-username dev4@seven26fitness.com --sender-email info@seven26fitness.com

sf project deploy start --source-dir portal-src --target-org dev4 --dry-run --wait 60
sf project deploy start --source-dir portal-src --target-org dev4 --wait 60
```

This portal project uses portal-src, not force-app. Publish in Builder after verifying the site and client access. The older README-DEPLOY describes managed-package deployment; use this README for the prepared dev4 source copy.
