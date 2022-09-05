# Python version can be changed, e.g.
# FROM python:3.8
# FROM docker.io/fnndsc/conda:python3.10.2-cuda11.6.0
FROM docker.io/python:3.10.6-slim-bullseye

LABEL org.opencontainers.image.authors="FNNDSC <dev@babyMRI.org>" \
      org.opencontainers.image.title="heuri-rename" \
      org.opencontainers.image.description="heuri-rename is a ChRIS ds plugin, which copies files from an input directory to an output directory under different names, similar to pl-bulk-rename, but in a more user-friendly manner using heuristics"

WORKDIR /usr/local/src/heuri-rename

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
ARG extras_require=none
RUN pip install ".[${extras_require}]"

CMD ["heuri-rename", "--help"]
