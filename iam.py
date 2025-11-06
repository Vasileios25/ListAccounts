import boto3
import datetime

iam = boto3.resource('iam')
iam_client = boto3.client('iam')
response = iam_client.list_roles()
today = datetime.datetime.now(datetime.timezone.utc)  # stay timezone-aware
cutoff_days = 60

for user in iam.users.all():
    last = getattr(user, 'password_last_used', None)  # datetime or None
    if last is None:
        # Never logged in to console (could be a candidate to remove if unused)
        print(f"{user.user_name}, NEVER")
    else:   
        delta_days = (today - last).days
        if delta_days >= cutoff_days:
            print(f"{user.user_name}, {delta_days} days")


while True:
    for iam_role in response['Roles'] :
        name = iam_role['RoleName']
        details = iam_client.get_role(RoleName=name)
        last = details['Role'].get('RoleLastUsed', {}).get('LastUsedDate')  

        if last is None:
           print(f"Role {name}, NEVER")
        else:
            delta_days = (today - last).days
            if delta_days >= cutoff_days:
                print(f"Role {name}, {delta_days} days")

    if response.get('IsTruncated'):
        response = iam_client.list_roles(Marker=response['Marker'])
    else:
        break