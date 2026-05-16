# Azure Storage Public Access Check

This Python script demonstrates how to programmatically check Azure Storage Accounts for public blob access settings using the Azure SDK. It simulates a basic security audit step that a Cloud Security Posture Management (CSPM) tool like Prowler would perform to identify potential vulnerabilities in your Azure environment.

## Language

`python`

## How to Run

1. Install required packages: `pip install azure-identity azure-mgmt-storage`
2. Set your Azure Subscription ID: `export AZURE_SUBSCRIPTION_ID="YOUR_SUBSCRIPTION_ID"`
3. Ensure you are logged into Azure CLI: `az login`
4. Run the script: `python check_azure_storage_security.py`

## Original Article

This example accompanies the Turkish article: [Azure'da Prowler Kurulumu: Güvenlik Denetiminde Pratik Bir Rehber](https://fatihsoysal.com/blog/azureda-prowler-kurulumu-guvenlik-denetiminde-pratik-bir-rehber/).

## License

MIT — see [LICENSE](LICENSE).
