# Exercise 5: Docker Security with AppArmor

## Goal

Run the Flask container under an AppArmor profile and verify that restricted actions are denied.

## Work

The Flask app, Dockerfile, named AppArmor profile, and Docker SDK scripts are included. The `/security-check` endpoint attempts to write under `/etc`; it returns HTTP 403 if the profile blocks the write and HTTP 500 if the write unexpectedly succeeds. The profile also denies reads of `/etc/passwd` and `/etc/shadow`, and execution from `/bin` and `/usr/bin`.

AppArmor profiles must be loaded by a Linux host kernel before Docker can apply them. On Ubuntu, from this directory:

```bash
sudo apt-get update
sudo apt-get install -y apparmor-utils
sudo aa-status
docker build -t flask-apparmor .
sudo install -m 0644 my-apparmor-profile /etc/apparmor.d/my-apparmor-profile
sudo apparmor_parser -r -W /etc/apparmor.d/my-apparmor-profile
docker run --rm -d --name flask-apparmor --security-opt apparmor=my-apparmor-profile -p 127.0.0.1:5000:5000 flask-apparmor
curl -i http://127.0.0.1:5000/
curl -i http://127.0.0.1:5000/security-check
docker rm -f flask-apparmor
python3 -m pip install -r requirements.txt
python3 apply_apparmor.py
python3 test_restricted_actions.py
sudo dmesg | grep apparmor
```

The Docker SDK script builds and starts a container with the loaded profile, inspects the container's `HostConfig.SecurityOpt`, checks the HTTP endpoint, then stops and removes the container. The restricted-action script checks that reading `/etc/passwd` and executing `/bin/bash` fail.

## Environment result

The Mac host does not provide AppArmor to Docker Desktop, so the exercise was run inside an Ubuntu 24.04 VM. Docker in that VM reported AppArmor among its security options and the named profile was attached to the container. In the latest VM check, reading `/etc/passwd` was denied, but executing `/bin/bash` was still allowed; full restriction enforcement is not yet verified.

## Evidence screenshots

The `Screenshots/` directory contains three screenshots supplied for this exercise:

1. `01-apparmor-not-available-on-macos.png` shows that AppArmor is unavailable on the macOS host.
2. `02-apply-apparmor-sdk.png` shows the container starting with the named profile attached.
3. `03-restricted-actions-not-enforced.png` shows an earlier test where `/etc/passwd` was readable and `/bin/bash` executable, so it is not proof that both restrictions passed.

The Ubuntu VM run later confirmed `/etc/passwd` reads were denied, but the Bash check still passed. Add a fresh screenshot after both checks are denied to document full enforcement.
