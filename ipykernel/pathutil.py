import re
from urllib.parse import unquote, urlparse


def detect_os_from_file_uri(file_uri: str) -> str:
    parsed = urlparse(file_uri)
    decoded_path = unquote(parsed.path)
    # Check for Windows drive letter at the beginning: /c:/ or /D:/ etc.
    if re.match(r"^/[a-zA-Z]:/", decoded_path):
        return "Windows"
    if decoded_path.startswith("/"):
        return "Linux"
    return "Linux"
