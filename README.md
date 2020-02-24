# cloudinstancecredentials

Generally in Public Cloud environments one does not want to have applications with a Web UI start automatically without a pre-populated user an password. This utility extracts information from a running instance and sets the web server for the web based UI up to use http-basicauth for login purposes.

The implementation is modular such that it can easily be expanded to other cloud frameworks and web servers.

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
    auth_basic_user_file /etc/nginx/cloudinstancecredentials;
    ...
}
```
