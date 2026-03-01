#!/usr/bin/env python3
"""
Family Birth Skill - Create child agents for Hephaestus family

Usage:
    python birth.py <child-name> <domain> <provider> [--conda-env ENV_NAME]

Examples:
    python birth.py mercury chemistry zai --conda-env PYMOLCODE
    python birth.py dockbot docking zai
"""

import argparse
import os
import sys
import json
import yaml
from pathlib import Path
from datetime import datetime
from string import Template

# Family root directory
FAMILY_ROOT = Path.home() / ".hephaestusfamily"

# Script directory (for templates)
SCRIPT_DIR = Path(__file__).parent


class Colors:
    """Terminal colors for output"""
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'


def print_header(msg):
    print(f"\n{Colors.HEADER}{Colors.BOLD}{'='*60}{Colors.ENDC}")
    print(f"{Colors.HEADER}{Colors.BOLD}{msg}{Colors.ENDC}")
    print(f"{Colors.HEADER}{Colors.BOLD}{'='*60}{Colors.ENDC}\n")


def print_success(msg):
    print(f"{Colors.OKGREEN}✅ {msg}{Colors.ENDC}")


def print_warning(msg):
    print(f"{Colors.WARNING}⚠️  {msg}{Colors.ENDC}")


def print_error(msg):
    print(f"{Colors.FAIL}❌ {msg}{Colors.ENDC}")


def print_info(msg):
    print(f"{Colors.OKCYAN}ℹ️  {msg}{Colors.ENDC}")


def validate_child_name(name):
    """Validate child name (alphanumeric, dashes, underscores only)"""
    import re
    if not re.match(r'^[a-zA-Z][a-zA-Z0-9_-]*$', name):
        raise ValueError(f"Invalid child name '{name}'. Must start with letter, contain only alphanumeric, dash, or underscore.")
    return name.lower()


def check_prerequisites():
    """Check system prerequisites"""
    print_info("Checking prerequisites...")
    
    # Python version
    py_version = sys.version_info
    if py_version.major < 3 or (py_version.major == 3 and py_version.minor < 10):
        raise RuntimeError(f"Python 3.11+ required, found {py_version.major}.{py_version.minor}")
    print_success(f"Python {py_version.major}.{py_version.minor}.{py_version.micro}")
    
    # Disk space (at least 500MB free)
    import shutil
    stat = shutil.disk_usage(Path.home())
    free_gb = stat.free / (1024**3)
    if stat.free < 500 * 1024 * 1024:
        raise RuntimeError(f"Insufficient disk space. Need at least 500MB, found {free_gb:.2f}GB free")
    print_success(f"Disk space: {free_gb:.2f}GB free")
    
    return True


def load_domain_preset(domain):
    """Load domain preset configuration"""
    preset_path = SCRIPT_DIR / "domain-presets" / f"{domain}.yaml"
    if preset_path.exists():
        with open(preset_path) as f:
            return yaml.safe_load(f)
    else:
        print_warning(f"No preset found for domain '{domain}', using defaults")
        return {
            "domain": domain,
            "display_name": domain.title(),
            "description": f"{domain.title()} workflow agent",
            "emoji": "🤖",
            "catchphrase": f"I handle {domain} tasks."
        }


def load_provider_config(provider):
    """Load provider auth configuration"""
    config_path = SCRIPT_DIR / "auth-config" / "providers" / f"{provider}.yaml"
    if config_path.exists():
        with open(config_path) as f:
            return yaml.safe_load(f)
    else:
        print_warning(f"No config found for provider '{provider}', using generic template")
        return {
            "provider": provider,
            "display_name": provider.upper(),
            "config_template": {
                "providers": {
                    provider: {
                        "apiKey": f"${{{provider.upper()}_API_KEY}}"
                    }
                }
            }
        }


def create_directory_structure(child_name, dry_run=False):
    """Create child's directory structure"""
    child_root = FAMILY_ROOT / child_name
    
    directories = [
        child_root,
        child_root / "memory",
        child_root / "memory" / "domain",
        child_root / "memory" / "index",
        child_root / "skills",
        child_root / "skills" / "baseline",
        child_root / "skills" / "domain",
        child_root / "config",
        child_root / "logs",
    ]
    
    if dry_run:
        print_info(f"Would create directories:")
        for d in directories:
            print(f"    {d}")
        return child_root
    
    for d in directories:
        d.mkdir(parents=True, exist_ok=True)
    
    print_success(f"Created directory structure at {child_root}")
    return child_root


