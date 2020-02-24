# cloudinstancecredentials

Command line tools for setting authorization credentials based on metadata present in a public cloud VM instance.

## Utilities

### set-http-basic-credentials

Sets credentials for http-basic authorization in NGINX web servers.

#### Usage

On a supported[*](lib/cloudinstancecredentials/) public cloud VM instance:
```
sudo set-http-basic-credentials
```

Alternatively, enable the one-shot service:
```
sudo systemctl enable set-http-basic-credentials.service
```

Any vhost config using this authorization should include the following config:
```
server {
    ...
    auth_basic	         'Authorization required';
    auth_basic_user_file /etc/nginx/.htpasswd;
    ...
}
```