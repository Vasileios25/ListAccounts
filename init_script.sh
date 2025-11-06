#!/bin/bash

PYTHON=python3

# 1. Logout and clear any previous credentials
aws sso logout
granted sso-tokens clear --all

# 2. Initiate AWS SSO config

echo ""
echo "What do you want to run?"
echo "1) List Accounts"
echo "2) IAM Roles"
echo "3) Exit"

read -rp "Choose an option [1-3]: " PROFILE_CHOISE

case $PROFILE_CHOISE in
1)
    aws sso login --profile list-accounts
    export AWS_PROFILE=accounts
    export AWS_SDK_LOAD_CONFIG=1
    
    ;;
2)
    aws sso login --profile sso-base
    export AWS_PROFILE=terraform
    export AWS_SDK_LOAD_CONFIG=1
    
    ;;
3)
    echo "Goodbye!"
    exit 0
    ;;
*)
    echo "Unknown selection. Try again."
    ;;
esac


# 3. Run scripts

while true; do
    echo ""
    echo "What do you want to run?"
    echo "1) List Accounts"
    echo "2) IAM Roles"
    echo "3) Exit"

    read -rp "Choose an option [1-3]: " ACTION

    case $ACTION in
        1)
            python accounts.py
            ;;
        2)
            python iam.py
            ;;
        3)
            echo "Goodbye!"
            exit 0
            ;;
        *)
            echo "Unknown selection. Try again."
            ;;
    esac
done
