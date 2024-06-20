import time

import requests
from requests import RequestException, HTTPError

from config import SERVER_API_URL


class LEDService:

    def send_request(self, action, on_time=None, off_time=None):
        try:
            if action in ['ping', 'on', 'off']:
                response = requests.get(f"{SERVER_API_URL}/{action}")
            elif action == "schedule":
                response = requests.post(f"{SERVER_API_URL}/schedule",
                                         json={"time_on_ms": on_time, "time_off_ms": off_time})
            else:
                raise ValueError(f"Invalid action: {action}")

            response.raise_for_status()
            return True, self.format_response(response.json())
        except (RequestException, HTTPError) as e:
            return False, f"Error: {str(e)}"

    @staticmethod
    def format_response(response_json):
        if "status" in response_json:
            status = response_json["status"].lower()
            if status == "scheduled":
                scheduling = response_json.get("scheduling", {})
                time_on = scheduling.get("time_on_ms", "unknown")
                time_off = scheduling.get("time_off_ms", "unknown")
                formatted_response = (f"**LED Status:** Scheduled ⏰\n"
                        f"**Scheduled On Time:** {time_on} ms\n"
                        f"**Scheduled Off Time:** {time_off} ms")
            elif status == "on":
                formatted_response = f"**LED Status:** ON 🟢"
            elif status == "off":
                formatted_response = f"**LED Status:** OFF 🔴"
            else:
                formatted_response = f"**LED Status:** Unknown ❓"
        else:
            formatted_response = "❓ Unknown response format"

        return f"{formatted_response}\n**Last update:** {time.strftime('%m/%d/%Y %H:%M:%S', time.localtime())}"
