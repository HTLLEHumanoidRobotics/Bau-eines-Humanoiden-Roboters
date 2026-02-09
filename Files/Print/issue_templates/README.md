# 🖨️ Print Issue Templates

This directory contains automatically generated templates for creating GitHub issues for all parts that need to be printed.

## 📁 Files

### 1. **all_printing_issues.md**
Contains formatted issue templates for all 92 parts, organized by category. You can copy and paste these directly into GitHub when creating new issues manually.

**Usage:**
- Open the file
- Find the part you want to create an issue for
- Copy the markdown template (between the ``` markers)
- Create a new issue on GitHub
- Paste the template and fill in the details

### 2. **printing_parts.csv**
A CSV file with all part information suitable for spreadsheet applications or batch processing.

**Columns:**
- `part_number`: The part identifier (e.g., A01, B42)
- `part_name`: Human-readable part name
- `category`: Part category (A-Head, B-Body, C-Arm, D-Hand&Finger)
- `color`: Default color for the part
- `quantity`: Number of this part needed (default: 1)
- `file_path`: Path to the STL file

**Usage:**
- Import into Excel/LibreOffice for tracking
- Use for planning and scheduling prints
- Export to other formats as needed

### 3. **printing_issues.json**
A JSON file formatted for automated issue creation via the GitHub API.

**Structure:**
```json
{
  "issues": [
    {
      "title": "Print: [A01]",
      "labels": ["printing", "A-Head"],
      "body": "... issue template content ..."
    }
  ],
  "count": 92
}
```

**Usage:**
- Use with GitHub CLI (`gh`) for batch issue creation
- Integrate with automation scripts
- Import into issue tracking tools

### 4. **printing_summary.md**
A comprehensive summary showing all parts organized in a table format.

**Contents:**
- Total part count
- Parts by category breakdown
- Complete table of all parts with their details

**Usage:**
- Quick reference for project overview
- Planning and resource allocation
- Progress tracking

## 🔄 Regenerating Templates

If you need to regenerate these templates (e.g., after adding new STL files):

```bash
cd Files/Print
python3 generate_print_issues.py
```

This will scan all STL files and regenerate all template files.

## 📊 Statistics

- **Total Parts:** 92
- **A-Head (Face/Neck):** 17 parts
- **B-Body (Ribcage):** 28 parts
- **C-Arm (Shoulder/Elbow/Forearm):** 35 parts
- **D-Hand&Finger:** 12 parts

## 🚀 Batch Issue Creation

### Using GitHub CLI

To create all issues at once using the GitHub CLI:

```bash
# Install GitHub CLI if not already installed
# https://cli.github.com/

# Authenticate
gh auth login

# Create issues from JSON (requires gh-issue-batch extension or custom script)
# See create_issues_batch.sh for automated batch creation
```

### Manual Creation

For manual issue creation:
1. Open `all_printing_issues.md`
2. Navigate to the part you want to print
3. Copy the markdown template for that part
4. Go to GitHub Issues → New Issue
5. Select the "Printing_Issue" template
6. Paste the pre-filled content
7. Adjust any details as needed
8. Submit the issue

## 🎯 Workflow Integration

These templates integrate with the printing workflow documented in `/Files/Print/README.md`:

1. **Before Printing:** Create an issue from these templates
2. **During Printing:** Update the issue with progress
3. **After Printing:** Update PRINT_LOG.md and close the issue

## 🔗 Related Files

- [Print Tracking Log](../PRINT_LOG.md)
- [Print Directory README](../README.md)
- [Issue Template](.github/ISSUE_TEMPLATE/printing_issue.md)
- [Generation Script](../generate_print_issues.py)

---

**Generated on:** 2026-02-09  
**Last Updated:** 2026-02-09
