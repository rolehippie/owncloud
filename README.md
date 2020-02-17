# owncloud

[![Build Status](https://cloud.drone.io/api/badges/rolehippie/owncloud/status.svg)](https://cloud.drone.io/rolehippie/owncloud)

Ansible role to configure owncloud

## Table of content

* [Default Variables](#default-variables)
  * [owncloud_admin_password](#owncloud_admin_password)
  * [owncloud_admin_username](#owncloud_admin_username)
  * [owncloud_apps_deprecated](#owncloud_apps_deprecated)
  * [owncloud_apps_disable](#owncloud_apps_disable)
  * [owncloud_apps_enable](#owncloud_apps_enable)
  * [owncloud_apps_install](#owncloud_apps_install)
  * [owncloud_apps_uninstall](#owncloud_apps_uninstall)
  * [owncloud_cert_resolver](#owncloud_cert_resolver)
  * [owncloud_db_host](#owncloud_db_host)
  * [owncloud_db_name](#owncloud_db_name)
  * [owncloud_db_password](#owncloud_db_password)
  * [owncloud_db_type](#owncloud_db_type)
  * [owncloud_db_username](#owncloud_db_username)
  * [owncloud_db_utf8mb4](#owncloud_db_utf8mb4)
  * [owncloud_domain](#owncloud_domain)
  * [owncloud_image](#owncloud_image)
  * [owncloud_insecure_middlewares](#owncloud_insecure_middlewares)
  * [owncloud_log_file](#owncloud_log_file)
  * [owncloud_log_level](#owncloud_log_level)
  * [owncloud_log_rotate_size](#owncloud_log_rotate_size)
  * [owncloud_network](#owncloud_network)
  * [owncloud_post_install](#owncloud_post_install)
  * [owncloud_post_server](#owncloud_post_server)
  * [owncloud_pre_install](#owncloud_pre_install)
  * [owncloud_pre_server](#owncloud_pre_server)
  * [owncloud_prefix](#owncloud_prefix)
  * [owncloud_publish_server](#owncloud_publish_server)
  * [owncloud_redis_db](#owncloud_redis_db)
  * [owncloud_redis_enabled](#owncloud_redis_enabled)
  * [owncloud_redis_host](#owncloud_redis_host)
  * [owncloud_redis_password](#owncloud_redis_password)
  * [owncloud_redis_port](#owncloud_redis_port)
  * [owncloud_secure_middlewares](#owncloud_secure_middlewares)
  * [owncloud_smtp_address](#owncloud_smtp_address)
  * [owncloud_smtp_auth](#owncloud_smtp_auth)
  * [owncloud_smtp_auth_type](#owncloud_smtp_auth_type)
  * [owncloud_smtp_domain](#owncloud_smtp_domain)
  * [owncloud_smtp_host](#owncloud_smtp_host)
  * [owncloud_smtp_mode](#owncloud_smtp_mode)
  * [owncloud_smtp_password](#owncloud_smtp_password)
  * [owncloud_smtp_port](#owncloud_smtp_port)
  * [owncloud_smtp_secure](#owncloud_smtp_secure)
  * [owncloud_smtp_username](#owncloud_smtp_username)
  * [owncloud_volume_hooks](#owncloud_volume_hooks)
  * [owncloud_volume_server](#owncloud_volume_server)
* [Dependencies](#dependencies)
* [License](#license)
* [Author](#author)

---

## Default Variables

### owncloud_admin_password

#### Default value

```YAML
owncloud_admin_password: admin
```

### owncloud_admin_username

#### Default value

```YAML
owncloud_admin_username: admin
```

### owncloud_apps_deprecated

#### Default value

```YAML
owncloud_apps_deprecated: []
```

### owncloud_apps_disable

#### Default value

```YAML
owncloud_apps_disable: []
```

### owncloud_apps_enable

#### Default value

```YAML
owncloud_apps_enable: []
```

### owncloud_apps_install

#### Default value

```YAML
owncloud_apps_install: []
```

### owncloud_apps_uninstall

#### Default value

```YAML
owncloud_apps_uninstall: []
```

### owncloud_cert_resolver

Cert resolver within traefik

#### Default value

```YAML
owncloud_cert_resolver: default
```

### owncloud_db_host

#### Default value

```YAML
owncloud_db_host: mariadb:3306
```

### owncloud_db_name

#### Default value

```YAML
owncloud_db_name: owncloud
```

### owncloud_db_password

#### Default value

```YAML
owncloud_db_password:
```

### owncloud_db_type

#### Default value

```YAML
owncloud_db_type: mysql
```

### owncloud_db_username

#### Default value

```YAML
owncloud_db_username:
```

### owncloud_db_utf8mb4

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
owncloud_image: owncloud/server:10.3
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

#### Default value

```YAML
owncloud_log_file: /dev/stdout
```

### owncloud_log_level

#### Default value

```YAML
owncloud_log_level: '2'
```

### owncloud_log_rotate_size

#### Default value

```YAML
owncloud_log_rotate_size: '104857600'
```

### owncloud_network

Docker network to connect to

#### Default value

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

Redis password

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

### owncloud_redis_db

#### Default value

```YAML
owncloud_redis_db:
```

### owncloud_redis_enabled

#### Default value

```YAML
owncloud_redis_enabled: true
```

### owncloud_redis_host

#### Default value

```YAML
owncloud_redis_host: redis
```

### owncloud_redis_password

#### Default value

```YAML
owncloud_redis_password:
```

### owncloud_redis_port

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

#### Default value

```YAML
owncloud_smtp_address: owncloud
```

### owncloud_smtp_auth

#### Default value

```YAML
owncloud_smtp_auth: true
```

### owncloud_smtp_auth_type

#### Default value

```YAML
owncloud_smtp_auth_type: LOGIN
```

### owncloud_smtp_domain

#### Default value

```YAML
owncloud_smtp_domain: example.com
```

### owncloud_smtp_host

#### Default value

```YAML
owncloud_smtp_host:
```

### owncloud_smtp_mode

#### Default value

```YAML
owncloud_smtp_mode: smtp
```

### owncloud_smtp_password

#### Default value

```YAML
owncloud_smtp_password:
```

### owncloud_smtp_port

#### Default value

```YAML
owncloud_smtp_port:
```

### owncloud_smtp_secure

#### Default value

```YAML
owncloud_smtp_secure:
```

### owncloud_smtp_username

#### Default value

```YAML
owncloud_smtp_username:
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

## Dependencies

None.

## License

Apache-2.0

## Author

Thomas Boerger
