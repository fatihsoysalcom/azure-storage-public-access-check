import os
from azure.identity import DefaultAzureCredential
from azure.mgmt.storage import StorageManagementClient

def check_azure_storage_public_access():
    """
    Checks Azure Storage Accounts for public blob access settings
    and reports potential security vulnerabilities.
    """
    subscription_id = os.environ.get("AZURE_SUBSCRIPTION_ID")
    if not subscription_id:
        print("Error: AZURE_SUBSCRIPTION_ID environment variable not set.")
        print("Please set it to your Azure subscription ID.")
        return

    print(f"--- Azure Storage Public Access Security Check for Subscription: {subscription_id} ---")

    try:
        # Authenticate using DefaultAzureCredential.
        # This credential type attempts to authenticate via various methods:
        # environment variables, managed identity, Azure CLI, etc.
        credential = DefaultAzureCredential()
        print("Authenticated to Azure.")

        # Create a Storage Management Client to interact with Azure Storage resources.
        storage_client = StorageManagementClient(credential, subscription_id)

        found_vulnerabilities = False

        # Iterate through all resource groups in the subscription.
        for rg in storage_client.resource_groups.list():
            print(f"\nChecking Resource Group: {rg.name}")

            # List all storage accounts within the current resource group.
            for storage_account in storage_client.storage_accounts.list_by_resource_group(rg.name):
                print(f"  Storage Account: {storage_account.name}")

                # Prowler and other Cloud Security Posture Management (CSPM) tools
                # would check configurations like public access. Here, we check
                # 'allow_blob_public_access'. If True, it means containers within
                # this storage account *can* be configured for public access, which
                # is a potential misconfiguration that security tools flag.
                if storage_account.allow_blob_public_access:
                    print(f"    [ALERT] Public blob access is ALLOWED for this storage account. "
                          f"This is a potential security risk if not intended. "
                          f"Review containers within '{storage_account.name}' for public access settings.")
                    found_vulnerabilities = True
                else:
                    print("    Public blob access is DISABLED (Good security posture).")

        if not found_vulnerabilities:
            print("\n--- No potential public access vulnerabilities found in checked storage accounts. ---")
        else:
            print("\n--- Review the identified storage accounts for public access configurations. ---")

    except Exception as e:
        print(f"\nAn error occurred: {e}")
        print("Ensure you are logged into Azure CLI (`az login`) and have the correct permissions.")

if __name__ == "__main__":
    check_azure_storage_public_access()
