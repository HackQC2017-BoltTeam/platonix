# Platonix

Automated license plate recognition server using [OpenALPR](http://www.openalpr.com/) and [Flask](http://flask.pocoo.org/).

## Build

```bash
docker build -t platonix .
```

## Run

"Production" mode:

```bash
docker run -d \
    -p 5000:5000 \
    --name platonix \
    platonix
```

Development mode:

```bash
docker run -d \
    -p 5000:5000 \
    -e FLASK_DEBUG=1 \
    --name platonix \
    -v $PWD:/srv/platonix \
    platonix
```

## API

`/ping` (validate the server is working):

```bash
curl http://localhost:5000/ping
```

`/photo` (upload and get results):

```bash
curl -F 'file=@plate_img.jpg' http://localhost:5000/photo
```
