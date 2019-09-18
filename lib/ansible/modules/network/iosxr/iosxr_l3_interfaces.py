#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat Inc.
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

##############################################
#                 WARNING
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#
##############################################

"""
The module file for ios_l3_interfaces
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type


ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'network'}


DOCUMENTATION = """
module: iosxr_l3_interfaces
version_added: 2.9
short_description: Manage Layer-3 interface on Cisco IOS-XR devices.
description: This module provides declarative management of Layer-3 interface on Cisco IOS-XR devices.
author: Sumit Jaiswal (@justjais)
notes:
  - Tested against Cisco IOS-XRv Version 6.1.3 on VIRL.
  - This module works with connection C(network_cli).
    See L(the IOS-XR Platform Options,../network/user_guide/platform_iosxr.html).
options:
  config:
    description: A dictionary of Layer-3 interface options
    type: list
    elements: dict
    suboptions:
      name:
        description:
        - Full name of the interface excluding any logical unit number, i.e. GigabitEthernet0/1.
        type: str
        required: True
      ipv4:
        description:
        - IPv4 address to be set for the Layer-3 interface mentioned in I(name) option.
        - The address format is <ipv4 address>/<mask>, the mask is number in range 0-32
          eg. 192.168.0.1/24
        type: list
        suboptions:
          address:
            description:
            - Configures the IPv4 address for Interface.
            type: str
          secondary:
            description:
            - Configures the IP address as a secondary address.
            type: bool
      ipv6:
        description:
        - IPv6 address to be set for the Layer-3 interface mentioned in I(name) option.
        - The address format is <ipv6 address>/<mask>, the mask is number in range 0-128
          eg. fd5d:12c9:2201:1::1/64
        type: list
        suboptions:
          address:
            description:
            - Configures the IPv6 address for Interface.
            type: str
  state:
    choices:
    - merged
    - replaced
    - overridden
    - deleted
    default: merged
    description:
    - The state of the configuration after module completion
    type: str
"""

EXAMPLES = """
---
# Using merged

# Before state:
# -------------
#
# viosxr#show running-config interface
# interface GigabitEthernet0/0/0/1
#  shutdown
# !
# interface GigabitEthernet0/0/0/2
#  shutdown
# !
# interface GigabitEthernet0/0/0/3
#  ipv4 address 192.168.0.2 255.255.255.0
#  shutdown
# !
# interface GigabitEthernet0/0/0/3.700
# !
# interface GigabitEthernet0/0/0/4
#  ipv6 address fd5d:12c9:2201:1::1/64
#  shutdown
# !

- name: Merge provided configuration with device configuration
  iosxr_l3_interfaces:
    config:
      - name: GigabitEthernet0/0/0/2
        ipv4:
        - address: 192.168.0.1/24
      - name: GigabitEthernet0/0/0/3
        ipv4:
        - address: 192.168.2.1/24
          secondary: True
    operation: merged

# After state:
# ------------
#
# viosxr#show running-config interface
# interface GigabitEthernet0/0/0/1
#  shutdown
# !
# interface GigabitEthernet0/0/0/2
#  ipv4 address 192.168.0.1 255.255.255.0
#  shutdown
# !
# interface GigabitEthernet0/0/0/3
#  ipv4 address 192.168.1.0 255.255.255.0
#  ipv4 address 192.168.2.1 255.255.255.0 secondary
#  shutdown
# !
# interface GigabitEthernet0/0/0/3.700
# !
# interface GigabitEthernet0/0/0/4
#  ipv6 address fd5d:12c9:2201:1::1/64
#  shutdown
# !

# Using overridden

# Before state:
# -------------
#
# viosxr#show running-config interface
# interface GigabitEthernet0/0/0/1
#  shutdown
# !
# interface GigabitEthernet0/0/0/2
#  ipv4 address 192.168.0.1 255.255.255.0
#  shutdown
# !
# interface GigabitEthernet0/0/0/3
#  ipv4 address 192.168.1.0 255.255.255.0
#  shutdown
# !
# interface GigabitEthernet0/0/0/3.700
# !
# interface GigabitEthernet0/0/0/4
#  ipv6 address fd5d:12c9:2201:1::1/64
#  shutdown
# !

- name: Override device configuration of all interfaces with provided configuration
  iosxr_l3_interfaces:
    config:
      - name: GigabitEthernet0/0/0/3
        ipv4:
        - address: 192.168.0.1/24
      - name: GigabitEthernet0/0/0/3.700
        ipv4:
        - address: 192.168.0.2/24
        - address: 192.168.2.1/24
          secondary: True
    operation: overridden

# After state:
# -------------
#
# viosxr#show running-config interface
# interface GigabitEthernet0/0/0/1
#  shutdown
# !
# interface GigabitEthernet0/0/0/2
#  shutdown
# !
# interface GigabitEthernet0/0/0/3
#  ipv4 address 192.168.0.1 255.255.255.0
#  shutdown
# !
# interface GigabitEthernet0/0/0/3.700
#  ipv4 address 192.168.0.2 255.255.255.0
#  ipv4 address 192.168.2.1 255.255.255.0 secondary
# !
# interface GigabitEthernet0/0/0/4
#  shutdown
# !

# Using replaced

# Before state:
# -------------
#
# viosxr#show running-config interface
# interface GigabitEthernet0/0/0/1
#  shutdown
# !
# interface GigabitEthernet0/0/0/2
#  shutdown
# !
# interface GigabitEthernet0/0/0/3
#  ipv4 address 192.168.0.2 255.255.255.0
#  shutdown
# !
# interface GigabitEthernet0/0/0/3.700
#  ipv4 address 192.168.0.1 255.255.255.0
# !
# interface GigabitEthernet0/0/0/4
#  ipv6 address fd5d:12c9:2201:1::1/64
#  shutdown
# !

