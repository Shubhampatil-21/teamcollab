### 🚀 Feature: Team Directory CLI Prototype

**Summary:**
This PR introduces a basic command-line interface for simulating team collaboration entities (members, roles, teams). This helps visualize early-stage model relationships and lays the groundwork for future API/backend integrations.

**Features:**
- Add team
- Add member with role and team
- List members by role or team

**Testing Instructions:**
```bash
# Add team
python team_directory.py add-team --name Backend

# Add member
python team_directory.py add-member --name Alice --email alice@example.com --role Developer --team Backend

# List members
python team_directory.py list-members --team Backend