# cloudinstancecredentials

Generally in Public Cloud environments one does not want to have applications with a Web UI start automatically without a pre-populated user an password. This utility extracts information from a running instance and sets the web server for the web based UI up to use http-basicauth for login purposes.

The implementation is modular such that it can easily be expanded to other cloud frameworks and web servers.

## Sources

#### AWS

Credentials for _EC2_ instances in _AWS_ are derived from IMDS:

* _username:_ the EC2 Instance ID
* _password:_ the EC2 instance's owner account ID (no dashes)

#### Azure

Credentials for _Azure Virtual Machines_ are derived from IMDS:

* _username:_ the VM instance name
* _password:_ the VM owner's subscription ID (UUID)

#### GCP

Credentials for _Google Compute Engine_ instances are derived from IMDS:

* _username:_ the VM instance ID
* _password:_ the VM instance name

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
