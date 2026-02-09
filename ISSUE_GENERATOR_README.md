# Issue Generator for 3D Printing Tasks

This tool automatically generates GitHub issues for all the 3D printable parts in your humanoid robot project.

## What This Tool Does

The `generate_print_issues.py` script:
- 🔍 Scans all STL files in the `Files/Print/pib_stl/` directory
- 📝 Generates individual issue content for each part (86 parts total)
- 🏷️ Categorizes parts by robot component (Head, Body, Arm, Hand & Fingers)
- 📂 Creates ready-to-use markdown files in the `generated_issues/` directory
- 🚀 Provides a bash script for bulk issue creation using GitHub CLI

## Quick Start

### Step 1: Generate Issue Files

```bash
python3 generate_print_issues.py
```

This creates:
- `generated_issues/` directory with 86 markdown files
- `generated_issues/README.md` with a summary and instructions
- `generated_issues/create_all_issues.sh` for automated issue creation

### Step 2: Create Issues in GitHub

You have **three options** to create the issues:

#### Option A: Automated (GitHub CLI) - RECOMMENDED

If you have the [GitHub CLI](https://cli.github.com/) installed:

```bash
cd generated_issues
./create_all_issues.sh
```

This will create all 86 issues at once with appropriate labels and categories.

#### Option B: Manual Creation (for selective parts)

1. Navigate to: https://github.com/HTLLEHumanoidRobotics/Bau-eines-Humanoiden-Roboters/issues
2. Click "New Issue"
3. Choose the "Printing_Issue" template
4. Open the corresponding `.md` file from `generated_issues/`
5. Copy the content and paste it into the issue
6. Set the title (e.g., "Print: A01 - Face")
7. Add labels: `printing`, `3d-print`, and the category (e.g., `head`)

#### Option C: GitHub API (for developers)

Use the GitHub REST API with a personal access token. See the [GitHub API documentation](https://docs.github.com/en/rest/issues/issues#create-an-issue).

## Issue Structure

Each generated issue includes:

- ✅ **Part Information**: Part number, name, category, and STL file path
- ⏱️ **Time Tracking**: Fields for planned vs actual print time
- 📒 **Notes**: Space for documenting issues or observations
- ⚙️ **Print Settings**: Printer, material, nozzle settings, infill, support
- 📋 **Progress Checklist**: From STL verification to post-processing

## Part Categories

The 86 parts are organized into 4 main categories:

- **Head** (16 parts): Face, neck, inner components
- **Body** (15 parts): Ribcage, electronics housing, connectors
- **Arm** (35 parts): Shoulders, elbows, forearms
- **Hand & Fingers** (20 parts): Palm, fingers, thumb components

## Regenerating Issues

If STL files are added or modified:

```bash
python3 generate_print_issues.py
```

The script will regenerate all issue files. Note that this overwrites existing files in `generated_issues/`.

## Customization

To modify the issue template, edit the `generate_issue_content()` function in `generate_print_issues.py`.

## Notes

- The `generated_issues/` directory is in `.gitignore` to avoid committing generated files
- Run the script whenever you add new STL files to the project
- The existing `.github/ISSUE_TEMPLATE/printing_issue.md` template is for manual issue creation

## Troubleshooting

**Q: The script doesn't find any STL files**
- Check that STL files exist in `Files/Print/pib_stl/`
- Verify the directory structure matches the expected format

**Q: GitHub CLI authentication fails**
- Run `gh auth login` to authenticate
- Ensure you have write permissions to the repository

**Q: I want to create issues for only some parts**
- Use Option B (manual creation) for selective parts
- Or modify the bash script to comment out unwanted parts

## Support

For issues or questions about this tool, please open an issue in the repository.
