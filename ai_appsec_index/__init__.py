"""AI AppSec Index - The definitive open-source reference for AI-augmented application security."""

import json
import csv
import os
from pathlib import Path

__version__ = "1.0.0"
__author__ = "Alpha One Index"

DATA_DIR = Path(__file__).parent.parent / "data"
KAGGLE_DIR = Path(__file__).parent.parent / "kaggle"


def load_dataset(name):
    """Load a JSON dataset by name.
    
    Args:
        name: One of 'remediation-leaderboard', 'aspm-capability-matrix',
              'ai-code-vulnerabilities', 'cra-compliance-map',
              'false-positive-benchmarks', 'cra-timeline'
    
    Returns:
        dict: The parsed JSON dataset
    """
    filepath = DATA_DIR / f"{name}.json"
    if not filepath.exists():
        raise FileNotFoundError(f"Dataset '{name}' not found at {filepath}")
    with open(filepath, "r") as f:
        return json.load(f)


def load_csv(name):
    """Load a CSV dataset by name.
    
    Args:
        name: CSV filename without extension
    
    Returns:
        list[dict]: List of row dictionaries
    """
    filepath = KAGGLE_DIR / f"{name}.csv"
    if not filepath.exists():
        raise FileNotFoundError(f"CSV '{name}' not found at {filepath}")
    with open(filepath, "r") as f:
        return list(csv.DictReader(f))


def list_datasets():
    """List all available datasets."""
    datasets = []
    if DATA_DIR.exists():
        datasets.extend([f.stem for f in DATA_DIR.glob("*.json")])
    return sorted(datasets)


def get_cve_count():
    """Get the total number of tracked CVEs."""
    data = load_dataset("ai-code-vulnerabilities")
    return len(data.get("vulnerabilities", []))


def get_aspm_vendors():
    """Get list of ASPM vendors in the matrix."""
    data = load_dataset("aspm-capability-matrix")
    return [t["tool"] for t in data.get("tools", [])]
