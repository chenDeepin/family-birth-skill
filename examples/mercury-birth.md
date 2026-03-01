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
✅ Python 3.11.11
✅ Disk space: 156.42GB free

ℹ️  Domain: Chemistry Workflow Agent
ℹ️  Provider: Zhipu AI
ℹ️  Runtime: conda:PYMOLCODE

✅ Created directory structure at /home/chen/.hephaestusfamily/mercury
✅ Created SOUL.md
✅ Created USER.md
✅ Created AGENTS.md
✅ Created memory/short-term.yaml
✅ Created memory/long-term.yaml
✅ Created memory/now.yaml
✅ Created memory/selfreview.yaml
✅ Created config/runtime.yaml
✅ Created config/.env
✅ Created config/nanobot.json
✅ Registered in family-manifest.yaml
✅ Created FAMILY_MANIFESTO.md
✅ Created HEARTBEAT.md
✅ Created family-insights.yaml
✅ Created family-errors.yaml

============================================================
🎉 Birth Complete! Next Steps
============================================================

1️⃣  Set the API key:
    export MERCURY_API_KEY='your-api-key-here'

2️⃣  Activate the conda environment:
    conda activate PYMOLCODE

3️⃣  Install nanobot (if not already):
    pip install nanobot-ai

4️⃣  Start the child agent:
    nanobot agent

📁 Child workspace: ~/.hephaestusfamily/mercury/
🔑 API key env var: MERCURY_API_KEY

✨ The child will introduce themselves when started!
```

---

## Step 2: Provide API Key

```bash
# Option A: Manual export (temporary)
export MERCURY_API_KEY='your-zhipu-api-key-here'

# Option B: Add to shell config (permanent)
echo 'export MERCURY_API_KEY="your-key-here"' >> ~/.bashrc
source ~/.bashrc

# Option C: Use setup script
cd ~/.hephaestusfamily/mercury/config
./setup-env.sh mercury zai
```

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

Merge Mercury's config with nanobot's config:

```bash
# Option A: Direct edit
nano ~/.nanobot/config.json
# Add content from ~/.hephaestusfamily/mercury/config/nanobot.json

# Option B: Replace (if fresh install)
cp ~/.hephaestusfamily/mercury/config/nanobot.json ~/.nanobot/config.json
```

---

## Step 5: Start Mercury

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

## Step 6: Verify Mercury

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

## Step 7: Family Integration

Mercury is now:
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
└── mercury/
    ├── SOUL.md               # Identity and values
    ├── USER.md               # Who they serve
    ├── AGENTS.md             # Operating principles
    │
    ├── memory/
    │   ├── short-term.yaml   # Recent movements
    │   ├── long-term.yaml    # Persistent knowledge
    │   ├── now.yaml          # Active tasks
    │   ├── selfreview.yaml   # Mistakes & lessons
    │   │
    │   ├── domain/           # Chemistry-specific
    │   │   ├── compounds.yaml
    │   │   ├── proteins.yaml
    │   │   ├── workflows.yaml
    │   │   └── lessons.yaml
    │   │
    │   └── index/            # Fast lookup
    │       ├── l0-abstracts.yaml
    │       ├── semantic.yaml
    │       └── tags.yaml
    │
    ├── skills/
    │   ├── baseline/         # Mandatory skills
    │   └── domain/           # Chemistry skills
    │
    └── config/
        ├── runtime.yaml      # Runtime config
        ├── .env              # Environment vars
        └── nanobot.json      # Nanobot config
```

---

## Next Steps

1. **Teach Mercury skills** - Add chemistry-specific capabilities
2. **Monitor growth** - Watch memory/domain/lessons.yaml for insights
3. **Family sync** - Hephaestus checks Mercury during heartbeat
4. **Evolve** - Mercury will grow with experience

---

*Mercury Prime - First child of Hephaestus Family* 🔮