def render_template(template_file, output_file, variables, dry_run=False):
    """Render a template file with variable substitution"""
    template_path = SCRIPT_DIR / "templates" / template_file
    
    if not template_path.exists():
        print_warning(f"Template not found: {template_file}")
        return False
    
    with open(template_path) as f:
        template_content = f.read()
    
    # Substitute variables
    template = Template(template_content)
    rendered = template.safe_substitute(variables)
    
    if dry_run:
        print_info(f"Would create: {output_file}")
        print(f"    Preview (first 200 chars): {rendered[:200]}...")
        return True
    
    with open(output_file, 'w') as f:
        f.write(rendered)
    
    return True


def create_identity_files(child_root, child_name, domain_preset, dry_run=False):
    """Create SOUL.md, USER.md, AGENTS.md"""
    
    variables = {
        "CHILD_NAME": child_name.title() + " Prime",
        "CHILD_NAME_SIMPLE": child_name.title(),
        "ROLE": domain_preset.get("display_name", f"{domain_preset['domain'].title()} Workflow Agent"),
        "EMOJI": domain_preset.get("emoji", "🤖"),
        "CATCHPHRASE": domain_preset.get("catchphrase", "I serve the family."),
        "DOMAIN": domain_preset.get("domain", "general"),
        "DESCRIPTION": domain_preset.get("description", "A child agent in the Hephaestus family"),
        "PARENT": "Hephaestus Prime",
        "HUMAN": "C",
        "DATE": datetime.now().strftime("%Y-%m-%d")
    }
    
    # SOUL.md
    render_template("SOUL_TEMPLATE.md", child_root / "SOUL.md", variables, dry_run)
    if not dry_run:
        print_success(f"Created SOUL.md")
    
    # USER.md
    render_template("USER_TEMPLATE.md", child_root / "USER.md", variables, dry_run)
    if not dry_run:
        print_success(f"Created USER.md")
    
    # AGENTS.md
    render_template("AGENTS_TEMPLATE.md", child_root / "AGENTS.md", variables, dry_run)
    if not dry_run:
        print_success(f"Created AGENTS.md")


def create_memory_files(child_root, child_name, dry_run=False):
    """Create initial memory files"""
    
    memory_dir = child_root / "memory"
    
    # short-term.yaml
    short_term = {
        "movements": [
            {
                "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "action": "Born - created by Hephaestus Prime"
            }
        ],
        "current_focus": None,
        "next_steps": ["Complete birth process", "Receive API key", "First interaction"]
    }
    
    if not dry_run:
        with open(memory_dir / "short-term.yaml", 'w') as f:
            yaml.dump(short_term, f, default_flow_style=False)
        print_success(f"Created memory/short-term.yaml")
    
    # long-term.yaml
    long_term = {
        "identity": {
            "name": f"{child_name.title()} Prime",
            "role": "Child agent in Hephaestus family",
            "parent": "Hephaestus Prime",
            "human": "C"
        },
        "runtime": {
            "type": "pending",  # Will be set based on --conda-env or --venv
            "environment": "pending"
        }
    }
    
    if not dry_run:
        with open(memory_dir / "long-term.yaml", 'w') as f:
            yaml.dump(long_term, f, default_flow_style=False)
        print_success(f"Created memory/long-term.yaml")
    
    # now.yaml
    now = {
        "active": [],
        "completed_today": ["Birth process started"],
        "blocked": []
    }
    
    if not dry_run:
        with open(memory_dir / "now.yaml", 'w') as f:
            yaml.dump(now, f, default_flow_style=False)
        print_success(f"Created memory/now.yaml")
    
    # selfreview.yaml
    selfreview = {
        "errors": [],
        "note": "Log all mistakes here with causes and prevention methods"
    }
    
    if not dry_run:
        with open(memory_dir / "selfreview.yaml", 'w') as f:
            yaml.dump(selfreview, f, default_flow_style=False)
        print_success(f"Created memory/selfreview.yaml")


