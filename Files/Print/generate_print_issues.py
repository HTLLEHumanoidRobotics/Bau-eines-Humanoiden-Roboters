#!/usr/bin/env python3
"""
Script to generate printing issue data for all robot parts.

This script scans the STL files and generates:
1. A markdown file with issue templates for each part
2. A CSV file for batch processing
3. A JSON file for automated issue creation via API
"""

import os
import json
import csv
from pathlib import Path
from typing import List, Dict, Tuple

# Base directory
SCRIPT_DIR = Path(__file__).parent
STL_DIR = SCRIPT_DIR / "pib_stl"

# Part categorization
PART_CATEGORIES = {
    'A': 'A-Head (Face/Neck)',
    'B': 'B-Body (Ribcage)',
    'C': 'C-Arm (Shoulder/Elbow/Forearm)',
    'D': 'D-Hand&Finger'
}

# Default colors by category
DEFAULT_COLORS = {
    'A': 'Weiß',
    'B': 'Weiß',
    'C': 'Weiß',
    'D': 'Schwarz'
}


def parse_stl_filename(filename: str) -> Tuple[str, str]:
    """
    Parse STL filename to extract part number and name.
    
    Args:
        filename: STL filename without extension
        
    Returns:
        Tuple of (part_number, part_name)
    """
    # Remove .stl extension if present
    if filename.endswith('.stl'):
        filename = filename[:-4]
    
    # Skip pib branding parts
    if filename.startswith('pib -'):
        return None, None
    
    # Split on first hyphen to get part number and name
    parts = filename.split('-', 1)
    if len(parts) == 2:
        part_number = parts[0]
        part_name = parts[1].replace('_', ' ')
        return part_number, part_name
    
    return None, None


def get_part_category(part_number: str) -> str:
    """Get category description for a part number."""
    if not part_number:
        return 'Unknown'
    
    prefix = part_number[0]
    return PART_CATEGORIES.get(prefix, 'Unknown')


def get_default_color(part_number: str) -> str:
    """Get default color for a part number."""
    if not part_number:
        return 'Weiß'
    
    prefix = part_number[0]
    return DEFAULT_COLORS.get(prefix, 'Weiß')


def scan_stl_files() -> List[Dict[str, str]]:
    """
    Scan all STL files and extract part information.
    
    Returns:
        List of dictionaries with part information
    """
    parts = []
    
    for stl_file in STL_DIR.rglob("*.stl"):
        filename = stl_file.stem
        part_number, part_name = parse_stl_filename(filename)
        
        if part_number and part_name:
            parts.append({
                'part_number': part_number,
                'part_name': part_name,
                'category': get_part_category(part_number),
                'color': get_default_color(part_number),
                'quantity': 1,
                'file_path': str(stl_file.relative_to(SCRIPT_DIR))
            })
    
    # Sort by part number
    parts.sort(key=lambda x: x['part_number'])
    
    return parts


def generate_markdown_issues(parts: List[Dict[str, str]], output_file: Path):
    """Generate a markdown file with all issue templates."""
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# 🖨️ Printing Issues - All Parts\n\n")
        f.write("This file contains issue templates for all robot parts that need to be printed.\n")
        f.write(f"Total parts: {len(parts)}\n\n")
        f.write("---\n\n")
        
        current_category = None
        
        for part in parts:
            # Add category header
            if part['category'] != current_category:
                current_category = part['category']
                f.write(f"\n## {current_category}\n\n")
            
            # Write issue template
            f.write(f"### Issue: Print [{part['part_number']}]\n\n")
            f.write("```markdown\n")
            f.write(f"Title: Print: [{part['part_number']}]\n\n")
            f.write("## 🖨️ Printing Issue Template\n\n")
            f.write("### 🔧 Teilinformationen\n")
            f.write(f"- **Part Number:** {part['part_number']}\n")
            f.write(f"- **Part Name:** {part['part_name']}\n")
            f.write(f"- **Menge:** {part['quantity']}\n")
            f.write(f"- **Farbe:** {part['color']}\n\n")
            f.write("### ⏱️ Zeit\n")
            f.write("- **Geplante Druckzeit:** ___ h ___ min\n")
            f.write("- **Tatsächliche Druckzeit:** ___ h ___ min\n\n")
            f.write("### 📒 Notizen\n")
            f.write("- \n\n")
            f.write("### ⚙️ Druckeinstellungen (relevant)\n")
            f.write("- Drucker:\n")
            f.write("- Material / Filament:\n")
            f.write("- Nozzle / Layerhöhe:\n")
            f.write("- Infill / Support:\n")
            f.write("```\n\n")
            f.write("---\n\n")


