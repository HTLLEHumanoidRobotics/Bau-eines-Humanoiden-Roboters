#!/usr/bin/env python3
"""
Generate GitHub issues for 3D printing parts.

This script scans the STL files in the repository and generates
issue content that can be used to create GitHub issues for tracking
the printing of each part.
"""

import os
import re
from pathlib import Path
from typing import List, Dict


# Constants
STL_BASE_PATH = 'Files/Print/pib_stl'


def parse_part_info(stl_path: str) -> Dict[str, str]:
    """
    Extract part information from STL file path.
    
    Args:
        stl_path: Path to the STL file
        
    Returns:
        Dictionary with part information
    """
    filename = Path(stl_path).stem
    parent_dir = Path(stl_path).parent.name
    
    # Extract part number and name
    # Format examples: A01-Face.stl, B25-Wire_connector.stl, D05-Finger_proximal_lower.stl
    match = re.match(r'([A-Z]\d+)(?:-([LR]))?-(.+)', filename)
    
    if match:
        part_number = match.group(1)
        side = match.group(2)  # L or R for left/right
        part_name = match.group(3).replace('_', ' ')
        
        if side:
            part_number = f"{part_number}-{side}"
            part_name = f"{part_name} ({side})"
    else:
        # Fallback if pattern doesn't match
        part_number = filename
        part_name = filename.replace('_', ' ')
    
    # Determine category from directory
    category_map = {
        'A-Head': 'Head',
        'B-Body': 'Body',
        'C-Arm': 'Arm',
        'D-Hand&Finger': 'Hand & Fingers'
    }
    category = category_map.get(parent_dir, parent_dir)
    
    return {
        'part_number': part_number,
        'part_name': part_name,
        'category': category,
        'filename': Path(stl_path).name
    }


def generate_issue_content(part_info: Dict[str, str]) -> str:
    """
    Generate GitHub issue content for a part.
    
    Args:
        part_info: Dictionary with part information
        
    Returns:
        Markdown formatted issue content
    """
    content = f"""## 🖨️ Printing Issue Template

### 🔧 Teilinformationen
- **Part Number:** {part_info['part_number']}
- **Part Name:** {part_info['part_name']}
- **Category:** {part_info['category']}
- **STL File:** `{STL_BASE_PATH}/{part_info['category']}/{part_info['filename']}`
- **Menge:** 1
- **Farbe:** 

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

### ✅ Status
- [ ] STL File überprüft
- [ ] Slicing abgeschlossen
- [ ] Druck gestartet
- [ ] Druck abgeschlossen
- [ ] Qualitätskontrolle
- [ ] Nachbearbeitung (falls erforderlich)
"""
    return content


def find_stl_files(base_path: str) -> List[str]:
    """
    Find all STL files in the print directory.
    
    Args:
        base_path: Base path to search for STL files
        
    Returns:
        List of STL file paths
    """
    stl_files = []
    print_path = Path(base_path) / STL_BASE_PATH
    
    for root, dirs, files in os.walk(print_path):
        # Skip the 'Large print parts' and 'Logo' directories
        dirs[:] = [d for d in dirs if d not in ['Large print parts', 'Logo']]
        
        for file in files:
            if file.endswith('.stl'):
                stl_files.append(os.path.join(root, file))
    
    return sorted(stl_files)


