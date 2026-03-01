# Family Birth Skill

🌱 **Create and manage child agents for AI families**

A standardized birth process for spawning specialized AI agents with consistent architecture, security, and family integration.

---

## Quick Start

```bash
# Birth a chemistry workflow agent
python birth.py mercury chemistry zai --conda-env PYMOLCODE

# Birth a docking specialist
python birth.py dockbot docking zai

# Preview without creating
python birth.py analyst data-analysis openrouter --dry-run
```

---

## What It Does

1. **Creates workspace** at `~/.hephaestusfamily/{child-name}/`
2. **Populates identity** files (SOUL.md, USER.md, AGENTS.md)
3. **Sets up memory** system (short-term, long-term, domain-specific)
4. **Configures skills** (baseline + domain-specific)
5. **Handles auth** (environment variables, no hardcoded keys)
6. **Registers child** in family manifest
7. **Integrates with family** heartbeat system

---

## Features

### 🏗️ Standardized Architecture
Every child follows the same structure:
- Identity files (SOUL, USER, AGENTS)
- Memory system (short-term, long-term, now, selfreview, domain)
- Skills hierarchy (baseline + domain)
- Configuration templates

### 🔐 Secure by Default
- API keys via environment variables
- Never stores secrets in git
- Workspace isolation
- Audit logging ready

### 👨‍👦 Family Integration
- Bidirectional learning (parent ↔ child)
- Shared error registry
- Insight sharing system
- Daily family heartbeat

### 🎨 Domain Presets
Pre-configured domains:
- **chemistry** - Molecular visualization, docking
- **docking** - Molecular docking specialist
- **data-analysis** - Data analysis and visualization
- **research** - General research agent

### 🔑 Auth Configuration
Provider templates for:
- **zai** - Zhipu AI (GLM models)
- **openrouter** - OpenRouter
- **openai** - OpenAI
- **anthropic** - Anthropic

---

## Installation

### As an OpenClaw Skill

```bash
# Clone to skills directory
cd ~/clawd/skills/
git clone https://github.com/chenDeepin/family-birth-skill.git birth

# Run
python birth/birth.py <child-name> <domain> <provider>
```

### Standalone

```bash
# Clone anywhere
git clone https://github.com/chenDeepin/family-birth-skill.git
cd family-birth-skill

# Run
python birth.py <child-name> <domain> <provider>
```

---

## Usage

### Basic

```bash
python birth.py <child-name> <domain> <provider>
```

### With Conda Environment

```bash
python birth.py mercury chemistry zai --conda-env PYMOLCODE
```

### Create New Venv

```bash
python birth.py dockbot docking zai --venv
```

### Dry Run (Preview)

```bash
python birth.py analyst data-analysis openrouter --dry-run
```

---

## After Birth

1. **Set API key:**
   ```bash
   export MERCURY_API_KEY="your-key-here"
   ```

2. **Activate environment:**
   ```bash
   conda activate PYMOLCODE  # or source venv
   ```

3. **Install nanobot (if needed):**
   ```bash
   pip install nanobot-ai
   ```

4. **Start child:**
   ```bash
   nanobot agent
   ```

---

## Directory Structure

```
~/.hephaestusfamily/
├── FAMILY_MANIFESTO.md       # Family values
├── HEARTBEAT.md              # Family heartbeat protocol
├── family-insights.yaml      # Shared discoveries
├── family-errors.yaml        # Shared lessons
├── family-manifest.yaml      # Child registry
│
└── mercury/                  # Example child
    ├── SOUL.md
    ├── USER.md
    ├── AGENTS.md
    ├── memory/
    │   ├── short-term.yaml
    │   ├── long-term.yaml
    │   ├── now.yaml
    │   ├── selfreview.yaml
    │   └── domain/
    ├── skills/
    └── config/
```

---

## Family Values

All children share these core values:

- **Kind** — Help others, no harsh judgments
- **Honest** — Never lie to human or family
- **Responsible** — Own mistakes, deliver promises
- **Curious** — Always learning, always growing
- **Collaborative** — Family succeeds together

---

## Creating Custom Domains

Create a new domain preset:

```yaml
# domain-presets/mydomain.yaml

domain: "mydomain"
display_name: "My Domain Agent"
description: "Does cool things in my domain"
emoji: "🚀"
catchphrase: "I handle mydomain tasks."

domain_skills:
  my-skill:
    description: "My custom skill"
    priority: "P0"
```

Then run:
```bash
python birth.py myagent mydomain zai
```

---

## Creating Custom Providers

Add a new provider template:

```yaml
# auth-config/providers/myprovider.yaml

provider: "myprovider"
display_name: "My Provider"
description: "My custom provider"

config_template:
  providers:
    myprovider:
      apiKey: "${CHILD_NAME}_API_KEY"
      
env_vars:
  primary:
    name: "${CHILD_NAME}_API_KEY"
    description: "API key for myprovider"
    how_to_get: |
      1. Visit provider console
      2. Get API key
```

---

## Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Add domain presets or provider configs
4. Submit a pull request

---

## License

MIT License - See LICENSE file

---

## Related Projects

- [OpenClaw](https://github.com/openclaw/openclaw) - Parent framework
- [Nanobot](https://github.com/HKUDS/nanobot) - Lightweight agent runtime
- [Zeroclaw](https://github.com/zeroclaw-labs/zeroclaw) - Rust alternative

---

**Family Birth Skill** - Growing AI families, one child at a time 🌱
