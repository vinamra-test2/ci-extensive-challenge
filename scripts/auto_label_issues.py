#!/usr/bin/env python3
"""
Automatic Issue Labeler Script

This script automatically labels GitHub issues based on keywords in their titles and descriptions.
- Labels issues with "bug" if they contain "error"
- Labels issues with "feature" if they contain "add" or "feature"

Usage:
    python auto_label_issues.py --token YOUR_GITHUB_TOKEN --repo owner/repo
"""

import argparse
import os
import sys
from github import Github
from github.GithubException import UnknownObjectException

def auto_label_issues(github_token, repository):
    """
    Automatically label issues in a GitHub repository based on keywords.
    
    Args:
        github_token (str): GitHub personal access token
        repository (str): Repository in format "owner/repo"
    """
    try:
        # Initialize GitHub client
        g = Github(github_token)
        repo = g.get_repo(repository)
        
        print(f"Processing issues in repository: {repository}")
        
        # Get all open issues
        open_issues = repo.get_issues(state='open')
        
        labeled_count = 0
        
        for issue in open_issues:
            if issue.pull_request:  # Skip pull requests
                continue
                
            print(f"\nProcessing issue #{issue.number}: {issue.title}")
            
            # Get issue title and body (convert to lowercase for case-insensitive matching)
            title = issue.title.lower()
            body = (issue.body or "").lower()
            
            # Determine which labels to add
            labels_to_add = []
            
            # Check for bug-related keywords
            if 'error' in title or 'error' in body:
                labels_to_add.append('bug')
            
            # Check for feature-related keywords
            if ('add' in title or 'add' in body or 
                'feature' in title or 'feature' in body):
                labels_to_add.append('feature')
            
            # Add labels if any were found
            if labels_to_add:
                try:
                    # Check if labels exist, create them if they don't
                    existing_labels = [label.name for label in repo.get_labels()]
                    
                    for label_name in labels_to_add:
                        if label_name not in existing_labels:
                            try:
                                repo.create_label(
                                    name=label_name,
                                    color="ff0000" if label_name == "bug" else "00ff00",
                                    description=f"Automatically created {label_name} label"
                                )
                                print(f"Created new label: {label_name}")
                            except Exception as e:
                                print(f"Could not create label {label_name}: {e}")
                    
                    # Add labels to issue
                    issue.add_to_labels(*labels_to_add)
                    print(f"✅ Added labels: {', '.join(labels_to_add)}")
                    labeled_count += 1
                    
                except Exception as e:
                    print(f"❌ Error adding labels: {e}")
            else:
                print("No matching keywords found")
        
        print(f"\n🏷️  Completed! Labeled {labeled_count} issues.")
        
    except UnknownObjectException:
        print(f"❌ Repository '{repository}' not found or not accessible")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Automatically label GitHub issues based on keywords")
    parser.add_argument("--token", required=True, help="GitHub personal access token")
    parser.add_argument("--repo", required=True, help="Repository in format 'owner/repo'")
    
    args = parser.parse_args()
    
    auto_label_issues(args.token, args.repo)

if __name__ == "__main__":
    main()