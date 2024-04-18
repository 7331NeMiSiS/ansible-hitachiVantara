#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2021, [ Hewlett Packard Enterprise Development LP ]
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'supported_by': 'certified',
                    'status': ['stableinterface']}

DOCUMENTATION = \
    r'''
---
module: hpe_hg_facts
short_description: This module provides Host Group information on the specified HPE XP storage system.
description:
     - The M(hpe_hg_facts) module provides Host Group information on the specified HPE XP storage system.
version_added: '02.9.0'
author:
  - Hewlett Packard Enterprise Development LP. VERSION 02.3.0.7
options:
  collections:
    description:
      - Ansible collections name for HPE XP storage modules 
    type: string
    required: yes
    default: hpe.xp_storage
  data:
    required: yes
    description:
      - data has the following properties
      - =================================================================
      - Getting Host Group  information  Facts
      - =================================================================
      - C(storage_serial:) Mandatory input. integer type. Storage system serial number.
      - C(hgName:) Optional input. string type. Host group name.If specified, return host groups with the input name.
      - C(Ports:) Optional input. array type. Storage FC port.If specified, return all host groups of the input FC ports.
      - C(lun:) Optional input. integer type. LDEV ID.If specified, return all host groups of the input LUN.
      - C(query:) Optional input. Valid values are
      - 1. wwns - Returns all the HBA WWNs available in the hostgroup
      - 2. luns - Returns all the LUNS mapped to the hostgroup
      - =================================================================
'''

EXAMPLES = \
    r'''
-
  name: Testing Get Host Group
  hosts: localhost
  gather_facts: false
  collections:
    - hpe.xp_storage
  vars:
    - storage_serial: 30074
    - hgName: test-ansible-hg-1-210
    - ports:
      - CL2-B
  tasks:
    - hpe_hg_facts:
        storage_serial: '{{ storage_serial }}'
        data:
          query: '{{ query | default(None) }}'
          lun: '{{ lun | default(None) }}'
          name: '{{ hgName | default(None) }}'
          ports: '{{ ports | default(None) }}'
      register: result
    - debug: var=result.hostGroups
'''

RETURN = r'''
'''

import json

import ansible_collections.hpe.xp_storage.plugins.module_utils.hv_hg_facts_runner as runner
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.hpe.xp_storage.plugins.module_utils.hv_infra import StorageSystem, \
    HostMode, StorageSystemManager
try:
    from ansible_collections.hpe.xp_storage.plugins.module_utils.hv_logger import MessageID
    HAS_MESSAGE_ID = True
except ImportError as error:
    HAS_MESSAGE_ID = False
from ansible_collections.hpe.xp_storage.plugins.module_utils.hv_log import Log, \
    HiException

logger = Log()


def main(module=None):
    fields = {'storage_serial': {'required': True, 'type': 'int'},
              'data': {'required': False, 'type': 'json'}}

    if module is None:
        module = AnsibleModule(argument_spec=fields)

    try:
        runner.runPlaybook(module)
    except HiException as ex:
        if HAS_MESSAGE_ID:
            logger.writeAMException(MessageID.ERR_OPERATION_HOSTGROUP)
        else:
            logger.writeAMException("0X0000")
        module.fail_json(msg=ex.format())
    except Exception as ex:
        try:
            storageSystem = StorageSystem(module.params['storage_serial'])
            if storageSystem.isSessionNotFound(ex.message):
                StorageSystemManager.addStorgeSystemByJson()
                runner.runPlaybook(module)
            else:
                module.fail_json(msg=ex.message)
        except Exception as ex2:
            module.fail_json(msg=ex.message + '. ' + ex2.message)


if __name__ == '__main__':
    main()