- name: Replaces device configuration of listed interfaces with provided configuration
  iosxr_l3_interfaces:
    config:
      - name: GigabitEthernet0/0/0/3
        ipv6:
        - address: fd5d:12c9:2201:1::1/64
      - name: GigabitEthernet0/0/0/4
        ipv4:
        - address: 192.168.0.2/24
    operation: replaced

# After state:
# -------------
#
# viosxr#show running-config interface
# interface GigabitEthernet0/0/0/1
#  shutdown
# !
# interface GigabitEthernet0/0/0/2
#  shutdown
# !
# interface GigabitEthernet0/0/0/3
#  ipv6 address fd5d:12c9:2201:1::1/64
#  shutdown
# !
# interface GigabitEthernet0/0/0/3.700
#  ipv4 address 192.168.0.1 255.255.255.0
# !
# interface GigabitEthernet0/0/0/4
#  ipv4 address 192.168.0.2 255.255.255.0
#  shutdown
# !

# Using deleted

# Before state:
# -------------
#
# viosxr#show running-config interface
# interface GigabitEthernet0/0/0/1
#  ipv4 address 192.168.2.1 255.255.255.0
#  shutdown
# !
# interface GigabitEthernet0/0/0/2
#  ipv4 address 192.168.3.1 255.255.255.0
#  shutdown
# !
# interface GigabitEthernet0/0/0/3
#  ipv4 address 192.168.0.2 255.255.255.0
#  shutdown
# !
# interface GigabitEthernet0/0/0/3.700
#  ipv4 address 192.168.0.1 255.255.255.0
# !
# interface GigabitEthernet0/0/0/4
#  ipv6 address fd5d:12c9:2201:1::1/64
#  shutdown
# !

- name: "Delete L3 attributes of given interfaces (Note: This won't delete the interface itself)"
  iosxr_l3_interfaces:
    config:
      - name: GigabitEthernet0/0/0/3
      - name: GigabitEthernet0/0/0/4
      - name: GigabitEthernet0/0/0/3.700
    operation: deleted

# After state:
# -------------
#
# viosxr#show running-config interface
# interface GigabitEthernet0/0/0/1
#  ipv4 address 192.168.2.1 255.255.255.0
#  shutdown
# !
# interface GigabitEthernet0/0/0/2
#  ipv4 address 192.168.3.1 255.255.255.0
#  shutdown
# !
# interface GigabitEthernet0/0/0/3
#  shutdown
# !
# interface GigabitEthernet0/0/0/3.700
# !
# interface GigabitEthernet0/0/0/4
#  shutdown
# !

# Using Deleted without any config passed
# "(NOTE: This will delete all of configured resource module attributes from each configured interface)"

# Before state:
# -------------
#
# viosxr#show running-config interface
# interface GigabitEthernet0/0/0/1
#  ipv4 address 192.168.2.1 255.255.255.0
#  shutdown
# !
# interface GigabitEthernet0/0/0/2
#  ipv4 address 192.168.3.1 255.255.255.0
#  shutdown
# !
# interface GigabitEthernet0/0/0/3
#  ipv4 address 192.168.0.2 255.255.255.0
#  shutdown
# !
# interface GigabitEthernet0/0/0/3.700
#  ipv4 address 192.168.0.1 255.255.255.0
# !
# interface GigabitEthernet0/0/0/4
#  ipv6 address fd5d:12c9:2201:1::1/64
#  shutdown
# !


- name: "Delete L3 attributes of all interfaces (Note: This won't delete the interface itself)"
  iosxr_l3_interfaces:
    operation: deleted

# After state:
# -------------
#
# viosxr#show running-config interface
# interface GigabitEthernet0/0/0/1
#  shutdown
# !
# interface GigabitEthernet0/0/0/2
#  shutdown
# !
# interface GigabitEthernet0/0/0/3
#  shutdown
# !
# interface GigabitEthernet0/0/0/3.700
# !
# interface GigabitEthernet0/0/0/4
#  shutdown
# !

"""

RETURN = """
before:
  description: The configuration as structured data prior to module invocation.
  returned: always
  type: list
  sample: The configuration returned will always be in the same format of the parameters above.
after:
  description: The configuration as structured data after module completion.
  returned: when changed
  type: list
  sample: The configuration returned will always be in the same format of the parameters above.
commands:
  description: The set of commands pushed to the remote device
  returned: always
  type: list
  sample: ['interface GigabitEthernet0/0/0/1', 'ipv4 address 192.168.0.1 255.255.255.0']
"""


from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.network.iosxr.argspec.l3_interfaces.l3_interfaces import L3_InterfacesArgs
from ansible.module_utils.network.iosxr.config.l3_interfaces.l3_interfaces import L3_Interfaces


def main():
    """
    Main entry point for module execution
    :returns: the result form module invocation
    """
    required_if = [('state', 'merged', ('config',)),
                   ('state', 'replaced', ('config',)),
                   ('state', 'overridden', ('config',))]

    module = AnsibleModule(argument_spec=L3_InterfacesArgs.argument_spec,
                           required_if=required_if,
                           supports_check_mode=True)

    result = L3_Interfaces(module).execute_module()
    module.exit_json(**result)


if __name__ == '__main__':
    main()
