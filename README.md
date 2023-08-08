# owncloud

[![Source Code](https://img.shields.io/badge/github-source%20code-blue?logo=github&amp;logoColor=white)](https://github.com/rolehippie/owncloud)
[![General Workflow](https://github.com/rolehippie/owncloud/actions/workflows/general.yml/badge.svg)](https://github.com/rolehippie/owncloud/actions/workflows/general.yml)
[![Readme Workflow](https://github.com/rolehippie/owncloud/actions/workflows/docs.yml/badge.svg)](https://github.com/rolehippie/owncloud/actions/workflows/docs.yml)
[![Galaxy Workflow](https://github.com/rolehippie/owncloud/actions/workflows/galaxy.yml/badge.svg)](https://github.com/rolehippie/owncloud/actions/workflows/galaxy.yml)
[![License: Apache-2.0](https://img.shields.io/github/license/rolehippie/owncloud)](https://github.com/rolehippie/owncloud/blob/master/LICENSE)
[![Ansible Role](https://img.shields.io/badge/role-rolehippie.owncloud-blue)](https://galaxy.ansible.com/rolehippie/owncloud)

Ansible role to install and configure an ownCloud.

## Sponsor

Building and improving this Ansible role have been sponsored by my current and previous employers like **[Cloudpunks GmbH](https://cloudpunks.de)** and **[Proact Deutschland GmbH](https://www.proact.eu)**.

## Table of content

- [Requirements](#requirements)
- [Default Variables](#default-variables)
  - [owncloud_admin_password](#owncloud_admin_password)
  - [owncloud_admin_username](#owncloud_admin_username)
  - [owncloud_apps_deprecated](#owncloud_apps_deprecated)
  - [owncloud_apps_disable](#owncloud_apps_disable)
  - [owncloud_apps_enable](#owncloud_apps_enable)
  - [owncloud_apps_install](#owncloud_apps_install)
  - [owncloud_apps_uninstall](#owncloud_apps_uninstall)
  - [owncloud_cert_resolver](#owncloud_cert_resolver)
  - [owncloud_db_host](#owncloud_db_host)
  - [owncloud_db_name](#owncloud_db_name)
  - [owncloud_db_password](#owncloud_db_password)
  - [owncloud_db_type](#owncloud_db_type)
  - [owncloud_db_username](#owncloud_db_username)
  - [owncloud_db_utf8mb4](#owncloud_db_utf8mb4)
  - [owncloud_domain](#owncloud_domain)
  - [owncloud_image](#owncloud_image)
  - [owncloud_insecure_middlewares](#owncloud_insecure_middlewares)
  - [owncloud_log_file](#owncloud_log_file)
  - [owncloud_log_level](#owncloud_log_level)
  - [owncloud_log_rotate_size](#owncloud_log_rotate_size)
  - [owncloud_network](#owncloud_network)
  - [owncloud_post_install](#owncloud_post_install)
  - [owncloud_post_server](#owncloud_post_server)
  - [owncloud_pre_install](#owncloud_pre_install)
  - [owncloud_pre_server](#owncloud_pre_server)
  - [owncloud_prefix](#owncloud_prefix)
  - [owncloud_publish_server](#owncloud_publish_server)
  - [owncloud_pull_image](#owncloud_pull_image)
  - [owncloud_redis_db](#owncloud_redis_db)
  - [owncloud_redis_enabled](#owncloud_redis_enabled)
  - [owncloud_redis_host](#owncloud_redis_host)
  - [owncloud_redis_password](#owncloud_redis_password)
  - [owncloud_redis_port](#owncloud_redis_port)
  - [owncloud_secure_middlewares](#owncloud_secure_middlewares)
  - [owncloud_smtp_address](#owncloud_smtp_address)
  - [owncloud_smtp_auth](#owncloud_smtp_auth)
  - [owncloud_smtp_auth_type](#owncloud_smtp_auth_type)
  - [owncloud_smtp_domain](#owncloud_smtp_domain)
  - [owncloud_smtp_host](#owncloud_smtp_host)
  - [owncloud_smtp_mode](#owncloud_smtp_mode)
  - [owncloud_smtp_password](#owncloud_smtp_password)
  - [owncloud_smtp_port](#owncloud_smtp_port)
  - [owncloud_smtp_secure](#owncloud_smtp_secure)
  - [owncloud_smtp_username](#owncloud_smtp_username)
  - [owncloud_version](#owncloud_version)
  - [owncloud_volume_hooks](#owncloud_volume_hooks)
  - [owncloud_volume_server](#owncloud_volume_server)
- [Discovered Tags](#discovered-tags)
- [Dependencies](#dependencies)
- [License](#license)
- [Author](#author)

---

## Requirements

- Minimum Ansible version: `2.10`


## Default Variables

### owncloud_admin_password

Password for the admin user

#### Default value

```YAML
owncloud_admin_password: admin
```

### owncloud_admin_username

Username for the admin user

#### Default value

```YAML
owncloud_admin_username: admin
```

### owncloud_apps_deprecated

List of deprecated apps

#### Default value

```YAML
owncloud_apps_deprecated: []
```

### owncloud_apps_disable

List of apps to disable

#### Default value

```YAML
owncloud_apps_disable: []
```

### owncloud_apps_enable

List of apps to enable

#### Default value

```YAML
owncloud_apps_enable: []
```

### owncloud_apps_install

List of apps to install

#### Default value

```YAML
owncloud_apps_install: []
```

### owncloud_apps_uninstall

List of apps to uninstall

#### Default value

```YAML
owncloud_apps_uninstall: []
```

### owncloud_cert_resolver

Cert resolver within traefik

#### Default value

```YAML
owncloud_cert_resolver:
```

#### Example usage

```YAML
owncloud_cert_resolver: default
```

### owncloud_db_host

Database host

#### Default value

```YAML
owncloud_db_host: mariadb:3306
```

### owncloud_db_name

Database name

#### Default value

```YAML
owncloud_db_name: owncloud
```

### owncloud_db_password

Database password

#### Default value

```YAML
owncloud_db_password:
```

### owncloud_db_type

Database type to use

#### Default value

```YAML
owncloud_db_type: mysql
```

### owncloud_db_username

Database username

#### Default value

```YAML
owncloud_db_username:
```

### owncloud_db_utf8mb4

Enable utf8mb4 database

#### Default value

```YAML
owncloud_db_utf8mb4: true
```

### owncloud_domain

Domain used to access ownCloud

#### Default value

```YAML
owncloud_domain:
```

### owncloud_image

Docker image to use

#### Default value

```YAML
owncloud_image: owncloud/server:{{ owncloud_version }}
```

### owncloud_insecure_middlewares

Insecure middlewares for traefik

#### Default value

```YAML
owncloud_insecure_middlewares:
  - https@file
  - errors@file
```

### owncloud_log_file

Path to logfile within container

#### Default value

```YAML
owncloud_log_file: /dev/stdout
```

### owncloud_log_level

Logging level

#### Default value

```YAML
owncloud_log_level: '2'
```

### owncloud_log_rotate_size

Log rotation file size

#### Default value

```YAML
owncloud_log_rotate_size: '104857600'
```

### owncloud_network

Docker network to connect to

#### Default value

```YAML
owncloud_network:
```

#### Example usage

```YAML
owncloud_network: traefik
```

### owncloud_post_install

List of post server hooks

#### Default value

```YAML
owncloud_post_install: []
```

### owncloud_post_server

List of post install hooks

#### Default value

```YAML
owncloud_post_server: []
```

### owncloud_pre_install

List of pre server hooks

#### Default value

```YAML
owncloud_pre_install: []
```

### owncloud_pre_server

List of pre install hooks

#### Default value

```YAML
owncloud_pre_server: []
```

### owncloud_prefix

Prefix used to access ownCloud

#### Default value

```YAML
owncloud_prefix:
```

### owncloud_publish_server

Publish the service on that binding

#### Default value

```YAML
owncloud_publish_server:
```

### owncloud_pull_image

Pull image as part of the tasks

#### Default value

```YAML
owncloud_pull_image: true
```

### owncloud_redis_db

Redis database

#### Default value

```YAML
owncloud_redis_db:
```

### owncloud_redis_enabled

Enable redis caching

#### Default value

```YAML
owncloud_redis_enabled: true
```

### owncloud_redis_host

Redis host

#### Default value

```YAML
owncloud_redis_host: redis
```

### owncloud_redis_password

Redis password

#### Default value

```YAML
owncloud_redis_password:
```

### owncloud_redis_port

Redis port

#### Default value

```YAML
owncloud_redis_port: 6379
```

### owncloud_secure_middlewares

Secure middlewares for traefik

#### Default value

```YAML
owncloud_secure_middlewares:
  - secure@file
  - errors@file
```

### owncloud_smtp_address

Mail sender address

#### Default value

```YAML
owncloud_smtp_address: owncloud
```

### owncloud_smtp_auth

Enable SMTP auth

#### Default value

```YAML
owncloud_smtp_auth: true
```

### owncloud_smtp_auth_type

Mail auth type

#### Default value

```YAML
owncloud_smtp_auth_type: LOGIN
```

### owncloud_smtp_domain

Mail sender domain

#### Default value

```YAML
owncloud_smtp_domain: example.com
```

### owncloud_smtp_host

Mail server host

#### Default value

```YAML
owncloud_smtp_host:
```

### owncloud_smtp_mode

Mail sending mode

#### Default value

```YAML
owncloud_smtp_mode: smtp
```

### owncloud_smtp_password

Mail server password

#### Default value

```YAML
owncloud_smtp_password:
```

### owncloud_smtp_port

Mail server port

#### Default value

```YAML
owncloud_smtp_port:
```

### owncloud_smtp_secure

Secure mode for mail server

#### Default value

```YAML
owncloud_smtp_secure:
```

### owncloud_smtp_username

Mail server username

#### Default value

```YAML
owncloud_smtp_username:
```

### owncloud_version

Version of the Docker image

#### Default value

```YAML
owncloud_version: 10.12.2
```

### owncloud_volume_hooks

Path to hooks volume

#### Default value

```YAML
owncloud_volume_hooks: /etc/owncloud
```

### owncloud_volume_server

Path to server volume

#### Default value

```YAML
owncloud_volume_server: /var/lib/owncloud
```

## Discovered Tags

**_owncloud_**


## Dependencies

- [rolehippie.docker](https://github.com/rolehippie/docker)
- [rolehippie.traefik](https://github.com/rolehippie/traefik)

## License

Apache-2.0

## Author

[Thomas Boerger](https://github.com/tboerger)
