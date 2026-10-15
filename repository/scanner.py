
from pathlib import Path


def scan_repository(repo_path: str) -> dict:
    """List files and directories in a repository."""

    root = Path(repo_path).resolve()

    if not root.exists():
        raise FileNotFoundError("Repository path does not exist.")

    if not root.is_dir():
        raise NotADirectoryError("The provided path is not a directory.")

    files = []
    directories = []

    ignored = {".git", ".venv", "__pycache__", "node_modules"}

    for path in root.rglob("*"):
        if any(part in ignored for part in path.parts):
            continue

        if path.is_file():
            files.append(str(path.relative_to(root)))
        elif path.is_dir():
            directories.append(str(path.relative_to(root)))

    return {
        "repository": str(root),
        "file_count": len(files),
        "directory_count": len(directories),
        "files": sorted(files),
        "directories": sorted(directories),
    }