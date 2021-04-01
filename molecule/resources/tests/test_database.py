import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('omero-database')


def test_services_running_and_enabled(host):
    if host.system_info.distribution == 'ubuntu':
        service = host.service('postgresql@11-main')
    else:
        service = host.service('postgresql-11')
    assert service.is_running
    assert service.is_enabled
