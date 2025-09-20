# 📘 RPA Project Estimator - Deployment & Running Instructions

## Quick Start Guide

This document provides step-by-step instructions for running the RPA Project Estimator application either locally on your computer or through Streamlit Cloud.

---

## 🖥️ OPTION 1: Running Locally on Your Computer

### Prerequisites
- **Python 3.8 or higher** installed ([Download Python](https://www.python.org/downloads/))
- **Git** installed ([Download Git](https://git-scm.com/downloads/)) - Optional
- **Web browser** (Chrome, Firefox, Edge, Safari)

### Method A: From GitHub (Recommended)

#### Step 1: Get the Code
Open Command Prompt (CMD) or PowerShell and run:

```cmd
# Clone the repository from GitHub
git clone https://github.com/DanielaRosenn/rpa-project-estimator.git

# Navigate into the project folder
cd rpa-project-estimator
```

**Alternative: Download Without Git**
1. Go to https://github.com/DanielaRosenn/rpa-project-estimator
2. Click the green "Code" button → "Download ZIP"
3. Extract the ZIP file to your desired location
4. Open CMD/PowerShell and navigate to the extracted folder

#### Step 2: Set Up Python Environment

```cmd
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# For Windows:
venv\Scripts\activate

# For Mac/Linux:
source venv/bin/activate
```

**You should see `(venv)` appear in your command prompt**

#### Step 3: Install Required Packages

```cmd
# Install all dependencies
pip install -r requirements.txt
```

This installs:
- streamlit (web interface)
- pandas (data handling)
- openpyxl (Excel support)
- plotly (visualizations)
- xlsxwriter (Excel creation)
- python-dateutil (date handling)

#### Step 4: Run the Application

```cmd
# Start the Streamlit app
streamlit run app.py
```

#### Step 5: Access the Application
- Your browser should open automatically
- If not, open your browser and go to: **http://localhost:8501**
- The application is now running locally!

#### Step 6: Stop the Application
- Press `Ctrl + C` in the command prompt
- Or close the command prompt window

---

### Method B: From Azure DevOps

#### Step 1: Clone from Azure DevOps
```cmd
# Clone from Azure DevOps
git clone https://uipathcato@dev.azure.com/uipathcato/uipath/_git/rpa_project_estimator

# Navigate to the folder
cd rpa_project_estimator
```

#### Step 2-6: Follow the same steps as Method A above

---

### 🚀 Quick Start for Daily Use

Once you've set up the application once, daily use is simple:

#### Create a Desktop Shortcut (Windows)

1. Create a new file called `Run_RPA_Estimator.bat` on your Desktop
2. Add this content:

```batch
@echo off
echo Starting RPA Project Estimator...
cd /d "C:\path\to\your\rpa-project-estimator"
call venv\Scripts\activate
start http://localhost:8501
streamlit run app.py
pause
```

3. Replace `C:\path\to\your\rpa-project-estimator` with your actual path
4. Save the file
5. Double-click to run anytime!

#### For Mac/Linux Users

Create a shell script `run_app.sh`:

```bash
#!/bin/bash
cd ~/path/to/rpa-project-estimator
source venv/bin/activate
streamlit run app.py
```

Make it executable: `chmod +x run_app.sh`
Run it: `./run_app.sh`

---

### 📁 Understanding Local Files

When running locally:

| File/Folder | Purpose | Can Delete? |
|------------|---------|-------------|
| `app.py` | Main application | ❌ No |
| `config.py` | Settings & constants | ❌ No |
| `calculations.py` | Business logic | ❌ No |
| `requirements.txt` | Package list | ❌ No |
| `venv/` | Python packages | ⚠️ Can recreate |
| `rpa_projects_database.xlsx` | Your project data | ⚠️ Backup first! |
| `README.md` | Documentation | ✅ Yes |

**Important**: The Excel file (`rpa_projects_database.xlsx`) contains all your project data. Back it up regularly!

---

### 🔧 Troubleshooting Local Installation

| Problem | Solution |
|---------|----------|
| **"python is not recognized"** | Install Python from python.org, or try `python3` or `py` |
| **"streamlit is not recognized"** | Activate virtual environment: `venv\Scripts\activate` |
| **"No module named streamlit"** | Run: `pip install -r requirements.txt` |
| **Port 8501 already in use** | Run on different port: `streamlit run app.py --server.port 8502` |
| **Excel file not created** | The file creates automatically when you save your first project |
| **Browser doesn't open** | Manually go to: http://localhost:8501 |

---

## ☁️ OPTION 2: Running Through Streamlit Cloud (Web-Based)

### Overview
Streamlit Cloud hosts your application online, making it accessible from anywhere without installation.

### Prerequisites
- **GitHub account** (free at [github.com](https://github.com))
- **Streamlit account** (free at [streamlit.io](https://streamlit.io))
- Your code in a GitHub repository

### Step-by-Step Deployment

#### Step 1: Prepare Your GitHub Repository

1. Ensure your code is pushed to GitHub:
   - Repository: https://github.com/DanielaRosenn/rpa-project-estimator
   - Must be **Public** for free hosting

2. Required files in repository:
   - ✅ `app.py`
   - ✅ `config.py`
   - ✅ `calculations.py`
   - ✅ `requirements.txt`
   - ✅ `README.md` (optional but recommended)
   - ❌ Don't include: `.venv/`, `.git/`, `*.xlsx` files

#### Step 2: Sign Up for Streamlit Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Click "Sign up"
3. Choose "Continue with GitHub"
4. Authorize Streamlit to access your GitHub

#### Step 3: Deploy Your Application

1. Click "New app" button
2. Fill in the deployment form:
   ```
   Repository: DanielaRosenn/rpa-project-estimator
   Branch: main
   Main file path: app.py
   ```
3. (Optional) Choose a custom URL:
   - Example: `rpa-estimator-2026`
   - Results in: `https://rpa-estimator-2026.streamlit.app`
4. Click "Deploy!"

#### Step 4: Wait for Deployment
- Takes 2-5 minutes
- You'll see build logs
- When ready: "Your app is live! 🎈"

#### Step 5: Access Your Application
- Your app URL: `https://[your-app-name].streamlit.app`
- Share this URL with anyone!
- No installation required for users

---

### 🔄 Updating Your Streamlit Cloud App

When you want to update the application:

1. **Make changes locally**
2. **Test locally** (run `streamlit run app.py`)
3. **Push to GitHub**:
   ```cmd
   git add .
   git commit -m "Description of changes"
   git push
   ```
4. **Automatic deployment** - Streamlit detects changes and redeploys (1-2 minutes)

---

### ⚙️ Streamlit Cloud Settings

Access your app dashboard at [share.streamlit.io](https://share.streamlit.io):

| Setting | Purpose |
|---------|---------|
| **Secrets Management** | Add API keys or passwords securely |
| **Advanced Settings** | Python version, custom domains |
| **App URL** | Change your app's URL |
| **Viewers** | See usage statistics |
| **Logs** | Debug issues |
| **Reboot App** | Restart if stuck |

---

### 📊 Comparison: Local vs Streamlit Cloud

| Feature | Local | Streamlit Cloud |
|---------|-------|-----------------|
| **Installation Required** | Yes (Python, packages) | No (just browser) |
| **Accessibility** | Only on your computer | Anywhere with internet |
| **URL** | http://localhost:8501 | https://yourapp.streamlit.app |
| **Data Storage** | Permanent (local Excel) | Temporary (resets on restart) |
| **Updates** | Manual | Automatic from GitHub |
| **Cost** | Free | Free (with limits) |
| **Privacy** | Complete control | Public repo required |
| **Performance** | Faster | Depends on internet |
| **Collaboration** | No | Yes (share URL) |
| **Uptime** | When you run it | 24/7 |

---

## 🎯 Which Option Should You Choose?

### Choose **Local** if you:
- Want complete data privacy
- Need permanent data storage
- Work mostly from one computer
- Have sensitive company data
- Don't need to share with many people
- Want fastest performance

### Choose **Streamlit Cloud** if you:
- Need to share with multiple people
- Want access from any device
- Don't want users to install anything
- Need 24/7 availability
- Want automatic updates
- Have non-sensitive data

### Use **Both** (Recommended):
- Develop and test locally
- Deploy to Streamlit Cloud for sharing
- Keep sensitive projects local only

---

## 💡 Pro Tips

### For Local Running:
1. **Create a backup routine**: Copy your Excel file weekly
2. **Use version control**: Commit changes to Git regularly
3. **Document changes**: Update README when adding features
4. **Test before sharing**: Run locally before pushing to cloud

### For Streamlit Cloud:
1. **Monitor usage**: Check dashboard for user statistics
2. **Set up secrets**: Never put passwords in code
3. **Use caching**: Add `@st.cache_data` for slow functions
4. **Optimize resources**: Free tier has 1GB limit

---

## 📞 Getting Help

### Resources:
- **Streamlit Documentation**: [docs.streamlit.io](https://docs.streamlit.io)
- **GitHub Repository**: [github.com/DanielaRosenn/rpa-project-estimator](https://github.com/DanielaRosenn/rpa-project-estimator)
- **Azure DevOps**: Internal repository for Cato team

### Common Commands Reference:

```cmd
# Local Development
python -m venv venv              # Create virtual environment
venv\Scripts\activate            # Activate (Windows)
pip install -r requirements.txt  # Install packages
streamlit run app.py            # Run application
Ctrl+C                          # Stop application

# Git Commands
git status                      # Check changes
git add .                       # Stage all changes
git commit -m "message"         # Commit changes
git push                        # Upload to GitHub
git pull                        # Download latest changes

# Streamlit Commands
streamlit run app.py --server.port 8502  # Different port
streamlit run app.py --help              # See all options
streamlit cache clear                    # Clear cache
```

---

## 🎉 You're Ready!

You now have everything you need to run the RPA Project Estimator:
- **Locally** for development and private use
- **On Streamlit Cloud** for sharing with others

Remember:
- Local = Privacy + Control
- Cloud = Accessibility + Sharing

Choose based on your needs, or use both!

---

*Last Updated: January 2025*
*Version: 1.0*