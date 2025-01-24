# Ansible role: pulsar-metric-collection

A role that either installs a: 
- producer script that sends htcondor stats to an amqp queue on the Pulsar side
- consumer script that collects the metrics from the amqp queue on the Galaxy side, aggregates them and sends them to an InfluxDB

## Requirements

No specific requirements, the role is self-contained.

## Role variables

Role variables are documented in the forms of comments on [defaults/main.yml](defaults/main.yml)

## Dependencies

None.

## Example Playbook

```yaml
---
- name: Install and configure a pulsar metric consumer script
  hosts: all
  vars:
    pulsar_metric_role: consumer
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
      - role: pdg.pulsar-metrics
```

```yaml
---
- name: Install and configure a pulsar metric producer script
  hosts: all
  vars:
    pulsar_metric_role: producer

  roles:
      - role: pdg.pulsar-metrics
```

## License

See [LICENSE.md](LICENSE.md)
