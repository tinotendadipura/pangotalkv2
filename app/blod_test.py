from google.oauth2 import service_account
import google.auth.transport.requests

# Path to your service account JSON file
SERVICE_ACCOUNT_FILE = '/path/to/your-service-account.json'

# Authenticate
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE,
    scopes=["https://www.googleapis.com/auth/cloud-platform"]
)

# Refresh and generate token
request = google.auth.transport.requests.Request()
credentials.refresh(request)

# Print the access token
print("Access Token:", credentials.token)