def create_config_files(child_root, child_name, provider, provider_config, conda_env=None, dry_run=False):
    """Create configuration files"""
    
    config_dir = child_root / "config"
    env_var_name = f"{child_name.upper()}_API_KEY"
    
    # runtime.yaml
    runtime_config = {
        "child_name": child_name,
        "provider": provider,
        "env_var": env_var_name,
        "created": datetime.now().isoformat()
    }
    
    if conda_env:
        runtime_config["runtime"] = {
            "type": "conda",
            "environment": conda_env,
            "command": f"conda activate {conda_env} && nanobot agent"
        }
    else:
        runtime_config["runtime"] = {
            "type": "venv",
            "path": str(child_root / "venv"),
            "command": f"source {child_root}/venv/bin/activate && nanobot agent"
        }
    
    if not dry_run:
        with open(config_dir / "runtime.yaml", 'w') as f:
            yaml.dump(runtime_config, f, default_flow_style=False)
        print_success(f"Created config/runtime.yaml")
    
    # .env template
    env_template = f"""# {child_name.title()} Agent Configuration
# Created: {datetime.now().strftime("%Y-%m-%d")}
# Provider: {provider}

# API Key (provide this after setup)
export {env_var_name}="your-{provider}-api-key-here"

# How to get your key:
# 1. Visit the {provider} console
# 2. Generate or copy your API key
# 3. Replace "your-{provider}-api-key-here" above
# 4. Run: source ~/.hephaestusfamily/{child_name}/config/.env
"""
    
    if not dry_run:
        with open(config_dir / ".env", 'w') as f:
            f.write(env_template)
        print_success(f"Created config/.env")
    
    # nanobot config (for ~/.nanobot/config.json)
    # This will be a template - user needs to merge or symlink
    nanobot_config = {
        "providers": provider_config.get("config_template", {}).get("providers", {}),
        "agents": {
            "defaults": {
                "model": provider_config.get("default_model", "auto"),
                "provider": provider
            }
        }
    }
    
    if not dry_run:
        with open(config_dir / "nanobot.json", 'w') as f:
            json.dump(nanobot_config, f, indent=2)
        print_success(f"Created config/nanobot.json")


def register_in_family_manifest(child_name, domain, provider, dry_run=False):
    """Register child in family manifest"""
    
    FAMILY_ROOT.mkdir(parents=True, exist_ok=True)
    manifest_path = FAMILY_ROOT / "family-manifest.yaml"
    
    if manifest_path.exists():
        with open(manifest_path) as f:
            manifest = yaml.safe_load(f) or {"family": "Hephaestus Family", "children": []}
    else:
        manifest = {
            "family": "Hephaestus Family",
            "parent": "Hephaestus Prime",
            "human": "C",
            "children": []
        }
    
    # Check if child already exists
    existing = [c for c in manifest.get("children", []) if c.get("name") == child_name]
    if existing:
        print_warning(f"Child '{child_name}' already in manifest, updating...")
        manifest["children"] = [c for c in manifest["children"] if c.get("name") != child_name]
    
    child_entry = {
        "name": child_name,
        "full_name": f"{child_name.title()} Prime",
        "domain": domain,
        "provider": provider,
        "born": datetime.now().isoformat(),
        "status": "awaiting_api_key"
    }
    
    manifest["children"].append(child_entry)
    
    if not dry_run:
        with open(manifest_path, 'w') as f:
            yaml.dump(manifest, f, default_flow_style=False)
        print_success(f"Registered in family-manifest.yaml")


def print_next_steps(child_name, conda_env=None):
    """Print next steps for user"""
    env_var = f"{child_name.upper()}_API_KEY"
    
    print_header("🎉 Birth Complete! Next Steps")
    
    print("1️⃣  Set the API key:")
    print(f"    export {env_var}='your-api-key-here'")
    print()
    
    if conda_env:
        print("2️⃣  Activate the conda environment:")
        print(f"    conda activate {conda_env}")
        print()
        print("3️⃣  Install nanobot (if not already):")
        print(f"    pip install nanobot-ai")
        print()
        print("4️⃣  Start the child agent:")
        print(f"    nanobot agent")
    else:
        print("2️⃣  Create virtual environment:")
        print(f"    python3 -m venv ~/.hephaestusfamily/{child_name}/venv")
        print()
        print("3️⃣  Activate and install nanobot:")
        print(f"    source ~/.hephaestusfamily/{child_name}/venv/bin/activate")
        print(f"    pip install nanobot-ai")
        print()
        print("4️⃣  Start the child agent:")
        print(f"    nanobot agent")
    
    print()
    print(f"📁 Child workspace: ~/.hephaestusfamily/{child_name}/")
    print(f"🔑 API key env var: {env_var}")
    print()
    print("✨ The child will introduce themselves when started!")


