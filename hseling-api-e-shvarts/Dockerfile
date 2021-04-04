FROM hseling/hseling-api-base:python3.6-alpine3.7 as hseling_api_build

LABEL maintainer="e-shvArts Team <shvarts.edition@gmail.com>"

RUN mkdir /dependencies
COPY ./hseling-api-e-shvarts/requirements.txt /dependencies/requirements.txt
COPY ./hseling-api-e-shvarts/setup.py /dependencies/setup.py

RUN pip install -r /dependencies/requirements.txt

FROM hseling/hseling-api-base:python3.6-alpine3.7 as production

COPY --from=hseling_api_build /usr/local/lib/python3.6/site-packages /usr/local/lib/python3.6/site-packages
COPY --from=hseling_api_build /usr/lib/python3.6/site-packages /usr/lib/python3.6/site-packages

COPY --from=hseling_api_build /dependencies /dependencies

COPY ./hseling-lib-e-shvarts /dependencies/hseling-lib-e-shvarts
RUN pip install /dependencies/hseling-lib-e-shvarts

COPY ./hseling-api-e-shvarts/hseling_api_e_shvarts /app/hseling_api_e_shvarts
COPY ./hseling-api-e-shvarts/main.py /app/main.py

RUN mkdir -p /data

ENV HSELING_API_E_SHVARTS_SETTINGS="/app/hseling_api_e_shvarts/default_settings.py"

HEALTHCHECK CMD curl --fail http://localhost:5000/api/healthz || exit 1

