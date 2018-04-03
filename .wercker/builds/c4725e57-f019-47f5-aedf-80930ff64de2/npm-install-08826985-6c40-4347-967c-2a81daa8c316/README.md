# npm-install step

Executes the `npm install` command with leveraging the wercker cache mechanism to improve installation time.

If `npm install` fails, it will be retried three times before failing.

## Options

### options
- type: string
- optional: true
- description: Passed through to npm install
- example: `options: -g bower`

### environment
- type: string
- optional: true
- description: Set node_env to use for npm install
- example: `environment: developement`

## Example

```yaml
build:
    steps:
        - npm-install
            options: $NPM_INSTALL_OPTIONS
            environment: $NPM_INSTALL_ENVIRONMENT
```

# License

The MIT License (MIT)

# Changelog

## 1.1.0

- Add environment option

## 1.0.0

- Add retry on error

## 0.9.3

- Fix wrong directory cache created

## 0.9.2

- Initial release
