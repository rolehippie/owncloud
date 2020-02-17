import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_service_file(host):
    file = host.file("/etc/systemd/system/owncloud.service")
    assert file.exists
