# Family Birth Skill

**Description:** Create and configure child agents for the Hephaestus family. Standardized birth process with templates, auth configuration, and family integration.

**Usage:**
```
/birth <child-name> <domain> <provider> [--conda-env ENV_NAME]
```

**Examples:**
```
/birth mercury chemistry zai --conda-env PYMOLCODE
/birth dockbot docking zai
/birth analyst data-analysis openrouter
```

**What it does:**
1. Creates child agent workspace in `~/.hephaestusfamily/{child-name}/`
2. Populates identity files (SOUL.md, USER.md, AGENTS.md)
3. Sets up memory system (short-term, long-term, now, selfreview, domain)
4. Configures baseline skills + domain-specific skills
5. Sets up auth configuration (env var based, no hardcoded keys)
6. Registers child in family manifest
7. Integrates with family heartbeat system

**Prerequisites:**
- Python 3.11+
- nanobot-ai package (installed in venv or conda env)
- Disk space (~500MB per child if creating new env)

**Options:**
- `--conda-env ENV_NAME` - Use existing conda environment (recommended for domain-specific tools)
- `--venv` - Create new virtual environment (default if no --conda-env)
- `--dry-run` - Preview what would be created without making changes
- `--provider-config PATH` - Custom provider config file

**Security:**
- API keys stored as environment variables: `{CHILD_NAME}_API_KEY`
- Never stores secrets in files that go to git
- Workspace isolation enforced
- Audit logging enabled

**After birth:**
1. Set API key: `export MERCURY_API_KEY="your-key"`
2. Activate environment: `conda activate PYMOLCODE` (or source venv)
3. Start child: `nanobot agent`
4. Verify child responds with identity

**Family Integration:**
- Child appears in family-manifest.yaml
- Errors logged to family-errors.yaml (bidirectional learning)
- Insights shared via family-insights.yaml
- Daily heartbeat checks child status

**Public Repository:** https://github.com/chenDeepin/family-birth-skill
