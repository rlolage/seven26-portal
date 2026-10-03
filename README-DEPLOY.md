# Seven26 portal deployment candidate

Prerequisites: Seven26 managed 2GP installed in package-test; Digital Experiences enabled and domain saved in that org; same active internal admin user exists as supplied below. Python 3 and Salesforce CLI installed.

This project deploys the existing enhanced LWR site, not a new package. It copies pages, routes, navigation, LWR branding palettes, theme layouts and CSS. Do not merge with the core packaging project. Do not create a duplicate empty site first. If a site with the same names or URL prefixes already exists, stop and inspect it before deployment to avoid updating an unintended site.

1. Extract and cd into seven26-portal (contains sfdx-project.json).
2. Authorize if needed: sf org login web --alias package-test
3. Enable Digital Experiences in Setup > Digital Experiences > Settings and save the domain.
4. Configure using the actual test-org admin USERNAME, not merely their email address:

python3 configure_portal.py --admin-username 'ADMIN_USERNAME' --sender-email 'YOUR_EMAIL_ADDRESS'

5. Check target identity and package installation: sf org open --target-org package-test
6. Validate:

sf project deploy start --source-dir portal-src --target-org package-test --dry-run --wait 30

7. If validation succeeds, deploy:

sf project deploy start --source-dir portal-src --target-org package-test --wait 30

8. Setup > Digital Experiences > All Sites > seven26fitness > Builder. Inspect pages and logo, then Publish. Use the UI initially to verify the site identity. Site membership includes System Administrator and installed Fitness Client Access permission set. Assign Fitness Client Access to test clients. Review Administration > Emails, Login & Registration, and Settings before activation; select available default email templates if needed and verify the sender. Self-registration is disabled and welcome emails are disabled in the prepared deployment. Configure a supported cloned external profile before enabling self-registration.
9. Recreate client sharing sets against installed namespaced custom objects and test access using a portal user. Object permission alone does not grant client-specific record access. Do not grant broad object access to the guest user.
10. Test client login, Programs/Home, Assessments, Body Composition, Progress and Badges; confirm another client's records are inaccessible. If a blank page appears, capture browser console error and deployment result.

Details: source names retained: Network seven26fitness, CustomSite seven26fitness, DigitalExperienceBundle site/seven26fitness1, DigitalExperienceConfig seven26fitness1. LWR path seven26fitness; backing Network/CustomSite path seven26fitnessvforcesite retained. Salesforce assigns the domain in the target org.

Installed LWC definitions use seven26fitness: rather than c:. Visualforce references use seven26fitness__. Removed source-only external profile membership/self-registration and source email-template references; Admin and installed Fitness Client Access membership remain. Backing CustomSite is active (required); Network stays UnderConstruction to allow verification before publication. Other site settings and LWR theme content preserved.

Source forgot-password page referenced CMS key MCT5QBVPQPEFF37JRA7D3D4L2DTE, whose media bytes were absent from the ZIP. That single image reference now uses the supplied site_logo image via a local static resource. Other empty logo slots remain as in source; set them in Builder if wanted. CMS content workspaces and legacy NetworkBranding are not deployed; enhanced LWR branding is in the copied site bundle. Navigation retains source Topics link; remove it in Builder if the destination does not use topics.

Local validation: XML and JSON parsed, six custom component references checked against installed-package source, original admin/profile references removed, CSS preserved. No authenticated Salesforce deployment was run here. This is a prepared deployment candidate; platform-specific dependencies can still be reported by dry-run. Share any errors for correction before deploying/publishing.

## Revision 2

CustomSite.active must be true for this network site. Network status remains UnderConstruction; welcome emails and self-registration remain disabled. Required changePasswordTemplate plus forgotPasswordTemplate/welcomeTemplate restored with three included text templates under unique Seven26Portal names; this avoids overwriting destination standard templates. Missing Network errors for navigation/configuration were downstream of the failed Network creation. Rerun configure_portal.py after extracting this revision before dry-run. No authenticated Salesforce deployment was performed.
