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
    telegraf_plugins_extra:
      # telegraf plugin for sending pulsar metrics to influx
      condor_monitor:
        plugin: exec
        config:
          - commands = [
            "{{ custom_telegraf_env }} python {{ pulsar_consumer_dir }}/pulsar_metric_consumer.py {{ galaxy_config_dir }}/job_conf.yml",
            ]
          - timeout = "10s"
          - data_format = "influx"
          - interval = "1m"

  roles:
      # Fastapi that collects stats about Pulsar nodes
      - role: pdg.pulsar-metric-collection
```

## License

See [LICENSE.md](LICENSE.md)
