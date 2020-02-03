# Roadmap

## v1.0.0
---

**Status**: In Progress

Statikos v1.0.0 includes the minimal viable product feature set.

This includes the following commands:

* `create`: create a Statikos service.
* `deploy`: deploy a Statikos service.
* `publish`: publish content.
* `remove`: remove a Statikos service.

The `statikos.yml` file has the following properties:

`statikos.yml`

```yaml
service:
  name: string
  domain_name: string
  content: string
```

## v1.1.0
---

**Status**: Not Started

Statikos v1.1.0 includes support for adding subject alternative names and using Certificate Validator to facilitate AWS Certificate Manager (ACM) certificate validation via DNS.

The `statikos.yml` file has the following properties:

`statikos.yml`

```yaml
service:
  name: string
  domain_name: string
  subject_alternative_names:
    - string
  validation_method: cv | dns
  content: string
```

## v1.2.0
---

**Status**: Not Started

Statikos v1.2.0 adds *quality-of-live* features. These include:

* Creating YAML or JSON CloudFormation templates.
* Adding console output for CloudFormation events.
* Adding a `test` command.
* Adding a `command` property to `statikos.yml`.

The `statikos.yml` file has the following properties:

`statikos.yml`

```yaml
service:
  name: string
  domain_name: string
  subject_alternative_names:
    - string
  validation_method: cv | dns
  content: string
  command: string
```
