import json
import os


def _opensearch_hosts():
    hosts = os.getenv("OPENSEARCH_HOSTS", "opensearch:9200")
    try:
        parsed_hosts = json.loads(hosts)
    except (TypeError, json.JSONDecodeError):
        parsed_hosts = hosts

    if isinstance(parsed_hosts, str):
        parsed_hosts = parsed_hosts.split(",")

    return [host.strip() for host in parsed_hosts if isinstance(host, str) and host.strip()]

OPEN_SEARCH_HTTP_PORT = os.environ.get("OPEN_SEARCH_HTTP_PORT", "9200")
OPENSEARCH_DSL_AUTOSYNC = os.environ.get('OPENSEARCH_DSL_AUTOSYNC', 'True') == 'True' 

OPENSEARCH_DSL = {
    'default': {
        'hosts': _opensearch_hosts(),
        'http_auth': (
            f"{os.environ.get('OPENSEARCH_ADMIN')}",
            f"{os.environ.get('OPENSEARCH_PASSWORD')}"
        ),
        'timeout': 120,
    }
}
