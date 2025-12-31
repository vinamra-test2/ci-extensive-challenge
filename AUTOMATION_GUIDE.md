# GitHub Automation Guide

This repository includes automated workflows for issue management and labeling.

## 🤖 Issue Auto-Labeling

The repository automatically labels new issues based on keywords in their titles and descriptions.

### How It Works

When a new issue is opened or edited, the GitHub Actions workflow automatically analyzes the content and applies labels:

- **Bug Label**: Applied if the issue contains "error" in the title or description
- **Feature Label**: Applied if the issue contains "add" or "feature" in the title or description

### Files

- `.github/workflows/issue-labeler.yml` - GitHub Actions workflow that runs automatically
- `scripts/auto_label_issues.py` - Python script for manual or additional automation
- `scripts/requirements.txt` - Python dependencies

### Usage

#### Automatic (GitHub Actions)

The labeling happens automatically when issues are created or updated. No manual intervention required!

#### Manual (Python Script)

You can also run the labeling script manually:

```bash
# Install dependencies
pip install -r scripts/requirements.txt

# Run the script
python scripts/auto_label_issues.py --token YOUR_GITHUB_TOKEN --repo owner/repo
```

### Testing the Automation

We created three test issues to verify the automation works:

1. **Issue #1**: "error test" - Should be labeled as "bug"
2. **Issue #2**: "feature adding requirements" - Should be labeled as "feature"
3. **Issue #3**: "email feature adding error" - Should be labeled as both "bug" and "feature"

### Customization

You can easily modify the labeling rules by editing:

1. **GitHub Actions**: Edit `.github/workflows/issue-labeler.yml`
2. **Python Script**: Edit `scripts/auto_label_issues.py`

#### Adding New Keywords

To add new keywords and labels, modify the logic in either the workflow file or Python script:

```javascript
// In the GitHub Actions workflow
if (issueTitle.includes('urgent') || issueBody.includes('urgent')) {
  labelsToAdd.push('priority-high');
}
```

```python
# In the Python script
if 'urgent' in title or 'urgent' in body:
    labels_to_add.append('priority-high')
```

### Permissions

The GitHub Actions workflow requires the following permissions:
- `issues: write` - To add labels to issues

### Monitoring

You can monitor the automation by:
1. Checking the Actions tab in your repository
2. Viewing the workflow logs for each run
3. Verifying labels are applied to new issues

## 🏗️ Repository Structure

- **main branch**: Contains the primary code, workflows, and documentation
- **analysis branch**: Contains analysis-related files (analysis.txt)
- **integration branch**: Contains integration-related files (integration.txt)

## 🚀 Next Steps

1. Test the automation by creating new issues with different keywords
2. Customize the labeling rules based on your project needs
3. Add more workflows for other automation tasks
4. Set up branch protection rules if needed

## 📚 Additional Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [GitHub REST API](https://docs.github.com/en/rest)
- [PyGithub Documentation](https://pygithub.readthedocs.io/)

## 🤝 Contributing

Feel free to improve the automation by:
- Adding new keyword patterns
- Improving the labeling logic
- Adding more automation workflows
- Enhancing documentation