def generate_csv(parts: List[Dict[str, str]], output_file: Path):
    """Generate a CSV file for batch processing."""
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['part_number', 'part_name', 'category', 'color', 'quantity', 'file_path']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        
        writer.writeheader()
        for part in parts:
            writer.writerow(part)


def generate_json(parts: List[Dict[str, str]], output_file: Path):
    """Generate a JSON file for automated issue creation."""
    issues = []
    
    for part in parts:
        issue = {
            'title': f"Print: [{part['part_number']}]",
            'labels': ['printing', part['category'].split()[0]],
            'body': f"""## 🖨️ Printing Issue Template

### 🔧 Teilinformationen
- **Part Number:** {part['part_number']}
- **Part Name:** {part['part_name']}
- **Menge:** {part['quantity']}
- **Farbe:** {part['color']}

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

---
**File:** `{part['file_path']}`
"""
        }
        issues.append(issue)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump({'issues': issues, 'count': len(issues)}, f, indent=2, ensure_ascii=False)


def generate_summary(parts: List[Dict[str, str]], output_file: Path):
    """Generate a summary report."""
    # Count by category
    category_counts = {}
    for part in parts:
        cat = part['category']
        category_counts[cat] = category_counts.get(cat, 0) + 1
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# 🖨️ Printing Parts Summary\n\n")
        f.write(f"**Total Parts:** {len(parts)}\n\n")
        f.write("## Parts by Category\n\n")
        
        for category in sorted(category_counts.keys()):
            count = category_counts[category]
            f.write(f"- **{category}:** {count} parts\n")
        
        f.write("\n## All Parts List\n\n")
        f.write("| Part Number | Part Name | Category | Color |\n")
        f.write("|-------------|-----------|----------|-------|\n")
        
        for part in parts:
            f.write(f"| {part['part_number']} | {part['part_name']} | "
                   f"{part['category']} | {part['color']} |\n")


def main():
    """Main function."""
    print("🔍 Scanning STL files...")
    parts = scan_stl_files()
    print(f"✅ Found {len(parts)} parts")
    
    # Generate output files
    print("\n📝 Generating output files...")
    
    output_dir = SCRIPT_DIR / "issue_templates"
    output_dir.mkdir(exist_ok=True)
    
    # Generate markdown with all issues
    md_file = output_dir / "all_printing_issues.md"
    generate_markdown_issues(parts, md_file)
    print(f"✅ Created: {md_file}")
    
    # Generate CSV
    csv_file = output_dir / "printing_parts.csv"
    generate_csv(parts, csv_file)
    print(f"✅ Created: {csv_file}")
    
    # Generate JSON for API
    json_file = output_dir / "printing_issues.json"
    generate_json(parts, json_file)
    print(f"✅ Created: {json_file}")
    
    # Generate summary
    summary_file = output_dir / "printing_summary.md"
    generate_summary(parts, summary_file)
    print(f"✅ Created: {summary_file}")
    
    print("\n✅ All files generated successfully!")
    print(f"\n📊 Summary:")
    print(f"   Total parts: {len(parts)}")
    
    # Print category breakdown
    category_counts = {}
    for part in parts:
        cat = part['category']
        category_counts[cat] = category_counts.get(cat, 0) + 1
    
    for category in sorted(category_counts.keys()):
        print(f"   {category}: {category_counts[category]} parts")


if __name__ == "__main__":
    main()