def main():
    """Main function to generate all issues."""
    # Get the repository root
    repo_root = Path(__file__).parent
    
    # Find all STL files
    stl_files = find_stl_files(str(repo_root))
    
    print(f"Found {len(stl_files)} STL files")
    
    # Create output directory
    output_dir = repo_root / 'generated_issues'
    output_dir.mkdir(exist_ok=True)
    
    # Generate issue content for each file
    issues_created = []
    
    for stl_file in stl_files:
        part_info = parse_part_info(stl_file)
        issue_content = generate_issue_content(part_info)
        
        # Create filename for the issue
        issue_filename = f"print_{part_info['part_number']}.md"
        issue_path = output_dir / issue_filename
        
        # Write issue content to file
        with open(issue_path, 'w', encoding='utf-8') as f:
            f.write(issue_content)
        
        issues_created.append({
            'title': f"Print: {part_info['part_number']} - {part_info['part_name']}",
            'file': issue_filename,
            'part': part_info
        })
    
    # Generate a summary file
    summary_path = output_dir / 'README.md'
    with open(summary_path, 'w', encoding='utf-8') as f:
        f.write("# Generated Printing Issues\n\n")
        f.write(f"Total issues generated: {len(issues_created)}\n\n")
        f.write("## How to Create Issues in GitHub\n\n")
        f.write("Since GitHub doesn't support bulk issue creation via the web interface, ")
        f.write("you have several options:\n\n")
        f.write("### Option 1: Manual Creation (Recommended for small batches)\n")
        f.write("1. Go to the Issues tab in your GitHub repository\n")
        f.write("2. Click 'New Issue'\n")
        f.write("3. Copy the content from the corresponding .md file in this directory\n")
        f.write("4. Paste it into the issue description\n")
        f.write("5. Add the title and labels\n\n")
        f.write("### Option 2: GitHub CLI (Recommended for bulk creation)\n")
        f.write("If you have the GitHub CLI installed, you can run:\n\n")
        f.write("```bash\n")
        f.write("# Example for creating all issues at once\n")
        f.write("cd generated_issues\n")
        f.write("for file in print_*.md; do\n")
        f.write('  TITLE=$(echo $file | sed \'s/print_/Print: /\' | sed \'s/.md//\')\n')
        f.write('  gh issue create --title "$TITLE" --body-file "$file" --label "printing,3d-print"\n')
        f.write("done\n")
        f.write("```\n\n")
        f.write("### Option 3: GitHub API\n")
        f.write("Use the GitHub REST API with a personal access token to create issues programmatically.\n\n")
        f.write("## Issues by Category\n\n")
        
        # Group by category
        by_category = {}
        for issue in issues_created:
            category = issue['part']['category']
            if category not in by_category:
                by_category[category] = []
            by_category[category].append(issue)
        
        for category, category_issues in sorted(by_category.items()):
            f.write(f"### {category} ({len(category_issues)} parts)\n\n")
            for issue in category_issues:
                f.write(f"- **{issue['title']}** → `{issue['file']}`\n")
            f.write("\n")
    
    print(f"\n✅ Successfully generated {len(issues_created)} issue files in 'generated_issues/' directory")
    print(f"📄 See generated_issues/README.md for instructions on how to create these issues in GitHub")
    
    # Also create a bash script for easy bulk creation
    script_path = output_dir / 'create_all_issues.sh'
    with open(script_path, 'w', encoding='utf-8') as f:
        f.write("#!/bin/bash\n")
        f.write("# Script to create all printing issues using GitHub CLI\n")
        f.write("# Usage: ./create_all_issues.sh\n")
        f.write("# Prerequisites: GitHub CLI (gh) must be installed and authenticated\n\n")
        f.write("set -e\n\n")
        f.write("if ! command -v gh &> /dev/null; then\n")
        f.write('    echo "Error: GitHub CLI (gh) is not installed."\n')
        f.write('    echo "Install it from: https://cli.github.com/"\n')
        f.write("    exit 1\n")
        f.write("fi\n\n")
        f.write('echo "Creating printing issues..."\n\n')
        
        for issue in issues_created:
            safe_title = issue['title'].replace("'", "'\\''")
            f.write(f"echo 'Creating: {safe_title}'\n")
            f.write(f"gh issue create --title '{safe_title}' ")
            f.write(f"--body-file '{issue['file']}' ")
            f.write(f"--label 'printing,3d-print,{issue['part']['category'].lower()}'\n\n")
        
        f.write('echo ""\n')
        f.write(f'echo "✅ Successfully created {len(issues_created)} issues!"\n')
    
    # Make script executable
    os.chmod(script_path, 0o755)
    print(f"📝 Created bash script: generated_issues/create_all_issues.sh")


if __name__ == '__main__':
    main()
