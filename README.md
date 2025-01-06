# Ansible role: pulsar-metric-collection

A role that installs a collector script that collects the pulsar consumption metrics from the respective amqp queue

## Requirements

No specific requirements, the role is self-contained.

## Role variables

Role variables are documented in the forms of comments on [defaults/main.yml](defaults/main.yml)

## Dependencies

None.

## Example Playbook

```yaml
---
- name: Install and configure a pulsar metric collector script
  hosts: all
  vars:
  roles:
      # Fastapi that collects stats about Pulsar nodes
      - role: pdg.pulsar-metric-collection
```

## License

See [LICENSE.md](LICENSE.md)

