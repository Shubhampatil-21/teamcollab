import click
from tabulate import tabulate

teams = [{'name': 'Backend 2', 'description': 'Handles APIs','members':[]}]
members = [{"name":"Alice",
              "email":'alice@example.com',
              "role":'Developer',
              "team":'Backend',
              },
              {"name":"Alice 1",
              "email":'alice@example.com',
              "role":'Developer',
              "team":'Frontend',
              },
              {"name":"Alice 2",
              "email":'alice@example.com',
              "role":'Developer',
              "team":'Backend',
              }]

@click.group()
def cli():
    pass

#Create a new team
@cli.command()
@click.option('--name',help="You have to mention team name")
@click.option('--description', help="You have to write description")
def add_team(name,description):
    team = {
        "name":name,
        "description":description,
        "members": [],
    }
    teams.append(team)
    click.echo(f'Team name {name} successfully added!')

#List all teams
@cli.command()
def list_teams():
    if not teams:
        click.echo("No teams are added!")
        return
    else:
        for team in teams:
            temp = []
            temp.append([team["name"]])
            click.echo(tabulate(temp,headers=["Team name"]))

#Add member to an existing team       
@cli.command()
@click.option('--name')
@click.option('--email')
@click.option('--role')
@click.option('--team')
def add_member(name,email,role,team):
    member = {"name":name,
              "email":email,
              "role":role,
              "team":team,
              }
    members.append(member)
    for t_team in teams:
        if t_team["name"] == team:
            t_team["members"].append(member)
            click.echo(f'Member {name} is added to the team {team}')

#filtered members by team or role
@cli.command()
@click.option('--team',default = None)
@click.option('--role',default = None)
def list_members(team,role):
    filtered = []
    if team:
        for t in members:
            if t["team"] == team:
                filtered.append(t)
    elif role:
        for t in members:
            if t["role"] == role:
                filtered.append(t)
    if not filtered:
        click.echo("No matching members found")
    else:
        table_data = []
        for i in filtered:
            table_data.append([i["name"], i["email"], i["role"], i["team"]])
        click.echo(tabulate(table_data,headers=["Name", "Email", "Role", "Team"]))



if __name__ == '__main__':
    cli()
