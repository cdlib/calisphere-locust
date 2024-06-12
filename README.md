# Calisphere Load Testing

[Locust.io](https://docs.locust.io/en/stable/) configurations for load testing a calisphere site.

## Install 

`pipenv install`

## Usage


### Test the public_interface component of Calisphere

```bash
pipenv run locust -f tests/new_calisphere.py
```

### Test the crop / clip component Calisphere

```bash
pipenv run locust -f tests/crop_clip.py
```


