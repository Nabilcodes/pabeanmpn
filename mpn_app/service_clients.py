import httpx

class DJBCServiceClient:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.client = httpx.Client(base_url=self.base_url)

    def send_ntpn(self, ntpn_data: dict) -> str:
        response = self.client.post("/api/receive-ntpn", json=ntpn_data)
        response.raise_for_status()
        return response.text
