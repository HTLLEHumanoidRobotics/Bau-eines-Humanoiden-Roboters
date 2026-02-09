# 🚀 Quick Start Guide - Creating Print Issues

This guide explains how to create GitHub issues for all the parts that need to be printed for the humanoid robot project.

## 📊 Overview

The repository contains **92 parts** across 4 categories:
- **A-Head (Face/Neck):** 17 parts
- **B-Body (Ribcage):** 28 parts  
- **C-Arm (Shoulder/Elbow/Forearm):** 35 parts
- **D-Hand&Finger:** 12 parts

## 🎯 Three Ways to Create Issues

### Method 1: Automated Batch Creation (Fastest) ⚡

Create all 92 issues at once using the GitHub CLI:

```bash
# Navigate to the Print directory
cd Files/Print

# Run the batch creation script
./create_issues_batch.sh
```

**Requirements:**
- GitHub CLI installed ([download here](https://cli.github.com/))
- Authenticated with GitHub (`gh auth login`)
- Permission to create issues in the repository

**What it does:**
- Creates all 92 issues automatically
- Adds appropriate labels (printing + category)
- Pre-fills all part information
- Takes ~1 minute to complete

### Method 2: Using Pre-Generated Templates (Recommended) 📋

Use the ready-made templates for individual issues:

1. Open `Files/Print/issue_templates/all_printing_issues.md`
2. Search for the part you want to print (e.g., "A01" or "Face")
3. Copy the markdown template between the ``` markers
4. Go to [GitHub Issues](https://github.com/HTLLEHumanoidRobotics/Bau-eines-Humanoiden-Roboters/issues/new)
5. Select the "Printing_Issue" template
6. Paste your copied content
7. Submit the issue

**Example:**
```markdown
Title: Print: [A01]

## 🖨️ Printing Issue Template

### 🔧 Teilinformationen
- **Part Number:** A01
- **Part Name:** Face
- **Menge:** 1
- **Farbe:** Weiß

### ⏱️ Zeit
- **Geplante Druckzeit:** ___ h ___ min
- **Tatsächliche Druckzeit:** ___ h ___ min

### 📒 Notizen
- 

### ⚙️ Druckeinstellungen (relevant)
- Drucker:
- Material / Filament:
- Nozzle / Layerhöhe:
- Infill / Support:
```

### Method 3: Manual Creation from Template 📝

Create issues from scratch using the template:

1. Go to [GitHub Issues → New Issue](https://github.com/HTLLEHumanoidRobotics/Bau-eines-Humanoiden-Roboters/issues/new)
2. Click the "Printing_Issue" template
3. Fill in all the fields manually
4. Submit the issue

## 📦 Available Resources

### Generated Files

All files are in `Files/Print/issue_templates/`:

| File | Description | Use Case |
|------|-------------|----------|
| `all_printing_issues.md` | All 92 issue templates | Copy-paste individual issues |
| `printing_summary.md` | Summary table of all parts | Quick reference, planning |
| `printing_parts.csv` | Spreadsheet format | Excel, tracking, sorting |
| `printing_issues.json` | API-ready format | Automated creation, scripts |

### Scripts

| Script | Purpose |
|--------|---------|
| `generate_print_issues.py` | Generate/update all templates |
| `create_issues_batch.sh` | Batch create all issues via CLI |

## 🔄 Workflow After Creating Issues

Once issues are created:

1. **Before Printing:**
   - Assign the issue to yourself
   - Read the printing instructions PDF
   - Fill in planned print time

2. **During Printing:**
   - Update the issue with progress
   - Note any problems or observations
   - Take photos for documentation

3. **After Printing:**
   - Update with actual print time
   - Add photos to `Files/Print/Media/pictures/`
   - Update `PRINT_LOG.md` with completion details
   - Close the issue

## 🛠️ Updating Templates

If new parts are added or you need to regenerate templates:

```bash
cd Files/Print
python3 generate_print_issues.py
```

This will scan all STL files and regenerate all template files.

## 📈 Tracking Progress

Use `Files/Print/PRINT_LOG.md` to track completed prints:
- Part A01 (Face) is already logged as an example
- Add new entries as parts are completed
- Update statistics at the top

## 🆘 Troubleshooting

### Batch Script Issues

**Problem:** `gh: command not found`
```bash
# Install GitHub CLI
# macOS: brew install gh
# Windows: Download from https://cli.github.com/
# Linux: See https://github.com/cli/cli/blob/trunk/docs/install_linux.md
```

**Problem:** `Error: Not authenticated`
```bash
gh auth login
# Follow the prompts to authenticate
```

### Template Generation Issues

**Problem:** Script doesn't find STL files
```bash
# Verify you're in the right directory
cd Files/Print
pwd  # Should end in Files/Print

# Run the script
python3 generate_print_issues.py
```

## 📚 Additional Documentation

- [Print Directory README](Files/Print/README.md) - Main documentation
- [Issue Templates README](Files/Print/issue_templates/README.md) - Template details
- [GitHub Issue Template](.github/ISSUE_TEMPLATE/printing_issue.md) - Base template

---

**Need Help?** Open an issue with the question label or contact the project maintainers.
