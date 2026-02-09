# 🖨️ 3D Printing Documentation

This directory contains all documentation and files related to 3D printing the humanoid robot parts.

## Directory Structure

```
Print/
├── PRINT_LOG.md              # Main tracking log for all printed parts
├── README.md                 # This file - overview and instructions
├── Materiallist.xlsx         # Material requirements and inventory
├── Media/                    # Images and documentation of prints
│   └── pictures/             # Photos of completed prints
├── pib_printingInstructions/ # Official printing instructions PDFs
└── pib_stl/                  # STL files organized by section
    ├── A-Head/               # Head and neck parts
    ├── B-Body/               # Body and ribcage parts
    ├── C-Arm/                # Arm parts
    └── D-Hand&Finger/        # Hand and finger parts
```

## 📋 Workflow

### 1. Creating a Print Issue

#### Option A: Using Pre-Generated Templates (Recommended)
1. Navigate to `issue_templates/all_printing_issues.md`
2. Find the part you want to print
3. Copy the pre-filled template for that part
4. Go to GitHub Issues → New Issue
5. Paste the template and adjust details as needed
6. Submit the issue

#### Option B: Batch Creation
Use the automated script to create all issues at once:
```bash
cd Files/Print
./create_issues_batch.sh
```
See [issue_templates/README.md](issue_templates/README.md) for details.

#### Option C: Manual Creation
1. Go to GitHub Issues
2. Click "New Issue"
3. Select the "Printing_Issue" template
4. Fill in the part details (Part Number, Name, etc.)
5. Submit the issue

### 2. During Printing
- Monitor the print progress
- Take photos of the print for documentation
- Note any issues or observations

### 3. After Printing
1. Update the issue with actual print time
2. Add photos to `Media/pictures/` directory
3. Update `PRINT_LOG.md` with the completed print details
4. Close the issue

## 📊 Tracking Completed Prints

All completed prints are documented in [PRINT_LOG.md](PRINT_LOG.md). This file includes:
- Part identification (Number, Name)
- Planned vs. actual print times
- Print settings used
- Material and color information
- Additional notes and observations

## 📁 Files Overview

### STL Files
- Located in `pib_stl/` directory
- Organized by robot section (A-Head, B-Body, C-Arm, D-Hand&Finger)
- Original files from the pib (printable robot) project

### Printing Instructions
- PDFs in `pib_printingInstructions/` directory
- Contains official instructions for each major section
- Includes recommended settings and assembly notes

### Material List
- Excel file `Materiallist.xlsx`
- Tracks material requirements
- Helps manage inventory and ordering

## 🎯 Part Numbering System

- **A-series**: Head and Neck parts (A01-A83)
- **B-series**: Body and Ribcage parts
- **C-series**: Arm parts
- **D-series**: Hand and Finger parts

## 📝 Tips for Successful Prints

1. Always check the printing instructions PDF before starting
2. Verify printer settings match the requirements
3. Plan for longer print times than estimated
4. Document any deviations or issues
5. Take photos of completed prints for reference

## 🔗 Related Resources

- [Printing Checklist](../../printing_checklist-pib_4.pdf)
- [GitHub Issue Template](../../.github/ISSUE_TEMPLATE/printing_issue.md)
- [Pre-Generated Issue Templates](issue_templates/) - Ready-to-use templates for all 92 parts
- [Issue Generation Script](generate_print_issues.py) - Regenerate templates if needed
- [Project Documentation](../../Diplomarbeit/)

## 🤖 Automation Tools

### Issue Generation
- **`generate_print_issues.py`**: Python script that scans all STL files and generates issue templates
- **`create_issues_batch.sh`**: Bash script for batch issue creation using GitHub CLI
- **`issue_templates/`**: Directory containing all generated templates and documentation

Run the generation script to update templates:
```bash
python3 generate_print_issues.py
```

---

**Last Updated:** 2026-02-09  
**Maintained by:** HTL Leoben Humanoid Robotics Team
