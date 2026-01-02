"""Main module for VPN config generator with refactored, streamlined logic."""

import os
import sys
import argparse

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

from processors.config_processor import process_all_configs
from utils.github_handler import GitHubHandler
from utils.logger import log, print_logs


def main(dry_run: bool = False, output_dir: str = "../githubmirror"):
    log("Starting VPN config generation...")
    file_pairs = process_all_configs(output_dir)

    if not dry_run and file_pairs:
        github_handler = GitHubHandler()
        github_handler.upload_multiple_files(file_pairs)

    print_logs()
    log("VPN config generation completed!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download configs and upload to GitHub")
    parser.add_argument("--dry-run", action="store_true", help="Only download and save locally, don't upload to GitHub")
    parser.add_argument("--output-dir", type=str, default="../githubmirror", help="Directory to save configs")
    args = parser.parse_args()

    main(dry_run=args.dry_run, output_dir=args.output_dir)
