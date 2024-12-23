import os

# Define the root directory and project structure
root_dir = "data-sceince-projects"
projects = {
    "eye_tracking_project": ["data", "notebooks", "src"],
    "MEG": ["data", "notebooks", "src"]
}

# Create the root directory
os.makedirs(root_dir, exist_ok=True)

# Create project directories and subdirectories
for project, subdirs in projects.items():
    project_path = os.path.join(root_dir, project)
    os.makedirs(project_path, exist_ok=True)
    
    # Create subdirectories within each project
    for subdir in subdirs:
        os.makedirs(os.path.join(project_path, subdir), exist_ok=True)
    
    # Create a README.md file for each project
    readme_path = os.path.join(project_path, "README.md")
    with open(readme_path, "w") as readme_file:
        readme_file.write(f"# {project.replace('_', ' ').title()}\n\nDescription of {project}.\n")

# Create a root-level README.md
root_readme_path = os.path.join(root_dir, "README.md")
with open(root_readme_path, "w") as root_readme:
    root_readme.write(
        "# Repository Name\n\n"
        "This repository contains multiple projects, including:\n\n"
        "1. **Eye-Tracking Project**: Description here.\n"
        "2. **MEG Project**: Description here.\n"
    )

print(f"Project structure created successfully in '{root_dir}'")