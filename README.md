# Team Directory CLI Prototype

The Team Directory CLI is a lightweight, interactive command-line tool designed to simulate the structure and behavior of a team collaboration system.

## Installation

```bash
# Clone the repository
git clone https://github.com/[your-username]/team-directory-cli.git

# Install dependencies
pip install click tabulate
```

## Usage Examples

### Team Management

Add a new team:
```bash
python team_directory.py add-team --name Backend --description "Handles APIs"
```

List all teams:
```bash
python team_directory.py list-teams
```

### Member Management

Add a member:
```bash
python team_directory.py add-member --name "Alice" --email "alice@example.com" --role Developer --team Backend
```

Filter members:

By team:
```bash
python team_directory.py list-members --team Backend
```

By role:
```bash
python team_directory.py list-members --role Developer
```