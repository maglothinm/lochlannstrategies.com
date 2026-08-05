# Rollback

By default, the installer creates a folder beside the website repository named similar to:

```text
lochlannstrategies.com-backup-v17.0.5-20260805T154927Z
```

To roll back, copy the backed-up files from that folder over the corresponding files in the website repository, then commit and push the restored files.

The backup includes the prior stylesheet and every HTML file whose stylesheet cache key was updated. The backup manifest lists all preserved files.
