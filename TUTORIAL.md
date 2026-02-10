# Hands-On Tutorial Guide

## Overview

This tutorial will teach you the essential tools for modern scientific software development: VS Code, Git, and GitHub. By the end, you'll be comfortable writing, versioning, and collaborating on code.

---

## Part 1: Getting Set Up (15 minutes)

### 1.1 Install Software

Make sure you have:
- [ ] Python 3.7+ installed
- [ ] Git installed
- [ ] VS Code installed
- [ ] GitHub account created

### 1.2 Clone the Repository

```bash
git clone https://github.com/JohanvdWesthuizen/qpl_handson_demo.git
cd qpl_handson_demo
```

### 1.3 Open in VS Code

```bash
code .
```

### 1.4 Install Dependencies

In the VS Code terminal:
```bash
pip install -r requirements.txt
```

---

## Part 2: Running Python Scripts in VS Code (20 minutes)

### 2.1 Run Your First Script

1. Open `basic_physics.py` in VS Code
2. Read through the code to understand what it does
3. Run it by clicking the "Run" button (▶️) or press `F5`
4. Observe the output in the terminal

### 2.2 Make Your First Edit

**Exercise**: Modify the values in `basic_physics.py`

1. Find the `main()` function
2. Change the `distance` value from 100 to 200
3. Change the `mass` value from 10 to 25
4. Run the script again and observe the changes

### 2.3 Explore Projectile Motion

1. Open `projectile_motion.py`
2. Run the script to see projectile calculations
3. **Challenge**: Add a new angle (e.g., 75 degrees) to the `angles` list
4. Run again and see the new results

### 2.4 Data Visualization

1. Open `data_analysis.py`
2. Run the script
3. It will generate a plot saved as `motion_analysis.png`
4. Open the generated image to view your plots

---

## Part 3: Git Basics (30 minutes)

### 3.1 Check Git Status

```bash
git status
```

You should see your modified files listed.

### 3.2 View Your Changes

```bash
git diff basic_physics.py
```

This shows the exact lines you changed.

### 3.3 Stage Your Changes

```bash
git add basic_physics.py
```

Or stage all changes:
```bash
git add .
```

### 3.4 Commit Your Changes

```bash
git commit -m "Modified distance and mass values in basic physics script"
```

**Good commit messages are:**
- Short and descriptive
- Written in present tense
- Explain *what* and *why*

### 3.5 View Commit History

```bash
git log --oneline
```

---

## Part 4: Branching and Experimenting (25 minutes)

### 4.1 Create a New Branch

```bash
git checkout -b experiment-projectile
```

### 4.2 Make Experimental Changes

1. Open `projectile_motion.py`
2. Change the `initial_velocity` from 20 to 50
3. Add more angles to test
4. Run the script to verify it works

### 4.3 Commit Your Experiment

```bash
git add projectile_motion.py
git commit -m "Experimented with higher initial velocity"
```

### 4.4 Switch Between Branches

```bash
git checkout main
```

Notice that your changes are gone! Now switch back:

```bash
git checkout experiment-projectile
```

Your changes are back!

### 4.5 Merge Your Changes

```bash
git checkout main
git merge experiment-projectile
```

---

## Part 5: Working with GitHub (30 minutes)

### 5.1 Connect to GitHub

If you haven't already:
```bash
git remote -v
```

This shows your GitHub repository connection.

### 5.2 Push Your Changes

```bash
git push origin main
```

### 5.3 Push Your Branch

```bash
git push origin experiment-projectile
```

### 5.4 Create a Pull Request

1. Go to your repository on GitHub
2. Click "Pull requests" tab
3. Click "New pull request"
4. Select `experiment-projectile` branch
5. Add a description of your changes
6. Click "Create pull request"

### 5.5 Review and Merge

1. Review the changes in the PR
2. Add comments if needed
3. Click "Merge pull request"
4. Delete the branch after merging

### 5.6 Pull Latest Changes

```bash
git checkout main
git pull origin main
```

---

## Part 6: Collaboration Exercise (20 minutes)

### 6.1 Add a New Feature

**Task**: Add a new physics calculation function

1. Create a new branch: `git checkout -b add-kinetic-energy`
2. Open `basic_physics.py`
3. Add this function before `main()`:

```python
def calculate_kinetic_energy(mass, velocity):
    """
    Calculate kinetic energy: KE = 0.5 * m * v²
    
    Args:
        mass: Mass in kilograms
        velocity: Velocity in m/s
    
    Returns:
        Kinetic energy in Joules
    """
    kinetic_energy = 0.5 * mass * velocity ** 2
    return kinetic_energy
```

4. Add this to the end of `main()` function (before the last line):

```python
    # Example 4: Calculate kinetic energy
    velocity_ke = 15  # m/s
    mass_ke = 5  # kg
    ke = calculate_kinetic_energy(mass_ke, velocity_ke)
    print(f"\n4. Kinetic Energy Calculation:")
    print(f"   Mass: {mass_ke} kg")
    print(f"   Velocity: {velocity_ke} m/s")
    print(f"   Kinetic Energy: {ke} J")
```

5. Test your changes:
   ```bash
   python basic_physics.py
   ```

6. Commit and push:
   ```bash
   git add basic_physics.py
   git commit -m "Add kinetic energy calculation function"
   git push origin add-kinetic-energy
   ```

7. Create a Pull Request on GitHub

---

## Part 7: Best Practices (10 minutes)

### Version Control Tips

✅ **DO:**
- Commit often with clear messages
- Create branches for new features
- Pull before you push
- Review your changes before committing

❌ **DON'T:**
- Commit broken code to main
- Use vague commit messages like "fix" or "update"
- Work directly on main for experiments
- Commit generated files (plots, cache files)

### VS Code Tips

- Use `Ctrl+P` (Cmd+P on Mac) to quickly open files
- Use `Ctrl+Shift+P` (Cmd+Shift+P) to open command palette
- Install Python extension for better code editing
- Use the integrated debugger to step through code
- Use Source Control panel (Git icon) for visual Git operations

---

## Challenges for Advanced Users

1. **Challenge 1**: Create a new script that calculates gravitational force between two objects
2. **Challenge 2**: Add error handling to the data analysis script
3. **Challenge 3**: Create a function that plots projectile trajectories
4. **Challenge 4**: Add unit tests for the physics functions
5. **Challenge 5**: Create a Jupyter notebook version of the analysis

---

## Troubleshooting

### Python Import Errors

If you get import errors:
```bash
pip install -r requirements.txt
```

### Git Permission Issues

Configure your Git identity:
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### VS Code Python Not Found

1. Open Command Palette (`Ctrl+Shift+P`)
2. Type "Python: Select Interpreter"
3. Choose your Python installation

---

## Resources

- [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)
- [VS Code Keyboard Shortcuts](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf)
- [Python Style Guide (PEP 8)](https://pep8.org/)
- [GitHub Flow Guide](https://guides.github.com/introduction/flow/)

---

## Next Steps

After this tutorial, you should be able to:
- ✅ Write and run Python scripts in VS Code
- ✅ Track changes with Git
- ✅ Create and merge branches
- ✅ Collaborate using GitHub
- ✅ Create and review Pull Requests

Keep practicing! The more you use these tools, the more natural they'll become.

Happy coding! 🚀
