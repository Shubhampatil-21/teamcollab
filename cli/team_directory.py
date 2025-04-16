import click
from tabulate import tabulate
import json

with open("teams.json","r") as teams_data:
    teams = json.load(teams_data)
with open("members.json","r") as teams_data:
    members = json.load(teams_data)

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
    with open("teams.json", "w") as file:
        json.dump(teams, file, indent=4)
    click.echo(f'Team name {name} successfully added!')

#List all teams
@cli.command()
def list_teams():
    temp = []
    if not teams:
        click.echo("No teams are added!")
        return
    else:
        for team in teams:
            temp.append([team["name"]])
        click.echo(tabulate(temp,headers=["Team name"]))

#Add member to an existing team       
@cli.command()
@click.option('--name')
@click.option('--email')
@click.option('--role')
@click.option('--team')
def add_member(name, email, role, team):
    member = {"name":name,
              "email":email,
              "role":role,
              "team":team,
              }
    members.append(member)
    with open("members.json", "w") as file:
        json.dump(members, file, indent=4)
    
    for t_team in teams:
        if t_team["name"] == team:
            t_team["members"].append(member)
            click.echo(f'Member {name} is added to the team {team}')
    with open("teams.json", "w") as file:
        json.dump(teams, file, indent=4)

#filtered members by team or role
@cli.command()
@click.option('--team',default = None)
@click.option('--role',default = None)
@click.option('--name',default = None)
def list_members(team,role, name):
    filtered = []
    if team:
        for t_mem in members:
            if t_mem["team"] == team:
                filtered.append(t_mem)
    elif role:
        for t_mem in members:
            if t_mem["role"] == role:
                filtered.append(t_mem)
    elif name:
        for t_mem in members:
            if t_mem["name"] == name:
                filtered.append(t_mem)

    if not filtered:
        click.echo("No matching members found")
    else:
        table_data = []
        for data in filtered:
            table_data.append([data["name"], data["email"], data["role"], data["team"]])
        click.echo(tabulate(table_data,headers=["Name", "Email", "Role", "Team"]))


if __name__ == '__main__':
    cli()