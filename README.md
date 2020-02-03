# Statikos

> στατικός: from ἵστημι (hístēmi, “to stand”) +‎ -ικός (-ikós).

Statikos (στατικός) is Greek for *static*.

Statikos is a Python package for generating static websites using AWS CloudFormation.

## Getting Started

Statikos only requires a domain name and generated static content.

### Step 1: Purchase a domain.

### Step 2: Install Statikos.

```bash
pip install statikos
```

### Step 3: Create `statikos.yml`.

`statikos.yml`

```yaml
stack_name: <stack-name>
domain_name: <domain-name>
```

**Note**: The syntax for `statikos.yml` can be found [here].

### Step 4: Deploy your static website.

```bash
statikos deploy
```
