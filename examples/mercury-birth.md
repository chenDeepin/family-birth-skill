# Example: Birthing Mercury Prime

This example shows the complete process of creating Mercury, a chemistry workflow agent.

---

## Step 1: Run Birth Command

```bash
cd ~/clawd/skills/birth
python birth.py mercury chemistry zai --conda-env PYMOLCODE
```

**Output:**
```
============================================================
🌱 Birthing Mercury Prime
============================================================

ℹ️  Checking prerequisites...
✅ Python 3.10.12
✅ Disk space: 55.41GB free

ℹ️  Domain: Chemistry Workflow Agent
ℹ️  Provider: Zhipu AI
ℹ️  Runtime: conda:PYMOLCODE

✅ Created directory structure at /home/chen/.hephaestusfamily/mercury
✅ Created SOUL.md
✅ Created USER.md
✅ Created AGENTS.md
[...]

============================================================
🎉 Birth Complete! Next Steps
============================================================

1️⃣  Set the API key:
    export {CHILD_NAME}_API_KEY='your-api-key-here'

2️⃣  Activate the conda environment:
    conda activate PYMOLCODE

3️⃣  Install nanobot (if not already):
    pip install nanobot-ai

4️⃣  Start the child agent:
    nanobot agent

📁 Child workspace: ~/.hephaestusfamily/{child-name}/
🔑 API key env var: {CHILD_NAME}_API_KEY

✨ The child will introduce themselves when started!
```

---

## Step 2: Provide API Key

**Important:** Replace `{CHILD_NAME}` with your actual child name (e.g., `MERCURY`)

```bash
# Option A: Manual export (temporary)
export MERCURY_API_KEY='your-zhipu-api-key-here'

# Option B: Add to shell config (permanent)
echo 'export MERCURY_API_KEY="your-key-here"' >> ~/.bashrc
source ~/.bashrc

# Option C: Use setup script
cd ~/.hephaestusfamily/mercury/config
./setup-env.sh mercury zai
# Then provide your key when prompted
```

**Note:** The environment variable name format is `{CHILD_NAME}_API_KEY` in uppercase.
- For child "mercury" → `MERCURY_API_KEY`
- For child "dockbot" → `DOCKBOT_API_KEY`

---

## Step 3: Install Nanobot

```bash
# Activate conda environment
conda activate PYMOLCODE

# Install nanobot (if not already installed)
pip install nanobot-ai
```

---

## Step 4: Configure Nanobot

Merge child's config with nanobot's config:

```bash
# Option A: Direct edit
nano ~/.nanobot/config.json
# Add content from ~/.hephaestusfamily/{child-name}/config/nanobot.json

# Option B: Replace (if fresh install)
cp ~/.hephaestusfamily/{child-name}/config/nanobot.json ~/.nanobot/config.json
```

**For ZAI provider:**
```json
{
  "providers": {
    "zhipu": {
      "apiKey": "${CHILD_NAME}_API_KEY",
      "apiBase": "https://open.bigmodel.cn/api/paas/v4"
    }
  },
  "agents": {
    "defaults": {
      "model": "glm-4-plus",
      "provider": "zhipu"
    }
  }
}
```

---

## Step 5: Copy Child's Identity to Nanobot Workspace

```bash
cp ~/.hephaestusfamily/{child-name}/SOUL.md ~/.nanobot/workspace/SOUL.md
cp ~/.hephaestusfamily/{child-name}/USER.md ~/.nanobot/workspace/USER.md
cp ~/.hephaestusfamily/{child-name}/AGENTS.md ~/.nanobot/workspace/AGENTS.md
```

---

## Step 6: Start Child Agent

```bash
conda activate PYMOLCODE
nanobot agent
```

**Expected output:**
```
🔮 Mercury Prime online.

I see molecules clearly.

How can I help you today, C?
```

---

## Step 7: Verify Child

Send a test message:
```
You: Load the structure 1IEP and show me the binding pocket.
```

**Expected response:**
```
Mercury: I'll load PDB 1IEP and visualize the binding pocket.
[loads structure]
[renders pocket]

Here's the ABL kinase structure with the ATP binding pocket highlighted.
The DFG motif is clearly visible at the activation loop.

Should I show specific interactions or prepare a publication figure?
```

---

## Step 8: Family Integration

Child is now:
- ✅ Registered in `~/.hephaestusfamily/family-manifest.yaml`
- ✅ Connected to family insights system
- ✅ Connected to family errors system
- ✅ Monitored by Hephaestus's heartbeat

---

## Directory Structure Created

```
~/.hephaestusfamily/
├── FAMILY_MANIFESTO.md
├── HEARTBEAT.md
├── family-insights.yaml
├── family-errors.yaml
├── family-manifest.yaml
│
└── {child-name}/               # e.g., mercury/
    ├── SOUL.md                 # Identity and values
    ├── USER.md                 # Who they serve
    ├── AGENTS.md               # Operating principles
    │
    ├── memory/
    │   ├── short-term.yaml     # Recent movements
    │   ├── long-term.yaml      # Persistent knowledge
    │   ├── now.yaml            # Active tasks
    │   ├── selfreview.yaml     # Mistakes & lessons
    │   │
    │   ├── domain/             # Domain-specific
    │   │   ├── compounds.yaml
    │   │   ├── proteins.yaml
    │   │   ├── workflows.yaml
    │   │   └── lessons.yaml
    │   │
    │   └── index/              # Fast lookup
    │
    ├── skills/
    │   ├── baseline/           # Shared skills (via shared/skills/)
    │   └── domain/             # Domain-specific skills
    │
    └── config/
        ├── runtime.yaml        # Runtime config
        ├── .env                # Environment vars
        └── nanobot.json        # Nanobot config
```

---

## Next Steps

1. **Teach skills** - Add domain-specific capabilities
2. **Monitor growth** - Watch memory/domain/lessons.yaml for insights
3. **Family sync** - Parent checks child during heartbeat
4. **Evolve** - Child will grow with experience

---

## Template Variables

When using this example, replace:
- `{CHILD_NAME}` → Your child's name (e.g., `mercury`, `dockbot`)
- `{CHILD_NAME}` (uppercase) → Environment variable (e.g., `MERCURY_API_KEY`)
- `{provider}` → Your API provider (e.g., `zai`, `openrouter`)

---

*Example completed 2026-03-01*
