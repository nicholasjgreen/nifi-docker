import nipyapi
from retrying import retry
from os import listdir
from os.path import isfile, join

@retry(wait_fixed=15000)
def connect_to_nifi():
    nipyapi.canvas.get_root_pg_id()

nipyapi.config.nifi_config.host = 'http://nifi:8080/nifi-api'
nipyapi.config.registry_config.host = 'http://nifi:8081/nifi-registry-api'
print("Connecting to nifi...")
connect_to_nifi()

rootPg = nipyapi.canvas.get_root_pg_id()
print("Root process group =", rootPg)

templates_path = "/app/templates/"
template_files = [join(templates_path, f) for f in listdir(templates_path) if isfile(join(templates_path, f))]
for template_file in template_files:
    print("Creating template", template_file)
    response = nipyapi.templates.upload_template(rootPg, template_file)
    templateId = response.template.id
    nipyapi.templates.deploy_template(rootPg, templateId)

# Start the process group
print("Starting root process group")
nipyapi.canvas.schedule_process_group(rootPg, True)

print("Done!")
