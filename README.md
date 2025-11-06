#  AWS SSO Python Automation (Work in Progress)

##  Overview
This project is a Python-based personal project to explore AWS automation using SSO, IAM, and Python scripting. It allows centralized automation of common AWS tasks, using:
1. **AWS SSO profiles**: Users choose which SSO profile to use for login..
2. **IAM role chaining**: Python scripts run using assumed IAM roles.
3. **Python scripts**: accounts.py Lists AWS account IDs. iam.py  Lists IAM roles and last-used information.


The main goal is to **demonstrate automated AWS operations** and proper handling of SSO tokens and IAM role chaining.

---

##  Current Status
 Working components:
- Centralized init.sh script with menu, SSO login, and action selection.
- Python scripts: accounts.py and iam.py.
- Virtual environment managed with uv.
- SSO login and role assumption tested successfully.

 In progress:
- Add more Python actions for IAM users, policies, and resource reports.
- Create role for iam permissions listing.
- Put more logic.

---

##  What I’ve Learned So Far
- How  **AWS SSO sessions** work with short-lived credentials.
- Using **boto3.Session(profile_name=…)** for programmatic access.
- Bash scripting patterns for **menus, loops, and environment variables.**  
- Reinforced troubleshooting discipline through trial-and-error experimentation

---


---

##  Project Context
This is a **personal learning project**.
Its purpose is to document growth as a Cloud / DevOps engineer — from manual AWS operations to automated, role-based access scripts.

I started this to connect my interests in:
- **Linux & Bash scripting**
- **AWS Cloud Services (SSO, IAM, Organizations)**
- **Python automation**

---

My aim is to demonstrate:
- Curiosity and willingness to explore complex topics  
- Practical, hands-on problem solving  
- Continuous improvement mindset  

---

## Tech Stack
| Component               | Description                                 |
| ----------------------- | ------------------------------------------- |
| **Python 3.12**         | Main scripting language                     |
| **Boto3 / Botocore**    | AWS SDK for Python                          |
| **AWS SSO**             | Authentication                              |
| **IAM / Organizations** | AWS identity management                     |
| **Bash**                | Automation wrapper (`init.sh`)              |
| **uv**                  | Virtual environment & dependency management |




## Getting Started

### Prerequisites
- Python ≥ 3.12
- uv installed (pip install uv)
- AWS CLI v2 configured with SSO profiles

### Clone
```bash
git clone https://your-repo-url.git
cd LempStackVaultDocker

   ```

2. uv sync
3. source .venv/bin/activate

### Executing program

Run the application using:
```bash
./init.sh

```
##  Author
**Vasileios Siaploulis**  
Cloud / DevOps Engineer in progress 
Passionate about Linux, networking, and secure automation.  



---