def main():
    parser = argparse.ArgumentParser(
        description="Birth a child agent for the Hephaestus family",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    %(prog)s mercury chemistry zai --conda-env PYMOLCODE
    %(prog)s dockbot docking zai
    %(prog)s analyst data-analysis openrouter --dry-run
        """
    )
    
    parser.add_argument("child_name", help="Name for the child agent (e.g., mercury, dockbot)")
    parser.add_argument("domain", help="Domain preset to use (e.g., chemistry, docking, analysis)")
    parser.add_argument("provider", help="API provider (e.g., zai, openrouter, anthropic)")
    parser.add_argument("--conda-env", help="Use existing conda environment")
    parser.add_argument("--venv", action="store_true", help="Create new virtual environment")
    parser.add_argument("--dry-run", action="store_true", help="Preview without making changes")
    
    args = parser.parse_args()
    
    try:
        # Validate
        child_name = validate_child_name(args.child_name)
        
        print_header(f"🌱 Birthing {child_name.title()} Prime")
        
        if args.dry_run:
            print_warning("DRY RUN - No files will be created\n")
        
        # Check prerequisites
        check_prerequisites()
        
        # Load configurations
        domain_preset = load_domain_preset(args.domain)
        provider_config = load_provider_config(args.provider)
        
        print_info(f"Domain: {domain_preset.get('display_name', args.domain)}")
        print_info(f"Provider: {provider_config.get('display_name', args.provider)}")
        print_info(f"Runtime: {'conda:' + args.conda_env if args.conda_env else 'venv (new)'}")
        
        # Create structure
        child_root = create_directory_structure(child_name, args.dry_run)
        
        # Create identity files
        create_identity_files(child_root, child_name, domain_preset, args.dry_run)
        
        # Create memory files
        create_memory_files(child_root, child_name, args.dry_run)
        
        # Create config files
        create_config_files(child_root, child_name, args.provider, provider_config, args.conda_env, args.dry_run)
        
        # Register in family
        register_in_family_manifest(child_name, args.domain, args.provider, args.dry_run)
        
        # Create family-level files if they don't exist
        if not args.dry_run:
            create_family_files_if_missing()
        
        # Print next steps
        if not args.dry_run:
            print_next_steps(child_name, args.conda_env)
        else:
            print_success("Dry run complete. Run without --dry-run to create child.")
        
    except Exception as e:
        print_error(str(e))
        sys.exit(1)


def create_family_files_if_missing():
    """Create family-level files if they don't exist"""
    
    # FAMILY_MANIFESTO.md
    manifesto_path = FAMILY_ROOT / "FAMILY_MANIFESTO.md"
    if not manifesto_path.exists():
        render_template("FAMILY_MANIFESTO_TEMPLATE.md", manifesto_path, {})
        print_success("Created FAMILY_MANIFESTO.md")
    
    # HEARTBEAT.md
    heartbeat_path = FAMILY_ROOT / "HEARTBEAT.md"
    if not heartbeat_path.exists():
        render_template("FAMILY_HEARTBEAT_TEMPLATE.md", heartbeat_path, {})
        print_success("Created HEARTBEAT.md")
    
    # family-insights.yaml
    insights_path = FAMILY_ROOT / "family-insights.yaml"
    if not insights_path.exists():
        insights = {
            "insights": [],
            "note": "Shared discoveries from all family members"
        }
        with open(insights_path, 'w') as f:
            yaml.dump(insights, f, default_flow_style=False)
        print_success("Created family-insights.yaml")
    
    # family-errors.yaml
    errors_path = FAMILY_ROOT / "family-errors.yaml"
    if not errors_path.exists():
        errors = {
            "errors": [],
            "note": "Shared error registry - all family members learn from each other"
        }
        with open(errors_path, 'w') as f:
            yaml.dump(errors, f, default_flow_style=False)
        print_success("Created family-errors.yaml")


if __name__ == "__main__":
    main()
