import nipyapi
from retrying import retry

@retry(wait_fixed=15000)
def connect_to_nifi():
    nipyapi.canvas.get_root_pg_id()


nipyapi.config.nifi_config.host = 'http://nifi:8080/nifi-api'
nipyapi.config.registry_config.host = 'http://nifi:8081/nifi-registry-api'
print("Connecting to nifi...")
connect_to_nifi()
