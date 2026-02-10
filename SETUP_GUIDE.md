# Git Installation & GitHub Setup - Quick Guide

## Install Git (Do this first!)

1. Download Git: https://git-scm.com/download/win
2. Run installer with default settings
3. Restart your terminal/PowerShell
4. Verify: `git --version`

## Configure Git (First time setup)

```powershell
# Set your name and email (used for commits)
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

## Create GitHub Repository

1. Go to: https://github.com/new
2. Repository name: `StudentPortal`
3. Choose Public or Private
4. **Don't** check any initialization boxes
5. Click "Create repository"

## Push Your Code to GitHub

After creating the repository, run these commands in PowerShell:

```powershell
# Navigate to your project
cd d:\Py_project\StudentPortal

# Initialize Git
git init

# Add all files
git add .

# Create first commit
git commit -m "Initial commit - StudentPortal ready for deployment"

# Add GitHub remote (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/StudentPortal.git

# Rename branch to main
git branch -M main

# Push to GitHub
git push -u origin main
```

## Create Render Account (Step 2)

1. Go to: **https://render.com**
2. Click **"Get Started"** or **"Sign Up"**
3. **Choose "Sign up with GitHub"** (RECOMMENDED)
   - This makes deployment easier
   - Authorizes Render to access your repositories
4. Or sign up with email if you prefer

That's it! Once you have both Git installed and a Render account, you're ready for Step 3 (actual deployment).
